# -*- coding: utf-8 -*-
"""ECMX-004 검사기.

ECMX-002에서 배운 것 하나: 경고만 내는 검사는 통과한 것과 구별되지 않는다.
그래서 여기서는 기본이 FAIL이고, WARN은 '사람이 눈으로 볼 것'이라고 분명히 표시한 항목뿐이다.
"""
import csv, json, os, re, sys, collections

BASE = "/mnt/user-data/outputs/ECMX4"
META = os.path.join(BASE, "tools", "citemeta4.json")

SCHEMA = {
    "scaffold_bom.csv": ["item_id", "layer", "name_ko", "name_en", "role_in_rc_system",
                         "material_scope", "necessity", "necessity_basis", "evidence_type",
                         "evidence_ref", "experiment_summary", "quant_spec", "supplier",
                         "catalog_no", "grade", "origin", "alternatives", "risk",
                         "confidence", "confidence_reason"],
    "rc_params.csv": ["param_id", "param_name", "material", "condition", "value", "unit",
                      "method", "effect", "evidence_ref", "confidence", "confidence_reason"],
    "medium_bom.csv": ["item_id", "category", "name_ko", "name_en", "function", "necessity",
                       "tissue_scope", "stage", "conc_typical", "conc_range", "form",
                       "xeno_status", "evidence_type", "evidence_ref", "experiment_summary",
                       "supplier", "catalog_no", "grade", "stock_storage", "alternatives",
                       "risk", "confidence", "confidence_reason"],
    "medium_delta.csv": ["delta_id", "name_ko", "prev_necessity", "new_necessity", "prev_conc",
                         "new_conc", "change_kind", "reason", "evidence_type", "evidence_ref",
                         "confidence"],
}

MAT_OK = {"A", "B", "C"}
XENO_OK = {"이종유래 없음", "동물유래 포함", "동물유래 — 대체재 있음",
           "동물유래 — 대체재 없음", "불명(확보 실패)"}
CHANGE_OK = {"필수도 변경", "농도 변경", "대체재 변경", "신규 추가", "삭제", "변경 없음 — 재확인"}

NEC = {"필수", "조건부", "선택"}
CONF = {"상", "중", "하"}
EVT = {"OMIT", "SUBST", "DOSE", "CLAIM", "REVIEW", "VENDOR"}
HEDGE = ["추후", "향후 조사", "향후 검토", "다음 단계에서", "추가 확인이 필요", "추가 조사가 필요",
         "TBD", "unknown", "Unknown", "차후"]
# '미정'은 '미정의(조성이 규명되지 않음)'와 겹친다. 뒤에 '의'가 오면 유예 표현이 아니다.
HEDGE_RE = [(re.compile(r"미정(?!의)"), "미정")]
NODATA = {"정량 근거 없음", "해당 없음", "—", "-", ""}
UNIT_RE = re.compile(
    r"(mg/mL|µg/mL|ug/mL|μg/mL|ng/mL|pg/mL|g/L|mg/L|%|×|x\b|mM|µM|uM|μM|nM|M\b|U/mL|U/g|U/mg|"
    r"EU/mg|EU/mL|EU/g|ppm|kPa|MPa|\bPa\b|℃|°C|°|분\b|시간|일\b|주\b|rpm|×g|xg|g\b|mL|µL|uL|μL|L\b|"
    r"kDa|Da|cP|mOsm|osm|bp|nm|µm|um|μm|mm|cm|pH|v/v|w/v|매\b|건\b|개\b|부\b|회\b|매/|배\b)", re.I)

fails, warns, notes = [], [], []


def F(code, msg):
    fails.append(f"[{code}] {msg}")


def W(code, msg):
    warns.append(f"[{code}] {msg}")


