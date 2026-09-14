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
import csv, os, re, sys, json

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
    r"금지\s*수치|인용하지|사실이\s*아니|것이\s*아니다|아니다|오류|반박|순환\s*파생|주의|배제|§4|"
    r"근거\s*없|정확히\s*말하면|삭제와|수용\s*경로|점진적|오해|잘못|해당하여|추적\s*가능한\s*1차")

DEFER = [r"이후\s*조사하겠", r"추가\s*확인이\s*필요", r"다음\s*단계에서\s*다루", r"추후\s*보완",
         r"향후\s*조사", r"TBD\b", r"to\s+be\s+determined"]

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

    print("=" * 72)
    print(f"ECMX validate.py — BASE={BASE}")
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


if __name__ == "__main__":
    sys.exit(main())
