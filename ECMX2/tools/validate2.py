# -*- coding: utf-8 -*-
"""ECMX-003 검사기.

ECMX-002에서 배운 것 하나: 경고만 내는 검사는 통과한 것과 구별되지 않는다.
그래서 여기서는 기본이 FAIL이고, WARN은 '사람이 눈으로 볼 것'이라고 분명히 표시한 항목뿐이다.
"""
import csv, json, os, re, sys, collections

BASE = "/mnt/user-data/outputs/ECMX2"
META = os.path.join(BASE, "tools", "citemeta3.json")

SCHEMA = {
    "scaffold_bom.csv": ["item_id", "layer", "name_ko", "name_en", "role_in_collagen_system",
                         "necessity", "necessity_basis", "evidence_type", "evidence_ref",
                         "experiment_summary", "quant_spec", "supplier", "catalog_no", "grade",
                         "origin", "alternatives", "risk", "confidence", "confidence_reason"],
    "collagen_params.csv": ["param_id", "param_name", "condition", "value", "unit", "method",
                            "effect", "evidence_ref", "confidence", "confidence_reason"],
    "medium_bom.csv": ["item_id", "category", "name_ko", "name_en", "function", "necessity",
                       "tissue_scope", "stage", "conc_typical", "conc_range", "form",
                       "evidence_type", "evidence_ref", "experiment_summary", "supplier",
                       "catalog_no", "grade", "stock_storage", "alternatives", "risk",
                       "confidence", "confidence_reason"],
}

NEC = {"필수", "조건부", "선택"}
CONF = {"상", "중", "하"}
EVT = {"OMIT", "SUBST", "DOSE", "CLAIM", "REVIEW", "VENDOR"}
HEDGE = ["추후", "향후 조사", "향후 검토", "다음 단계에서", "추가 확인이 필요", "추가 조사가 필요",
         "TBD", "unknown", "Unknown", "미정", "차후"]
NODATA = {"정량 근거 없음", "해당 없음", "—", "-", ""}
UNIT_RE = re.compile(
    r"(mg/mL|µg/mL|ug/mL|μg/mL|ng/mL|pg/mL|g/L|mg/L|%|×|x\b|mM|µM|uM|μM|nM|M\b|U/mL|U/g|U/mg|"
    r"EU/mg|EU/mL|EU/g|ppm|kPa|MPa|\bPa\b|℃|°C|°|분\b|시간|일\b|주\b|rpm|×g|xg|g\b|mL|µL|uL|μL|L\b|"
    r"kDa|Da|cP|mOsm|osm|bp|nm|µm|um|μm|mm|cm|pH|v/v|w/v)", re.I)

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
    out = re.findall(r"10\.\d{4,9}/[^\s;,)\]\"']+", s)
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
    if len(s) < 55:
        F("V2", f"scaffold_bom.csv {len(s)}행 (최소 55)")
    by = collections.Counter((r.get("layer") or "").strip().upper() for r in s)
    for L, n in (("L6", 8), ("L8", 10)):
        if by.get(L, 0) < n:
            F("V2", f"scaffold_bom.csv {L} {by.get(L,0)}행 (최소 {n})")
    miss = [f"L{i}" for i in range(1, 10) if by.get(f"L{i}", 0) == 0]
    if miss:
        F("V2", f"scaffold_bom.csv 비어 있는 층위 {miss}")
    p = read("collagen_params.csv") or []
    if len(p) < 25:
        F("V2", f"collagen_params.csv {len(p)}행 (최소 25)")
    m = read("medium_bom.csv") or []
    if len(m) < 45:
        F("V2", f"medium_bom.csv {len(m)}행 (최소 45)")
    bc = collections.Counter((r.get("category") or "").strip() for r in m)
    for c, n in (("니치성장인자", 6), ("저분자", 6)):
        if bc.get(c, 0) < n:
            F("V2", f"medium_bom.csv 범주 '{c}' {bc.get(c,0)}행 (최소 {n})")
    mm = read("medium_matrix.csv") or []
    if len(mm) < 20:
        F("V2", f"medium_matrix.csv {len(mm)}행 (최소 20)")
    if mm:
        need = ["장", "간", "뇌", "신장", "폐", "췌장", "위", "종양"]
        have = list(mm[0].keys())
        miss = [t for t in need if t not in have]
        if miss:
            F("V2", f"medium_matrix.csv 조직 열 누락 {miss}")
        if have and have[0] != "성분":
            F("V2", f"medium_matrix.csv 첫 열이 '성분'이 아님 — '{have[0]}'")


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
    for i, r in enumerate(read("collagen_params.csv") or [], 2):
        if (r.get("confidence") or "").strip() not in CONF:
            F("V3", f"collagen_params.csv:{i} confidence '{r.get('confidence')}'")
        if not (r.get("method") or "").strip():
            F("V3", f"collagen_params.csv:{i} method 비어 있음 — 측정법 없는 물성치는 쓸 수 없다")
        if not (r.get("unit") or "").strip():
            F("V3", f"collagen_params.csv:{i} unit 비어 있음")
    mm = read("medium_matrix.csv") or []
    for i, r in enumerate(mm, 2):
        for k, v in r.items():
            if k == "성분" or v is None:
                continue
            v = v.strip()
            if v and not any(v.startswith(x) for x in ("필수", "조건부", "선택", "미사용")):
                F("V3", f"medium_matrix.csv:{i} 열 '{k}' 값이 등급으로 시작하지 않음 — '{v[:24]}'")