def read(fn):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def refs_of(s):
    """evidence_ref 문자열에서 식별자만 뽑는다."""
    s = str(s or "")
    # 옛 DOI는 괄호를 포함한다: 10.1016/0006-291x(92)91234-5
    out = re.findall(r"10\.\d{4,9}/(?:\([^)\s]*\)|[^\s;,\]\"'])+", s)
    out = [re.sub(r"[.,;\]]+$", "", x) for x in out]
    out += re.findall(r"\b(?:US|WO|EP|KR|JP|CN)[\s-]?\d{4,}[A-Z0-9]*\b", s)
    out += re.findall(r"\bPMC\d{5,}\b", s)
    out += re.findall(r"\bPMID[:\s]*(\d{6,})\b", s)
    return [re.sub(r"[.,;)\]]+$", "", x) for x in out]


# ── 1. 스키마 ────────────────────────────────────────────────
def check_schema():
    for fn, cols in SCHEMA.items():
        rows = read(fn)
        if rows is None:
            F("V1", f"{fn} 없음")
            continue
        if not rows:
            F("V1", f"{fn} 행 없음")
            continue
        got = list(rows[0].keys())
        if got != cols:
            miss = [c for c in cols if c not in got]
            extra = [c for c in got if c not in cols]
            F("V1", f"{fn} 헤더 불일치 — 누락 {miss} / 추가 {extra}")


# ── 2. 최소 분량 ─────────────────────────────────────────────
def check_counts():
    s = read("scaffold_bom.csv") or []
    if len(s) < 60:
        F("V2", f"scaffold_bom.csv {len(s)}행 (최소 60)")
    by = collections.Counter((r.get("layer") or "").strip().upper() for r in s)
    for L, n in (("L1", 10), ("L5", 8), ("L6", 10), ("L9", 12)):
        if by.get(L, 0) < n:
            F("V2", f"scaffold_bom.csv {L} {by.get(L,0)}행 (최소 {n})")
    miss = [f"L{i}" for i in range(1, 10) if by.get(f"L{i}", 0) == 0]
    if miss:
        F("V2", f"scaffold_bom.csv 비어 있는 층위 {miss}")
    p = read("rc_params.csv") or []
    if len(p) < 30:
        F("V2", f"rc_params.csv {len(p)}행 (최소 30)")
    m = read("medium_bom.csv") or []
    if len(m) < 65:
        F("V2", f"medium_bom.csv {len(m)}행 (최소 65)")
    bc = collections.Counter((r.get("category") or "").strip() for r in m)
    for c, n in (("니치성장인자", 6), ("저분자", 6)):
        if bc.get(c, 0) < n:
            F("V2", f"medium_bom.csv 범주 '{c}' {bc.get(c,0)}행 (최소 {n})")
    d = read("medium_delta.csv") or []
    if len(d) < 20:
        F("V2", f"medium_delta.csv {len(d)}행 (최소 20)")


# ── 2b. 재료 축 ─────────────────────────────────────────────
def check_material():
    """material_scope가 비어 있거나 읽히지 않으면 이 보고서의 핵심 축이 무너진다."""
    rows = read("scaffold_bom.csv") or []
    seen = collections.Counter()
    for i, r in enumerate(rows, 2):
        s = (r.get("material_scope") or "").strip()
        if not s:
            F("V2b", f"scaffold_bom.csv:{i} material_scope 비어 있음")
            continue
        if "전 조합" in s or "전체" in s:
            got = MAT_OK
        else:
            got = {m for m in MAT_OK if re.search(rf"\b{m}\b", s)}
        if not got:
            F("V2b", f"scaffold_bom.csv:{i} material_scope '{s[:24]}' 에서 A/B/C를 읽을 수 없음")
            continue
        seen[frozenset(got)] += 1
    for m in MAT_OK:
        n = sum(v for k, v in seen.items() if m in k)
        if n == 0:
            F("V2b", f"재료 {m}에 해당하는 행이 하나도 없음 — 세 재료를 모두 다뤄야 한다")
    if seen and len(seen) == 1:
        F("V2b", "모든 행의 material_scope가 동일 — 재료별 차이를 구분하지 않았다")
    notes.append("material_scope 조합 분포: "
                 + ", ".join(f"{'+'.join(sorted(k))}:{v}" for k, v in
                             sorted(seen.items(), key=lambda kv: -kv[1])[:8]))

    pr = read("rc_params.csv") or []
    bad = [i for i, r in enumerate(pr, 2) if not (r.get("material") or "").strip()]
    if bad:
        F("V2b", f"rc_params.csv material 열 비어 있음 {len(bad)}행 — 첫 행 {bad[:5]}")


