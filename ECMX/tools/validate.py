#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ECMX-002 자동 검사기 (§13-3).
검사 항목
  1) 스키마 필드 결측         (material_inventory.csv / essential_*.csv)
  2) L1~L9 층위 커버리지
  3) AX-1~AX-9 기능축 커버리지
  4) E0/E1 근거유형 적법성    (REVIEW/VENDOR 단독 금지)
  5) 신뢰도 판정 사유 누락
  6) §4 금지 수치 문자열
  7) HTML 외부 자원 참조
  8) ORGANOID_TYPES 행 존재 (essential_matrix.csv)
  9) 유예 표현(R-03) 검사
사용:  python3 tools/validate.py [BASE_DIR]
종료코드 0=통과, 1=실패
"""
import collections, csv, json, os, re, sys

BASE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LAYERS = [f"L{i}" for i in range(1, 10)]
AXES   = [f"AX-{i}" for i in range(1, 10)]
TIERS  = ["E0", "E1", "E2", "E3"]
EVID   = ["OMIT", "SUBST", "DOSE", "CLAIM", "REVIEW", "VENDOR"]
STRONG = {"OMIT", "SUBST", "DOSE"}
CONF   = ["상", "중", "하"]

ORGANOID_TYPES = ["장", "간", "뇌", "신장", "폐", "췌장", "위", "종양"]

INV_FIELDS = ["material_id","name_ko","name_en","synonyms","layer","function_role",
  "ecm_counterpart","essentiality","evidence_ref","patent_ref","supplier","catalog_no",
  "grade","origin","spec","price","alternatives","risk","confidence","confidence_reason"]

ESS_FIELDS = ["essential_id","name_ko","name_en","layer","axis","tier","evidence_type",
  "evidence_ref","experiment_summary","patent_ref","tissue_scope","quant_range",
  "alternatives","open_issues","confidence","confidence_reason"]

# §4 금지 수치/서술 — 무비판 인용 금지
FORBIDDEN = [
  (r"12\s*억\s*달러|1\.2\s*billion|USD\s*1\.2\s*B", "금지수치1: 오가노이드 '지지체' 시장 12억 달러"),
  (r"(17|18)\s*%\s*(의\s*)?(연평균|CAGR)|CAGR\s*(of\s*)?1[78]", "금지수치1: CAGR 17~18%"),
  (r"9\s*0\s*%\s*(가|는|이상)?\s*(특정|단일|한)\s*사", "금지수치2: '90% 특정사 의존'"),
  (r"28[,.]?000\s*(리터|L\b|litre|liter)", "금지수치3: 매트릭스 사용량 28,000 L"),
  (r"(FDA|미국\s*식품의약국)[^。\.\n]{0,40}(오가노이드)[^。\.\n]{0,20}(승인|허용)", "금지서술4: FDA가 오가노이드를 승인/허용"),
]
# 금지수치를 '반박·주의'로 인용하는 문맥은 허용
REBUTTAL_HINT = re.compile(
    r"금지\s*수치|인용하지\s*(말|않)|사실이\s*아니|것이\s*아니다|승인한\s*것이\s*아니|"
    r"반박|순환\s*파생|§4|배제(함|했|한다)|추적\s*가능한\s*1차\s*출처가?\s*(없|부재)|"
    r"정확히\s*말하면|오기재|오해|잘못\s*(된|전용)|무비판")

DEFER = [r"이후\s*조사하겠", r"추가\s*확인이\s*필요", r"다음\s*단계에서\s*다루", r"추후\s*보완",
         r"향후\s*조사", r"TBD\b", r"to\s+be\s+determined",
         r"추후\s*(에\s*)?(다루|검토|보강|조사)", r"향후\s*(과제로|검토|보강)", r"다음\s*단계로\s*미",
         r"차후\s*(에\s*)?(다루|검토)"]

errors, warns, info = [], [], []


def read_csv(path):
    p = os.path.join(BASE, path)
    if not os.path.exists(p):
        errors.append(f"[파일없음] {path}")
        return None, []
    with open(p, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows, (rows[0].keys() if rows else [])


def check_schema(rows, fields, label, idkey):
    if rows is None:
        return
    missing_cols = [c for c in fields if c not in (rows[0].keys() if rows else [])]
    if missing_cols:
        errors.append(f"[{label}] 스키마 열 누락: {missing_cols}")
    blanks = 0; cells = 0
    for r in rows:
        for c in fields:
            if c in r:
                cells += 1
                v = (r.get(c) or "").strip()
                if v == "":
                    blanks += 1
                    errors.append(f"[{label}] 결측 공란: {r.get(idkey,'?')} / {c} — 결측 사유 문자열 필요")
                elif v.lower() == "unknown":
                    errors.append(f"[{label}] 'unknown' 사용 금지: {r.get(idkey,'?')} / {c}")
    rate = (blanks / cells * 100) if cells else 100.0
    info.append(f"[{label}] 행 {len(rows)}건, 필수필드 결측률 {rate:.1f}%")
    return rate


def main():
    # --- M2 인벤토리 ---
    inv, _ = read_csv("material_inventory.csv")
    if inv:
        rate = check_schema(inv, INV_FIELDS, "M2", "material_id")
        if rate is not None and rate >= 20.0:
            errors.append(f"[G2] 결측률 {rate:.1f}% ≥ 20% 기준 초과")
        seen = {}
        for r in inv:
            seen.setdefault(r.get("layer", "").strip(), 0)
            seen[r.get("layer", "").strip()] += 1
        missing_layers = [l for l in LAYERS if seen.get(l, 0) == 0]
        if missing_layers:
            errors.append(f"[G2] 미탐색 층위: {missing_layers}")
        else:
            info.append(f"[G2] L1~L9 전 층위 등재 확인: " +
                        ", ".join(f"{l}={seen[l]}" for l in LAYERS))
        info.append(f"[G2] 총 물질 {len(inv)}건")
        if len(inv) < 80:
            errors.append(f"[G2] MIN_MATERIALS=80 미달 ({len(inv)})")
        ids = [r.get("material_id") for r in inv]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            errors.append(f"[M2] material_id 중복: {sorted(dup)}")
        # 공급사/카탈로그 보유율 (G3, L1·L6·L7)
        tgt = [r for r in inv if r.get("layer") in ("L1", "L6", "L7")]
        ok = [r for r in tgt
              if r.get("supplier", "").strip() and r.get("catalog_no", "").strip()
              and "미확인" not in r.get("catalog_no", "")
              and "해당없음" not in r.get("catalog_no", "")]
        if tgt:
            pct = len(ok) / len(tgt) * 100
            info.append(f"[G3] L1·L6·L7 공급사+카탈로그 보유율 {pct:.1f}% ({len(ok)}/{len(tgt)})")
            if pct < 60:
                errors.append(f"[G3] 보유율 {pct:.1f}% < 60% 기준")

    # --- M3 필수물질 ---
    ess, _ = read_csv("essential_items.csv")
    if ess:
        check_schema(ess, ESS_FIELDS, "M3", "essential_id")
        ax_hit = set()
        for r in ess:
            for a in AXES:
                if re.search(a + r"(?!\d)", r.get("axis", "")):
                    ax_hit.add(a)
            t = r.get("tier", "").strip()
            if t not in TIERS:
                errors.append(f"[M3] 잘못된 등급값: {r.get('essential_id')} = '{t}'")
            ets = [e.strip() for e in re.split(r"[;,/|]", r.get("evidence_type", "")) if e.strip()]
            for e in ets:
                if e not in EVID:
                    errors.append(f"[M3] 잘못된 근거유형: {r.get('essential_id')} = '{e}'")
            if t in ("E0", "E1") and not (set(ets) & STRONG):
                errors.append(f"[M3][핵심위반] {r.get('essential_id')} 등급 {t} 인데 "
                              f"OMIT/SUBST/DOSE 근거 없음 (근거유형={ets}) — R-13 위반")
            if t in ("E0", "E1") and set(ets) and set(ets) <= {"REVIEW", "VENDOR"}:
                errors.append(f"[M3][핵심위반] {r.get('essential_id')} REVIEW/VENDOR 단독으로 {t} 부여")
            c = r.get("confidence", "").strip()
            if c not in CONF:
                errors.append(f"[M3] 신뢰도 등급값 오류: {r.get('essential_id')} = '{c}'")
            if len((r.get("confidence_reason") or "").strip()) < 5:
                errors.append(f"[M3] 신뢰도 판정 사유 누락: {r.get('essential_id')}")
        miss_ax = [a for a in AXES if a not in ax_hit]
        if miss_ax:
            errors.append(f"[G4] 미탐색 기능축: {miss_ax}")
        else:
            info.append("[G4] AX-1~AX-9 전 축 탐색 확인")
        info.append(f"[G4] M3 등재 {len(ess)}건 / 축 커버 {len(ax_hit)}개")

    # --- 조직 매트릭스 ---
    mtx, _ = read_csv("essential_matrix.csv")
    if mtx:
        col0 = list(mtx[0].keys())[0]
        tissues = " ".join(r.get(col0, "") for r in mtx)
        miss_t = [t for t in ORGANOID_TYPES if t not in tissues]
        if miss_t:
            errors.append(f"[G4] essential_matrix.csv 조직 행 누락: {miss_t}")
        else:
            info.append(f"[G4] ORGANOID_TYPES 8개 조직 행 모두 존재 ({len(mtx)}행)")
        bad = []
        for r in mtx:
            for k, v in r.items():
                if k == col0 or v is None:
                    continue
                v = v.strip()
                if v and v.split("(")[0].strip() not in TIERS + ["-", "n/a", "근거없음"]:
                    bad.append(f"{r.get(col0)}/{k}={v}")
        if bad:
            errors.append(f"[G4] 매트릭스 셀 값이 E0~E3 규격 밖: {bad[:10]}")

    # --- 텍스트 산출물 검사 ---
    md_files = [f for f in os.listdir(BASE) if f.endswith(".md")]
    for f in sorted(md_files):
        txt = open(os.path.join(BASE, f), encoding="utf-8").read()
        for line_no, line in enumerate(txt.splitlines(), 1):
            for pat, name in FORBIDDEN:
                if re.search(pat, line, re.I):
                    ctx = line
                    if not REBUTTAL_HINT.search(ctx):
                        errors.append(f"[§4] {f}:{line_no} {name} — 무비판 인용 의심: {line.strip()[:90]}")
                    else:
                        info.append(f"[§4] {f}:{line_no} {name} — 반박/주의 문맥으로 확인(허용)")
            if f != "gaps.md":
                for d in DEFER:
                    if re.search(d, line):
                        errors.append(f"[R-03] {f}:{line_no} 유예 표현 사용: {line.strip()[:80]}")
        # 헤더 검사
        if not txt.startswith("---\nagent:"):
            errors.append(f"[§7] {f} 메시지 패싱 헤더 누락")

    # --- HTML 외부 자원 검사 ---
    html = os.path.join(BASE, "ECMX_report.html")
    if os.path.exists(html):
        h = open(html, encoding="utf-8").read()
        ext = []
        ext += re.findall(r'<(?:script|img|iframe|video|audio|source|embed)[^>]*\ssrc\s*=\s*["\'](?!data:)([^"\']+)', h, re.I)
        ext += re.findall(r'<link[^>]*\shref\s*=\s*["\'](?!#|data:)([^"\']+)', h, re.I)
        ext += re.findall(r'@import\s+(?:url\()?["\']([^"\']+)', h, re.I)
        ext += re.findall(r'url\(\s*["\']?(https?://[^)"\']+)', h, re.I)
        ext = [e for e in ext if not e.startswith("#")]
        if ext:
            errors.append(f"[G9] HTML 외부 자원 참조 {len(ext)}건: {ext[:8]}")
        else:
            info.append("[G9] HTML 외부 자원 참조 0건 (자체 완결형 확인)")
        # 앵커 대응
        anchors = set(re.findall(r'\sid\s*=\s*["\']([^"\']+)', h))
        links = set(re.findall(r'href\s*=\s*["\']#([^"\']+)', h))
        dead = sorted(links - anchors)
        if dead:
            errors.append(f"[G9] 끊어진 내부 앵커 {len(dead)}건: {dead[:10]}")
        else:
            info.append(f"[G9] 내부 앵커 {len(links)}개 전부 대상 존재")
        figs = len(re.findall(r"<figure", h, re.I))
        info.append(f"[G8] HTML 내 <figure> {figs}개")
        if figs < 10:
            errors.append(f"[G8] MIN_FIGURES=10 미달 ({figs})")
        svgs = len(re.findall(r"<svg", h, re.I))
        info.append(f"[G8] 인라인 SVG {svgs}개")
        # 필수 삽입 문단
        if "자유실시(FTO)" not in h:
            errors.append("[§9-6] 필수 삽입 문단 누락")
        for line_no, line in enumerate(h.splitlines(), 1):
            for pat, name in FORBIDDEN:
                if re.search(pat, line, re.I) and not REBUTTAL_HINT.search(line):
                    errors.append(f"[§4] HTML:{line_no} {name} 무비판 인용 의심")



    check_extra()
    check_prose()
    check_grade_mapping()
    check_evidence_count()


    print("=" * 72)
    for i in info:
        print("  INFO  " + i)
    for w in warns:
        print("  WARN  " + w)
    for e in errors:
        print("  FAIL  " + e)
    print("-" * 72)
    print(f"결과: {'PASS' if not errors else 'FAIL'}  (오류 {len(errors)}건)")
    return 1 if errors else 0


# ─────────── 확장 검사 (V 감사 반려-009 반영) ───────────
BAD_MISSING = ("unknown", "미상", "n/a", "na", "-", "?", "미정")

SUP_FIELDS = ["supplier_id","supplier_name","country","category","product_name","catalog_no",
  "grade","origin","spec","price","pack_size","storage","lead_time","supply_risk",
  "source_url","verified_date","confidence","confidence_reason"]
PLS_FIELDS = ["patent_id","title","assignee","assignee_type","jurisdiction","priority_date",
  "filing_date","pub_date","ipc","tech_category","claim_checked","legal_status","expiry_note",
  "significance","confidence","confidence_reason"]
PES_FIELDS = ["patent_id","title","assignee","app_no","file_date","pub_date","ipc","claim_type",
  "essential_elements","composition_ranges","organoid_scope","legal_status","claim_quote",
  "confidence","confidence_reason"]


def norm_name(s):
    """물질명 정규화 — 표기 차이를 흡수해 중복 등재를 탐지한다."""
    s = (s or "").lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[\s\-_·,/]+", "", s)
    s = re.sub(r"(전구체|계열|제품군|용액|분말|무수|과립|이온가교)$", "", s)
    return s


def check_extra():
    # (가) 추가 CSV 스키마 + 사유 없는 결측 표지
    for fn, fields, idk, label in (("suppliers.csv", SUP_FIELDS, "supplier_id", "공급"),
                                   ("patents_landscape.csv", PLS_FIELDS, "patent_id", "특허랜드스케이프"),
                                   ("patent_essentials.csv", PES_FIELDS, "patent_id", "특허독립항")):
        rows, _ = read_csv(fn)
        if not rows: continue
        check_schema(rows, fields, label, idk)
        for r in rows:
            for c in fields:
                v = (r.get(c) or "").strip().lower()
                if v in BAD_MISSING:
                    errors.append(f"[{label}] 사유 없는 결측 표지 '{r.get(c)}': {r.get(idk)} / {c}")
        info.append(f"[{label}] {len(rows)}행 스키마 검사 완료")

    inv, _ = read_csv("material_inventory.csv")
    ess, _ = read_csv("essential_items.csv")
    mtx, _ = read_csv("essential_matrix.csv")

    # (나) 물질명 정규화 중복 — 같은 층위 안의 제품(SKU) 변형은 정상이므로
    #     '동일 물질이 서로 다른 층위에 중복 등재된 경우'만 결함으로 본다(V 감사 반려-004의 실제 결함 유형).
    if inv:
        seen = {}
        for r in inv:
            key = norm_name(r.get("name_ko"))
            if len(key) < 3: continue
            seen.setdefault(key, []).append((r.get("layer"), r.get("material_id")))
        cross = {k: v for k, v in seen.items() if len({l for l, _ in v}) > 1}
        if cross:
            for k, v in list(cross.items())[:12]:
                errors.append(f"[G2] 동일 물질이 서로 다른 층위에 중복 등재: '{k}' → {sorted(v)}")
        else:
            info.append("[G2] 층위 간 동일 물질 중복 등재: 0건 (같은 층위 내 제품 변형은 정상으로 간주)")
        sku = {k: v for k, v in seen.items() if len(v) > 1 and len({l for l, _ in v}) == 1}
        if sku:
            info.append(f"[G2] 같은 층위 내 제품 변형 {len(sku)}군 — 등급 일관성은 아래 R-13 검사로 확인")

    # (다) R-10 — function_role이 매트릭스 비해당인데 essentiality가 '필수'
    if inv:
        pat = re.compile(r"매트릭스\s*(결합형\s*)?아님|매트릭스\s*성분이\s*아니|배지\s*(첨가형|성분)")
        bad = [r for r in inv if pat.search(r.get("function_role", ""))
               and (r.get("essentiality") or "").strip() == "필수"]
        for r in bad:
            errors.append(f"[R-10] 배지·비매트릭스 성분에 '필수' 부여: {r.get('material_id')} {r.get('name_ko')}")
        if not bad:
            info.append("[R-10] 배지 성분의 매트릭스 '필수' 오기재: 0건")
        # essentiality 값 영역
        # L9는 물질이 아니라 규격 항목이므로 '필수'의 뜻이 다르다. 값에 그 구분을 명시하도록 허용한다.
        OK_VALS = ("필수", "조건부", "선택",
                   "필수(출하 판정 시험)", "조건부(규격 항목)", "선택(규격 항목)")
        for r in inv:
            e = (r.get("essentiality") or "").strip()
            if e not in OK_VALS:
                errors.append(f"[M2] essentiality 값 오류: {r.get('material_id')} = '{e}'")
            if r.get("layer") == "L9" and e in ("필수", "조건부", "선택"):
                errors.append(f"[R-13] L9 규격 항목의 essentiality에 매트릭스 필수도 값을 사용: "
                              f"{r.get('material_id')} = '{e}' — 규격 항목임을 값에 명시해야 함")
        # 판정 기준 문서화 여부
        # 주의: 감사·레드팀·신뢰도 문서는 '기준이 없다'고 지적하는 과정에서 같은 낱말을 쓰므로
        #       검사 대상에서 제외한다. 기준은 조사 산출물(01_~07_) 안에 있어야 한다.
        SRC = [f for f in os.listdir(BASE)
               if re.match(r"0[1-7]_.*\.md$", f)]
        defined = False
        for fn in SRC:
            t = open(os.path.join(BASE, fn), encoding="utf-8", errors="replace").read()
            if "essentiality" in t and re.search(r"판정\s*기준|부여\s*기준", t):
                defined = True
                info.append(f"[R-13] essentiality 판정 기준 정의 위치: {fn}")
                break
        if defined:
            info.append("[R-13] essentiality 판정 기준이 문서에 정의됨")
        else:
            errors.append("[R-13] essentiality 3단계의 판정 기준이 어느 문서에도 정의되지 않음")

    # (라) 동일 물질 SKU 간 등급 역전
    if inv:
        grp = {}
        for r in inv:
            k = norm_name(r.get("name_ko"))
            if len(k) < 3: continue
            grp.setdefault(k, set()).add(re.sub(r"\(.*?\)", "", (r.get("essentiality") or "")).strip())
        split = {k: v for k, v in grp.items() if len(v) > 1}
        if split:
            for k, v in list(split.items())[:10]:
                errors.append(f"[R-13] 동일 물질의 제품 간 필수도 불일치: '{k}' → {sorted(v)}")
        else:
            info.append("[R-13] 동일 물질 제품 간 필수도 역전: 0건")

    # (마) tier ↔ 조직 매트릭스 교차 검사
    #     주의: 한 축(AX-n)에 여러 열이 걸리고(예: "AX-1 라미닌", "AX-1 RGD 대체"),
    #     매트릭스 셀은 축 전체의 요약 판정이라 항목 등급과 입도가 다르다.
    #     따라서 '최대 모순'(항목 E0인데 해당 조직의 그 축 열이 전부 E3)만 결함으로 본다.
    if ess and mtx:
        col0 = list(mtx[0].keys())[0]
        bad = []
        for r in ess:
            if (r.get("tier") or "").strip() != "E0":
                continue
            scope = r.get("tissue_scope", "")
            if "전체" in scope:
                continue
            axes = re.findall(r"AX-\d", r.get("axis", ""))
            for row in mtx:
                tkey = row.get(col0, "").split("(")[0].strip()
                if not tkey or tkey not in scope:
                    continue
                for ax in axes:
                    cells = [(c, (v or "").strip()[:2]) for c, v in row.items()
                             if c != col0 and c.startswith(ax)]
                    if cells and all(v == "E3" for _, v in cells):
                        bad.append(f"{tkey}/{ax}: 항목 {r.get('essential_id')} E0 ↔ 매트릭스 전 열 E3")
        bad = sorted(set(bad))
        for m in bad[:10]:
            errors.append(f"[G4] 항목 등급과 조직 매트릭스가 최대 모순: {m}")
        if not bad:
            info.append("[G4] tier ↔ 조직 매트릭스 교차 검사: 최대 모순(E0 ↔ 전 열 E3) 0건")

    # (바) 초록 전용 근거로 E0·E1 부여
    if ess:
        weak = [r for r in ess if r.get("tier") in ("E0", "E1")
                and re.search(r"본문\s*미확인|초록\s*범위", r.get("experiment_summary", ""))
                and (r.get("confidence") or "").strip() == "하"]
        for r in weak:
            errors.append(f"[R-13] 초록 전용·신뢰도 하 근거로 {r.get('tier')} 부여: {r.get('essential_id')}")
        if not weak:
            info.append("[R-13] 초록 전용·신뢰도 하 근거의 E0·E1: 0건")






# ─────────── 3차 감사 반영: 산문·헤더까지 훑는 교차 검사 ───────────
DOC_CSV = [("03_materials_bio.md", "inv_bio.csv"), ("04_materials_chem.md", "inv_chem.csv"),
           ("05_specs_regulatory.md", "inv_spec.csv"), ("06_supply.md", "suppliers.csv"),
           ("07_patents.md", "patents_landscape.csv"), ("11_essential_materials.md", "essential_items.csv"),
           ("12_patent_essentials.md", "patent_essentials.csv")]

# 배지·비매트릭스 성분을 식별하는 표현 (R-10)
MEDIUM_PAT = re.compile(r"매트릭스\s*(결합형\s*)?아님|매트릭스\s*성분이\s*아니|"
                        r"배지\s*(첨가형|성분|조성)|medium supplement")


def check_prose():
    """산문·헤더가 데이터와 어긋나는 유형을 잡는다. 2·3차 감사에서 반복 지적된 실패 유형이다."""

    # T-a. 헤더 items_count ↔ 대응 CSV 행수
    for md, cs in DOC_CSV:
        pm, pc = os.path.join(BASE, md), os.path.join(BASE, cs)
        if not (os.path.exists(pm) and os.path.exists(pc)):
            continue
        t = open(pm, encoding="utf-8", errors="replace").read()
        m = re.search(r"^items_count:\s*(\d+)", t, re.M)
        n = len(list(csv.DictReader(open(pc, encoding="utf-8-sig"))))
        if not m:
            errors.append(f"[§7] {md} 헤더에 items_count 없음")
        elif int(m.group(1)) != n:
            errors.append(f"[G5] {md} 헤더 items_count={m.group(1)} ≠ {cs} 행수 {n}")
    info.append("[G5] 헤더 items_count ↔ CSV 행수 대조 완료")

    # T-b. 산문의 '옛 총계' 잔존 — 각 문서가 자기 CSV 행수가 아닌 총계를 말하는지
    for md, cs in DOC_CSV:
        pm, pc = os.path.join(BASE, md), os.path.join(BASE, cs)
        if not (os.path.exists(pm) and os.path.exists(pc)):
            continue
        n = len(list(csv.DictReader(open(pc, encoding="utf-8-sig"))))
        t = open(pm, encoding="utf-8", errors="replace").read()
        for mm in re.finditer(r"(등재\s*(물질|항목|건수)[^\n]{0,30}?|총\s*)\*{0,2}(\d{2,4})\*{0,2}\s*건", t):
            v = int(mm.group(3))
            if v != n and v > 9:
                line = t[:mm.start()].count("\n") + 1
                errors.append(f"[G5] {md}:{line} 산문 총계 {v}건 ≠ {cs} 행수 {n}")
        # 'N건 중' 형태의 모수 — 전체 총계이거나 그 문서의 층위·부분집합 실측과 일치해야 한다.
        # 어긋나면 FAIL. (WARN으로 두었더니 실재 결함이 PASS를 통과했다 — V 4차 감사 지적)
        subset = set()
        rows_ = list(csv.DictReader(open(pc, encoding="utf-8-sig")))
        if rows_:
            subset |= set(collections.Counter(r.get("layer", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("tier", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("category", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("essentiality", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("confidence", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("grade", "") for r in rows_).values())
            subset |= set(collections.Counter(r.get("claim_checked", "") for r in rows_).values())
            # 품번·공급사·가격 확보 건수 같은 실무 부분집합
            for col, pat in (("catalog_no", r"^(맞춤합성|확보 실패|미확인|해당없음)"),
                             ("supplier", r"^(확보 실패|미확인|해당없음)"),
                             ("price", r"(미표시|미확인|확인 실패|차단|해당없음)")):
                if rows_ and col in rows_[0]:
                    subset.add(sum(1 for r in rows_ if (r.get(col) or "").strip()
                                   and not re.search(pat, (r.get(col) or "").strip())))
        ok_vals = {n} | {v for v in subset if v}
        # 다른 데이터셋(예: 특허 검색 원자료 726건, 청구항 원문 104건)을 가리키는 문장이 있으므로,
        # '이 문서의 자기 인벤토리'를 가리키는 문맥에서만 발화한다.
        SELF_CTX = re.compile(r"등재|본 문서|이 문서|인벤토리|L[1-9]\b|"
                              + re.escape(cs.replace(".csv", "")))
        for mm in re.finditer(r"\*{0,2}\s*(\d{2,4})\s*\*{0,2}\s*건\s*\*{0,2}\s*중", t):
            v = int(mm.group(1))
            if v <= 9 or v in ok_vals:
                continue
            ls = t.rfind("\n", 0, mm.start()) + 1
            le = t.find("\n", mm.end())
            sent = t[ls:le if le > 0 else len(t)]
            if not SELF_CTX.search(sent):
                continue          # 다른 데이터셋 참조로 간주
            line = t[:mm.start()].count("\n") + 1
            errors.append(f"[G5] {md}:{line} 모수 '{v}건 중'이 {cs}의 총계({n})와도 "
                          f"어떤 부분집합 실측과도 일치하지 않음")
    info.append("[G5] 산문 총계 ↔ CSV 행수 대조 완료")

    # T-c. 본문이 주장하는 매트릭스 셀 등급 ↔ 실제 셀 값
    mtx, _ = read_csv("essential_matrix.csv")
    if mtx:
        present = set()
        for row in mtx:
            for k, v in row.items():
                vv = (v or "").strip()[:2]
                if vv in ("E0", "E1", "E2", "E3"):
                    present.add(vv)
        for md, _cs in DOC_CSV:
            pm = os.path.join(BASE, md)
            if not os.path.exists(pm): continue
            t = open(pm, encoding="utf-8", errors="replace").read()
            for mm in re.finditer(r"(E[0-3])[^\n]{0,24}(으로|로)\s*표기했다|"
                                  r"매트릭스[^\n]{0,60}?(E[0-3])[^\n]{0,12}(으로|로)\s*(표기|기재)", t):
                g = mm.group(1) or mm.group(3)
                if g and g not in present:
                    line = t[:mm.start()].count("\n") + 1
                    errors.append(f"[G4] {md}:{line} 본문이 매트릭스 {g} 셀을 근거로 드나 "
                                  f"실제 매트릭스에 {g} 셀은 0개")
        info.append(f"[G4] 본문의 매트릭스 셀 인용 대조 완료 (실재 등급: {sorted(present)})")

    # T-d. 배지·비매트릭스 성분의 essentiality 는 '선택'이어야 한다 (R-10 정의역 전수)
    inv, _ = read_csv("material_inventory.csv")
    if inv:
        bad = [r for r in inv
               if MEDIUM_PAT.search(r.get("function_role", ""))
               and re.sub(r"\(.*?\)", "", r.get("essentiality", "")).strip() != "선택"]
        for r in bad:
            errors.append(f"[R-10] 배지·비매트릭스 성분의 필수도가 '선택'이 아님: "
                          f"{r.get('material_id')} {r.get('name_ko')} = '{r.get('essentiality')}'")
        if not bad:
            info.append("[R-10] 배지·비매트릭스 성분 필수도 전수 검사: 위반 0건")

    # T-e. 인용 DOI ↔ 근거 대장 등재
    led = os.path.join(BASE, "evidence_ledger.md")
    if os.path.exists(led):
        lt = open(led, encoding="utf-8", errors="replace").read()
        known = set(x.lower() for x in re.findall(r"10\.\d{4,5}/[A-Za-z0-9./_()<>-]+", lt))
        miss = collections.Counter()
        for fn in os.listdir(BASE):
            if not fn.endswith((".md", ".csv", ".html")) or fn in ("evidence_ledger.md", "gaps.md"):
                continue
            t = open(os.path.join(BASE, fn), encoding="utf-8", errors="replace").read()
            if fn.endswith(".html"):
                t = re.sub(r"<[^>]+>", " ", t)          # 태그가 식별자에 섞이지 않도록
            for d in re.findall(r"10\.\d{4,5}/[A-Za-z0-9./_()-]+", t):
                d = d.lower().rstrip(").,;:]").rstrip(".")
                if len(d) > 8 and d not in known:
                    miss[d] += 1
        if miss:
            for d, c in list(miss.most_common())[:8]:
                errors.append(f"[R-04] 근거 대장 미등재 식별자: {d} ({c}회) — "
                              f"대장에 등재하거나 비(非)PubMed 출처임을 대장에 명기할 것")
        info.append(f"[R-04] 인용 DOI ↔ 근거 대장 대조 완료 (미등재 {len(miss)}종)")


def check_grade_mapping():
    """인벤토리 essentiality ↔ M3 tier 매핑 검사 (`03_`의 기준표를 데이터 전체에 적용).
    기준표: E0 → 필수 / E1 → 필수·조건부 / E2 → 조건부 / E3 → 선택."""
    inv, _ = read_csv("material_inventory.csv")
    ess, _ = read_csv("essential_items.csv")
    if not (inv and ess):
        return
    order = {"E0": 0, "E1": 1, "E2": 2, "E3": 3}
    best = {}
    for r in ess:
        keys = {norm_name(r.get("name_ko")), norm_name(r.get("name_en"))}
        for syn in re.split(r"[;,/|]", r.get("synonyms", "") or ""):
            keys.add(norm_name(syn))
        for k in keys:
            if len(k) < 3:
                continue
            t = (r.get("tier") or "").strip()
            if t in order and (k not in best or order[t] < order[best[k][0]]):
                best[k] = (t, r.get("essential_id"))

    def lookup(row):
        """인벤토리 행 ↔ M3 항목 결합. 정확 일치 → 포함관계 순으로 찾는다."""
        cand = {norm_name(row.get("name_ko")), norm_name(row.get("name_en"))}
        for syn in re.split(r"[;,/|]", row.get("synonyms", "") or ""):
            cand.add(norm_name(syn))
        cand = {c for c in cand if len(c) >= 3}
        for c in cand:
            if c in best:
                return best[c]
        # 포함관계 — 제품 표기가 더 길거나(재조합 인간 라미닌511) 더 짧은(라미닌) 경우.
        # 단, 짧은 이름이 긴 합성어의 '가운데'에 박힌 경우는 결합하지 않는다.
        # 'REDV 피브로넥틴 CS5 펩타이드'는 짧은 모티프이지 '전장 피브로넥틴'이 아니다 —
        # 그런 결합을 허용하면 서로 다른 물질을 같은 등급 규칙에 묶게 된다.
        def affix(a, b):
            lo, hi = (a, b) if len(a) <= len(b) else (b, a)
            if len(lo) < 4 or len(lo) / len(hi) < 0.6:
                return False
            return hi.startswith(lo) or hi.endswith(lo)

        for c in cand:
            if len(c) < 4:
                continue
            hits = {v for k, v in best.items() if len(k) >= 4 and affix(k, c)}
            if len(hits) == 1:
                return next(iter(hits))
        return None
    EXPECT = {"E0": {"필수"}, "E1": {"필수", "조건부"}, "E2": {"조건부"}, "E3": {"선택"}}
    bad = []
    matched = 0
    for r in inv:
        if (r.get("layer") or "") == "L9":       # 규격 항목은 다른 축
            continue
        hit = lookup(r)
        if not hit:
            continue
        matched += 1
        t, eid = hit
        e = re.sub(r"\(.*?\)", "", r.get("essentiality", "")).strip()
        if e and e not in EXPECT[t]:
            bad.append(f"{r.get('material_id')} {r.get('name_ko')}: 인벤토리 '{e}' ↔ "
                       f"{eid} {t} (기대 {'/'.join(sorted(EXPECT[t]))})")

    # ── 선언 매핑 검사 ──────────────────────────────────────────────
    # 이름 대조는 제품명(인벤토리)과 기능명(M3)이 달라 정의역이 좁다.
    # 그래서 행이 `confidence_reason`에 **스스로 인용한** M3 항목 ID를 읽어
    # ① 그 ID가 실재하는지 ② 인용한 등급이 실제 등급과 같은지
    # ③ 그 등급과 essentiality가 기준표에 맞는지를 검사한다. 정밀도가 높다.
    tier_of = {r.get("essential_id"): (r.get("tier") or "").strip() for r in ess}
    decl = miscite = 0
    for r in inv:
        reason = r.get("confidence_reason", "")
        for m in re.finditer(r"(N-\d{3})\s*\(([^)]*)\)?[^.]{0,40}?(E[0-3])", reason):
            eid, _nm, cited = m.group(1), m.group(2), m.group(3)
            decl += 1
            actual = tier_of.get(eid)
            if actual is None:
                errors.append(f"[G5] {r.get('material_id')} 사유가 실재하지 않는 M3 항목을 인용: {eid}")
                miscite += 1
                continue
            if actual != cited:
                errors.append(f"[G5] {r.get('material_id')} 사유의 인용 등급 불일치: "
                              f"{eid}를 {cited}로 적었으나 실제 {actual}")
                miscite += 1
                continue
            e = re.sub(r"\(.*?\)", "", r.get("essentiality", "")).strip()
            if (r.get("layer") or "") != "L9" and e and e not in EXPECT[actual]:
                errors.append(f"[R-13] {r.get('material_id')} 선언 매핑 위반: "
                              f"'{e}' ↔ {eid} {actual} (기대 {'/'.join(sorted(EXPECT[actual]))})")
    info.append(f"[G5] 선언 매핑 검사: {decl}쌍 대조, 오인용 {miscite}건")

    for b in bad[:12]:
        errors.append(f"[R-13] essentiality ↔ M3 등급 매핑 위반: {b}")
    if not bad:
        info.append(f"[R-13] essentiality ↔ M3 등급 매핑: M3 키 {len(best)}종, 결합된 인벤토리 {matched}행, 위반 0건")


def check_evidence_count():
    """각 .md 헤더의 evidence_count.papers ↔ 그 문서가 실제로 인용한 고유 식별자 수.
    본문만 고치고 헤더를 두는 실패 유형을 막는다(V 5차 감사 지적)."""
    DOI_RE2 = re.compile(r"10\.\d{4,5}/[A-Za-z0-9./_()<>-]+")
    for fn in sorted(os.listdir(BASE)):
        if not re.match(r"(0[1-9]|1[0-2])_.*\.md$", fn):
            continue
        t = open(os.path.join(BASE, fn), encoding="utf-8", errors="replace").read()
        m = re.search(r"evidence_count:\s*\{papers:\s*(\d+)", t)
        if not m:
            errors.append(f"[§7] {fn} 헤더에 evidence_count.papers 없음")
            continue
        hdr = int(m.group(1))
        got = {d.lower().rstrip(").,;:]").rstrip(".") for d in DOI_RE2.findall(t)}
        got = {d for d in got if len(d) > 8}
        if hdr != len(got):
            errors.append(f"[G5] {fn} 헤더 evidence_count.papers={hdr} ≠ "
                          f"본문 고유 DOI {len(got)}건")
    info.append("[G5] 헤더 evidence_count ↔ 본문 인용 식별자 대조 완료")


if __name__ == "__main__":
    sys.exit(main())