# ── 4. 인용 실재성 ───────────────────────────────────────────
def check_refs():
    if not os.path.exists(META):
        F("V4", "citemeta3.json 없음 — 인용 검증 불가")
        return set()
    meta = json.load(open(META, encoding="utf-8"))
    keys = set(meta)
    bad, used = collections.Counter(), set()
    for fn in ("scaffold_bom.csv", "medium_bom.csv", "collagen_params.csv"):
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
    for fn in ("01_collagen_scaffold.md", "02_medium.md"):
        p = os.path.join(BASE, fn)
        if not os.path.exists(p):
            F("V5", f"{fn} 없음")
            continue
        t = open(p, encoding="utf-8").read()
        for h in HEDGE:
            for m in re.finditer(re.escape(h), t):
                ctx = t[max(0, m.start() - 60):m.start() + 60].replace("\n", " ")
                # 규칙 자체를 인용한 문장은 제외
                if "금지" in ctx or "쓰지 않" in ctx or "적지 않" in ctx:
                    continue
                F("V5", f"{fn} 유예 표현 '{h}' — …{ctx.strip()[:90]}…")
    for fn in ("scaffold_bom.csv", "medium_bom.csv", "collagen_params.csv"):
        for i, r in enumerate(read(fn) or [], 2):
            blob = " ".join(str(v) for v in r.values())
            for h in HEDGE:
                if h in blob:
                    F("V5", f"{fn}:{i} 유예 표현 '{h}'")
                    break


# ── 6. 단위 ──────────────────────────────────────────────────
def check_units():
    for i, r in enumerate(read("scaffold_bom.csv") or [], 2):
        q = (r.get("quant_spec") or "").strip()
        if q in NODATA or q.startswith("확보 실패"):
            continue
        if not UNIT_RE.search(q):
            F("V6", f"scaffold_bom.csv:{i} quant_spec에 단위 없음 — '{q[:44]}'")
    for i, r in enumerate(read("medium_bom.csv") or [], 2):
        for col in ("conc_typical", "conc_range"):
            v = (r.get(col) or "").strip()
            if v in NODATA or v.startswith("확보 실패") or not re.search(r"\d", v):
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
    for i, r in enumerate(read("collagen_params.csv") or [], 2):
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
            F("V8", f"collagen_params.csv:{i} 한 행에 G′와 E를 함께 적음 — '{nm[:40]}'")
        if isG and re.search(r"AFM|압축|compress|인장|tensile", meth, re.I):
            F("V8", f"collagen_params.csv:{i} G′인데 측정법이 '{meth[:26]}' — 유변계가 아님")
        if isE and re.search(r"유변계|rheo|진동|oscillat", meth, re.I):
            F("V8", f"collagen_params.csv:{i} 영률인데 측정법이 '{meth[:26]}' — 유변계 출력은 G′다")
        if not (isG or isE):
            W("V8", f"collagen_params.csv:{i} 탄성률 단위인데 G′/E 구분이 param_name에 없음 — '{nm[:34]}'")


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
    p = os.path.join(BASE, "ECMX003_report.html")
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
    check_schema(); check_counts(); check_domain()
    check_refs(); check_hedge(); check_units()
    check_separation(); check_rheology()
    check_html("ECMX003_report.html", need_fonts=False)
    if os.path.exists(os.path.join(BASE, "ECMX003_report_artifact.html")):
        check_html("ECMX003_report_artifact.html", need_fonts=True)
    check_prose()

    print("=" * 74)
    print("ECMX-003 검사 결과")
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