# ── 2c. 이종유래 축 ─────────────────────────────────────────
def check_xeno():
    rows = read("medium_bom.csv") or []
    cnt = collections.Counter()
    for i, r in enumerate(rows, 2):
        v = (r.get("xeno_status") or "").strip()
        if v not in XENO_OK:
            F("V2c", f"medium_bom.csv:{i} xeno_status '{v[:24]}' 는 정해진 값이 아님")
        else:
            cnt[v] += 1
    if cnt:
        notes.append("xeno_status 분포: " + ", ".join(f"{k} {v}" for k, v in cnt.most_common()))
    d = read("medium_delta.csv") or []
    for i, r in enumerate(d, 2):
        k = (r.get("change_kind") or "").strip()
        if k not in CHANGE_OK:
            F("V2c", f"medium_delta.csv:{i} change_kind '{k[:20]}' 는 정해진 값이 아님")
        if not (r.get("reason") or "").strip():
            F("V2c", f"medium_delta.csv:{i} reason 비어 있음 — 변경 사유 없는 변경은 쓸 수 없다")


# ── 2d. delta가 실제 이전 판정과 맞는가 ─────────────────────
PREV = "/mnt/user-data/outputs/ECMX2/medium_bom.csv"


def check_delta_against_prev():
    """delta의 prev_necessity가 ECMX-003 실물과 어긋나면, 변경 내역 자체를 믿을 수 없다.

    '무엇이 바뀌었다'는 주장은 바뀌기 전 값이 맞아야 성립한다. 그래서 대조한다.
    """
    d = read("medium_delta.csv") or []
    if not d or not os.path.exists(PREV):
        return
    prev = {}
    with open(PREV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            nm = (r.get("name_ko") or "").strip()
            if nm:
                prev[nm] = (r.get("necessity") or "").strip()
    miss = matched = 0
    for i, r in enumerate(d, 2):
        nm = (r.get("name_ko") or "").strip()
        # '성분명 (MD-011 → MD4-011)' 형태의 추적 표기를 떼어 낸다
        nm = re.sub(r"\s*\((?:MD|MD4)[^)]*\)\s*$", "", nm).strip()
        nm = re.sub(r"\s*—\s*[^—]*$", "", nm).strip() if " — " in nm else nm
        pn = (r.get("prev_necessity") or "").strip()
        kind = (r.get("change_kind") or "").strip()
        if kind == "신규 추가":
            if pn and not re.match(r"^\s*(—|-|없음|해당\s*없음|신규|N/?A)", pn):
                F("V2d", f"medium_delta.csv:{i} '신규 추가'인데 prev_necessity가 '{pn}'")
            continue
        # 이름이 정확히 같지 않을 수 있으므로 부분 일치까지 본다
        hit = prev.get(nm)
        if hit is None:
            cand = [v for k, v in prev.items() if nm and (nm in k or k in nm)]
            hit = cand[0] if len(cand) == 1 else None
        if hit is None:
            miss += 1
            W("V2d", f"medium_delta.csv:{i} '{nm[:22]}' 를 ECMX-003 BOM에서 찾지 못함")
            continue
        matched += 1
        if pn and pn != hit:
            F("V2d", f"medium_delta.csv:{i} '{nm[:20]}' prev_necessity '{pn}' "
                     f"≠ ECMX-003 실제 '{hit}'")
    notes.append(f"delta 대조: 이전 BOM과 이름이 맞은 행 {matched}, 못 찾은 행 {miss}")


# ── 3. 값 도메인 ─────────────────────────────────────────────
def check_domain():
    for fn in ("scaffold_bom.csv", "medium_bom.csv"):
        for i, r in enumerate(read(fn) or [], 2):
            n = (r.get("necessity") or "").strip()
            if n not in NEC:
                F("V3", f"{fn}:{i} necessity '{n}'")
            c = (r.get("confidence") or "").strip()
            if c not in CONF:
                F("V3", f"{fn}:{i} confidence '{c}'")
            if not (r.get("confidence_reason") or "").strip():
                F("V3", f"{fn}:{i} confidence_reason 비어 있음")
            for t in re.split(r"[;,]", r.get("evidence_type") or ""):
                t = t.strip()
                if t and t not in EVT:
                    F("V3", f"{fn}:{i} evidence_type '{t}'")
    for i, r in enumerate(read("rc_params.csv") or [], 2):
        if (r.get("confidence") or "").strip() not in CONF:
            F("V3", f"rc_params.csv:{i} confidence '{r.get('confidence')}'")
        if not (r.get("method") or "").strip():
            F("V3", f"rc_params.csv:{i} method 비어 있음 — 측정법 없는 물성치는 쓸 수 없다")
        if not (r.get("unit") or "").strip():
            F("V3", f"rc_params.csv:{i} unit 비어 있음")


# ── 4. 인용 실재성 ───────────────────────────────────────────
def check_refs():
    if not os.path.exists(META):
        F("V4", "citemeta3.json 없음 — 인용 검증 불가")
        return set()
    meta = json.load(open(META, encoding="utf-8"))
    keys = set(meta)
    bad, used = collections.Counter(), set()
    for fn in ("scaffold_bom.csv", "medium_bom.csv", "rc_params.csv", "medium_delta.csv"):
        for i, r in enumerate(read(fn) or [], 2):
            got = refs_of(r.get("evidence_ref"))
            et = {x.strip() for x in re.split(r"[;,]", r.get("evidence_type") or "") if x.strip()}
            if not got and et and et != {"VENDOR"}:
                W("V4", f"{fn}:{i} evidence_ref에 식별자 없음인데 근거 성격이 {sorted(et)} — "
                        f"'{str(r.get('evidence_ref'))[:40]}'")
            for k in got:
                kl = k.lower().replace(" ", "").replace("-", "")
                hit = kl in keys or k.lower() in keys
                if not hit:
                    for cand in (k.lower(), kl, kl.upper().lower()):
                        if cand in keys:
                            hit = True
                            break
                if hit:
                    used.add(k)
                else:
                    bad[k] += 1
    if bad:
        F("V4", f"수집 자료에 없는 식별자 {len(bad)}종 — " +
          ", ".join(f"{k}({v})" for k, v in bad.most_common(8)))
    notes.append(f"인용 식별자 실재 확인 {len(used)}종")
    return used


# ── 5. 유예 표현 ─────────────────────────────────────────────
def check_hedge():
    for fn in ("01_rc_scaffold.md", "02_medium.md"):
        p = os.path.join(BASE, fn)
        if not os.path.exists(p):
            F("V5", f"{fn} 없음")
            continue
        t = open(p, encoding="utf-8").read()
        for h, rx in [(h, re.compile(re.escape(h))) for h in HEDGE] + \
                     [(lbl, rx) for rx, lbl in HEDGE_RE]:
            for m in rx.finditer(t):
                ctx = t[max(0, m.start() - 60):m.start() + 60].replace("\n", " ")
                # 규칙 자체를 인용한 문장은 제외
                if "금지" in ctx or "쓰지 않" in ctx or "적지 않" in ctx:
                    continue
                F("V5", f"{fn} 유예 표현 '{h}' — …{ctx.strip()[:90]}…")
    for fn in ("scaffold_bom.csv", "medium_bom.csv", "rc_params.csv", "medium_delta.csv"):
        for i, r in enumerate(read(fn) or [], 2):
            blob = " ".join(str(v) for v in r.values())
            hit = next((h for h in HEDGE if h in blob), None)
            if not hit:
                hit = next((lbl for rx, lbl in HEDGE_RE if rx.search(blob)), None)
            if hit:
                F("V5", f"{fn}:{i} 유예 표현 '{hit}'")


# ── 6. 단위 ──────────────────────────────────────────────────
def check_units():
    for i, r in enumerate(read("scaffold_bom.csv") or [], 2):
        q = (r.get("quant_spec") or "").strip()
        if (q in NODATA or q.startswith("확보 실패") or q.startswith("정량 근거 없음")
                or q.startswith("배지 소관") or q.startswith("해당 없음")):
            continue
        if not UNIT_RE.search(q):
            F("V6", f"scaffold_bom.csv:{i} quant_spec에 단위 없음 — '{q[:44]}'")
    for i, r in enumerate(read("medium_bom.csv") or [], 2):
        for col in ("conc_typical", "conc_range"):
            v = (r.get(col) or "").strip()
            if (v in NODATA or v.startswith("확보 실패") or v.startswith("정량 근거 없음")
                    or v.startswith("해당 없음") or not re.search(r"\d", v)):
                continue
            if not UNIT_RE.search(v):
                F("V6", f"medium_bom.csv:{i} {col}에 단위 없음 — '{v[:34]}'")


# ── 7. 두 계통 분리 ──────────────────────────────────────────
MX_ONLY = ["콜라겐", "가교", "EDC", "NHS", "제니핀", "genipin", "트랜스글루타미네이스",
           "글루타르알데하이드", "매트리젤", "Matrigel", "알지네이트", "하이드로겔"]
MD_ONLY = ["B-27", "B27", "N-2 보충", "Advanced DMEM", "GlutaMAX", "페니실린", "프리모신",
           "Primocin", "니코틴아마이드"]


def check_separation():
    for i, r in enumerate(read("medium_bom.csv") or [], 2):
        nm = ((r.get("name_ko") or "") + " " + (r.get("name_en") or "")).strip()
        for w in MX_ONLY:
            if w.lower() in nm.lower():
                F("V7", f"medium_bom.csv:{i} 매트릭스 성분이 배지 BOM에 있음 — '{nm[:30]}'")
                break
    for i, r in enumerate(read("scaffold_bom.csv") or [], 2):
        nm = ((r.get("name_ko") or "") + " " + (r.get("name_en") or "")).strip()
        L = (r.get("layer") or "").strip().upper()
        for w in MD_ONLY:
            if w.lower() in nm.lower():
                F("V7", f"scaffold_bom.csv:{i} 배지 성분이 지지체 BOM에 있음 — '{nm[:30]}'")
                break
        if L == "L4":
            blob = " ".join([r.get("role_in_collagen_system") or "",
                             r.get("necessity_basis") or "", r.get("quant_spec") or ""])
            if ("결합" not in blob and "고정" not in blob and "테더" not in blob
                    and "배지 소관" not in blob and "매트릭스" not in blob):
                W("V7", f"scaffold_bom.csv:{i} L4 행이 매트릭스 결합형인지 불명 — '{nm[:26]}'")


# ── 8. G′ / E 혼동 ───────────────────────────────────────────
def check_rheology():
    for i, r in enumerate(read("rc_params.csv") or [], 2):
        u = (r.get("unit") or "").lower()
        nm = (r.get("param_name") or "")
        meth = (r.get("method") or "")
        # 점도(Pa·s)는 탄성률이 아니다 — 같은 'Pa'가 들어 있을 뿐이다.
        if re.search(r"pa\s*[·.*]?\s*s", u):
            continue
        if not re.search(r"\b(pa|kpa|mpa)\b", u):
            continue
        isG = ("G′" in nm or "G'" in nm or "저장" in nm or "storage" in nm.lower())
        isE = ("영률" in nm or "young" in nm.lower() or "E " in nm or "탄성계수" in nm)
        if isG and isE:
            F("V8", f"rc_params.csv:{i} 한 행에 G′와 E를 함께 적음 — '{nm[:40]}'")
        if isG and re.search(r"AFM|압축|compress|인장|tensile", meth, re.I):
            F("V8", f"rc_params.csv:{i} G′인데 측정법이 '{meth[:26]}' — 유변계가 아님")
        if isE and re.search(r"유변계|rheo|진동|oscillat", meth, re.I):
            F("V8", f"rc_params.csv:{i} 영률인데 측정법이 '{meth[:26]}' — 유변계 출력은 G′다")
        if not (isG or isE):
            W("V8", f"rc_params.csv:{i} 탄성률 단위인데 G′/E 구분이 param_name에 없음 — '{nm[:34]}'")


# ── 9. 보고서 HTML ───────────────────────────────────────────
ALLOWED_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com")


def check_html(fn, need_fonts):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        F("V9", f"{fn} 없음")
        return
    t = open(p, encoding="utf-8").read()
    ext = re.findall(r'(?:src|href)\s*=\s*"(https?://[^"]+)"', t)
    for u in ext:
        host = re.sub(r"^https?://([^/]+).*$", r"\1", u)
        if host not in ALLOWED_HOSTS:
            F("V9", f"{fn} 외부 리소스 — {u[:70]}")
    if not need_fonts and ext:
        F("V9", f"{fn} 자립본인데 외부 리소스 {len(ext)}건")
    figs = len(re.findall(r"<figure", t))
    svgs = len(re.findall(r"<svg", t))
    if figs < 10:
        F("V9", f"{fn} 그림 {figs}개 (최소 10)")
    if svgs < figs:
        F("V9", f"{fn} figure {figs}개인데 svg {svgs}개")
    ids = set(re.findall(r'\sid="([^"]+)"', t))
    hrefs = set(re.findall(r'href="#([^"]+)"', t))
    broken = sorted(hrefs - ids)
    if broken:
        F("V9", f"{fn} 깨진 앵커 {len(broken)}개 — {broken[:6]}")
    if "<img" in t:
        F("V9", f"{fn} <img> 사용 — 도판은 전부 인라인 SVG여야 한다")
    notes.append(f"{fn}: 그림 {figs} · SVG {svgs} · 앵커 {len(ids)} · 외부 {len(ext)}")


# ── 10. 본문 수치 ↔ CSV 정합 ────────────────────────────────
def check_prose():
    """보고서가 스스로 말한 개수와 실제 CSV 행 수가 어긋나면 잡는다(ECMX-002의 교훈)."""
    p = os.path.join(BASE, "ECMX004_report.html")
    if not os.path.exists(p):
        return
    t = open(p, encoding="utf-8").read()
    real = {"지지체": len(read("scaffold_bom.csv") or []),
            "배지": len(read("medium_bom.csv") or [])}
    for m in re.finditer(r"(지지체|배지)\s*BOM[^。\.]{0,24}?\*{0,2}(\d{1,4})\s*(?:행|개|건|품목)", t):
        k, v = m.group(1), int(m.group(2))
        if v != real[k]:
            F("V10", f"본문 '{k} BOM {v}' ≠ 실제 {real[k]}")


def main():
    check_schema(); check_counts(); check_material(); check_xeno(); check_delta_against_prev(); check_domain()
    check_refs(); check_hedge(); check_units()
    check_separation(); check_rheology()
    check_html("ECMX004_report.html", need_fonts=False)
    if os.path.exists(os.path.join(BASE, "ECMX004_report_artifact.html")):
        check_html("ECMX004_report_artifact.html", need_fonts=True)
    check_prose()

    print("=" * 74)
    print("ECMX-004 검사 결과")
    print("=" * 74)
    for n in notes:
        print("  · " + n)
    print(f"\nFAIL {len(fails)}건 / WARN {len(warns)}건")
    for x in fails[:80]:
        print("  FAIL " + x)
    if len(fails) > 80:
        print(f"  … 외 {len(fails)-80}건")
    for x in warns[:40]:
        print("  WARN " + x)
    if len(warns) > 40:
        print(f"  … 외 {len(warns)-40}건")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
