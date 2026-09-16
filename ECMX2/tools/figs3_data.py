# -*- coding: utf-8 -*-
"""ECMX-003 데이터 도판 — CSV에서만 값을 받는다.

여기 함수는 어느 것도 수치를 자기 안에 갖고 있지 않다. 인자로 들어온 행이 비어 있으면
빈 축을 예쁘게 그리는 대신 '정량 근거 없음'이라고 적는다. 그것이 R-04의 뜻이다.
"""
import re, math
from figlib2 import *

NEC = ("필수", "조건부", "선택", "미사용")
LAYERS = [("L1", "구조 단백질"), ("L2", "다당 · GAG"), ("L3", "프로테오글리칸"),
          ("L4", "성장인자"), ("L5", "펩타이드 모티프"), ("L6", "가교제"),
          ("L7", "합성 백본"), ("L8", "완충 · 이온"), ("L9", "품질 규격")]


# ── 파서 ────────────────────────────────────────────────────────
_NUM = r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?"

def nums(s):
    return [float(x) for x in re.findall(_NUM, str(s or ""))]


TO_NG_ML = {"ng/ml": 1.0, "ng/㎖": 1.0, "µg/ml": 1e3, "ug/ml": 1e3, "μg/ml": 1e3,
            "mg/ml": 1e6, "g/l": 1e6, "pg/ml": 1e-3, "ng/l": 1e-6}

def to_ng_ml(s):
    """농도 문자열 → (low, high) ng/mL. 단위를 못 읽으면 None."""
    t = str(s or "").replace(" ", "").lower()
    for u, k in sorted(TO_NG_ML.items(), key=lambda x: -len(x[0])):
        if u in t:
            v = nums(t.split(u)[0][-24:])
            if not v:
                return None
            return (min(v[-2:]) * k, max(v[-2:]) * k) if len(v) >= 2 else (v[-1] * k, v[-1] * k)
    return None


def to_pa(s):
    """탄성률 문자열 → Pa. kPa/MPa 인식."""
    t = str(s or "").replace(" ", "").lower()
    for u, k in (("mpa", 1e6), ("kpa", 1e3), ("pa", 1.0)):
        if u in t:
            v = nums(t.split(u)[0][-16:])
            if v:
                return v[-1] * k
    return None


def to_mg_ml(s):
    t = str(s or "").replace(" ", "").lower()
    for u, k in (("mg/ml", 1.0), ("g/l", 1.0), ("%w/v", 10.0), ("mg/cm3", 1.0)):
        if u in t:
            v = nums(t.split(u)[0][-16:])
            if v:
                return v[-1] * k
    return None


# ── 그림 ────────────────────────────────────────────────────────
def fig_layer_stack(rows, title_txt="층위별 소요 항목 수와 필수도",
                    sub="콜라겐 I/III 골격을 전제로 한 판정"):
    """층위 L1~L9 × 필수도 누적 막대."""
    W = 900
    H = 130 + len(LAYERS) * 40
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, title_txt, sub))

    cnt = {L: {n: 0 for n in NEC} for L, _ in LAYERS}
    for r in rows:
        L = (r.get("layer") or "").strip().upper()[:2]
        n = (r.get("necessity") or "").strip()
        if L in cnt and n in cnt[L]:
            cnt[L][n] += 1
    mx = max([sum(v.values()) for v in cnt.values()] + [1])

    x0, bw = 220, 560
    y = 68
    for L, nm in LAYERS:
        tot = sum(cnt[L].values())
        b.append(txt(24, y + 17, L, 12, C["mx"], weight="700", mono=True))
        b.append(txt(54, y + 17, nm, 12, C["ink"]))
        if tot == 0:
            b.append(nodata(x0, y + 2, 240, 22, "이 층위에 해당 항목 없음"))
        else:
            cx = x0
            for n in NEC:
                c = cnt[L][n]
                if not c:
                    continue
                w = c / mx * bw
                b.append(rect(cx, y + 2, w, 24, N_FILL[n], rx=3, stroke=C["line2"], sw=.6))
                if w > 20:
                    b.append(txt(cx + w / 2, y + 19, str(c), 11,
                                 N_TXT[n] if n != "선택" else C["ink"], "middle", "600", mono=True))
                cx += w + 2
            b.append(txt(cx + 8, y + 19, f"합 {tot}", 10.5, C["faint"], mono=True))
        y += 40

    b.append(legend(24, H - 22, [(N_FILL[n], n) for n in NEC[:3]], horiz=True, step=120))
    b.append(txt(24, H - 44, f"막대 길이는 항목 수에 비례 · 최대 {mx}개", 10, C["faint"]))
    return svg(W, H, "".join(b), title_txt)


# 값 칸에서 수치를 뽑을 때 걸려 넘어지는 것들:
#   "438 ± 87 (mean ± SEM, n=6)"  → 마지막 숫자를 집으면 n=6의 6을 집는다
#   "914 (무가교) → 1690 (UV 가교)" → 전후 두 값이 한 칸에 들어 있다
#   unit "mPa·s"                   → 'Pa'가 들어 있지만 점도이지 탄성률이 아니다
# 그래서 파서를 느슨하게 두지 않는다. 애매하면 그리지 않는 쪽을 택한다.
_ADDITIVE = re.compile(r"나노섬유|PCL|BGN|생체활성유리|나노입자|복합|블렌드|알지네이트|"
                       r"PEG|dECM|하이브리드|막\b|스캐폴드|피브린")
# '무가교'에도 '가교'가 들어 있다. 부정 접두사를 빼지 않으면 대조군이 처리군으로 분류된다.
_XLINK = re.compile(r"(?<!무)(?<!비)가교|crosslink|글루타르|mTG|트랜스글루타|제니핀|EDC|UV|리보플라빈")


def _unit_scale(unit):
    """단위 문자열 앞머리만 본다. 'kPa (Young's modulus, E)' → 1e3, 'mPa·s' → None."""
    u = str(unit or "").strip().lower()
    if re.match(r"^m?pa\s*[·.*]\s*s", u):
        return None          # 점도
    m = re.match(r"^(k|m)?pa\b", u)
    if not m:
        return None
    return {"k": 1e3, "m": 1e6, None: 1.0}[m.group(1)]


def _lead_num(s):
    """문자열 맨 앞의 수치. '438 ± 87 (…n=6)' → 438.0"""
    m = re.match(r"\s*~?\s*약?\s*(" + _NUM + ")", str(s or ""))
    return float(m.group(1)) if m else None


def _pre_post(s):
    """'914 (무가교) → 1690 (UV 가교)' → (914.0, 1690.0). 화살표가 없으면 (값, None)."""
    s = str(s or "")
    if "→" in s or "->" in s:
        a, b = re.split(r"→|->", s, 1)
        return _lead_num(a), _lead_num(b)
    return _lead_num(s), None


def _is_E(name, method):
    blob = (name or "") + " " + (method or "")
    return bool(re.search(r"영률|young|압축|compress|인장|tensile|AFM", blob, re.I))


def fig_conc_modulus(params):
    """콜라겐 농도 ↔ 겔 강성. 순수 무가교 겔만 점으로 찍고, 가교 효과는 화살표로 얹는다.

    복합재(나노섬유막·나노입자 첨가 등)는 제외한다. 그 값은 콜라겐 겔의 강성이 아니라
    복합체의 강성이어서, 같은 축에 올리면 농도-강성 관계를 잘못 읽게 만든다.
    """
    W, H = 900, 452
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "콜라겐 농도와 겔 강성",
                   "순수 콜라겐 겔만 표시 · G′(진동 유변계)과 E(압축·AFM)는 서로 환산되지 않는다"))

    pts, arrows, dropped = [], [], 0
    for r in params:
        nm, cond = r.get("param_name") or "", r.get("condition") or ""
        k = _unit_scale(r.get("unit"))
        if k is None:
            continue
        conc = to_mg_ml(cond)
        if not conc:
            continue
        zero_ctrl = re.search(r"0\s*%\s*(?:\(w/v\))?\s*(?:첨가|added)?", cond)
        if (_ADDITIVE.search(cond) or _ADDITIVE.search(nm)) and not zero_ctrl:
            dropped += 1
            continue
        pre, post = _pre_post(r.get("value"))
        if pre is None:
            continue
        kind = "E" if _is_E(nm, r.get("method")) else "G"
        xl = bool(_XLINK.search(nm) or _XLINK.search(cond))
        if xl and post is not None:
            arrows.append((conc, pre * k, post * k, kind))
        elif xl:
            arrows.append((conc, None, pre * k, kind))
        else:
            pts.append((conc, pre * k, kind))

    px0, py0, pw, ph = 86, 66, 700, 286
    b.append(rect(px0, py0, pw, ph, "#FCFDFD", rx=8, stroke=C["line"]))
    if not pts and not arrows:
        b.append(nodata(px0 + 40, py0 + ph / 2 - 24, pw - 80, 48,
                        "농도–강성 짝이 확보되지 않음"))
        return svg(W, H, "".join(b), "콜라겐 농도와 겔 강성")

    allv = [v for _, v, _ in pts] + [v for _, a, z, _ in arrows for v in (a, z) if v]
    allc = [x for x, _, _ in pts] + [x for x, _, _, _ in arrows]
    xlo, xhi = max(min(allc) * .7, 1e-2), max(allc) * 1.5
    ylo, yhi = max(min(allv) * .45, 1e-1), max(allv) * 2.4
    X = logscale(xlo, xhi, px0 + 34, pw - 70)

    def Y(v):
        l0, l1 = math.log10(ylo), math.log10(yhi)
        return py0 + ph - 34 - (math.log10(v) - l0) / (l1 - l0) * (ph - 66)

    for d in logticks(ylo, yhi, dense=False):
        b.append(line(px0 + 14, Y(d), px0 + pw - 14, Y(d), C["line"], 1, dash="3 4"))
        b.append(txt(px0 + 10, Y(d) + 4, fmt_si(d, "Pa"), 9.5, C["faint"], "end", mono=True))
    b.append(axis_x(px0 + 20, px0 + pw - 14, py0 + ph - 30, logticks(xlo, xhi),
                    lambda v: f"{v:g}", X))
    b.append(txt(px0 + pw / 2, py0 + ph + 2, "콜라겐 농도 (mg/mL, 로그)", 10.5, C["mut"], "middle"))
    b.append(txt(px0 + 20, py0 + 20, "↑ 탄성률 (Pa, 로그)", 10.5, C["mut"]))

    for conc, a, z, kind in arrows:
        col = C["cnd"]
        if a:
            b.append(line(X(conc), Y(a), X(conc), Y(z), col, 1.6, marker="ar", op=.75))
            b.append(circ(X(conc), Y(a), 3.2, "#FFFFFF", col, 1.4))
        b.append(path(f"M{X(conc)-4.6} {Y(z)} L{X(conc)} {Y(z)-4.6} "
                      f"L{X(conc)+4.6} {Y(z)} L{X(conc)} {Y(z)+4.6} Z", col, "#FFFFFF", 1.1))
    for conc, v, kind in pts:
        col = C["mx"] if kind == "G" else C["opt"]
        b.append(circ(X(conc), Y(v), 5.2, col, "#FFFFFF", 1.3, op=.92))

    b.append(legend(px0 + pw - 246, py0 + 30, [
        (C["mx"], f"무가교 순수 콜라겐 겔 G′ ({len(pts)}점)"),
        (C["cnd"], f"가교 후 G′ — 화살표는 가교 전→후 ({len(arrows)}건)"),
    ], size=10.2))
    note = (f"collagen_params.csv에서 <b>순수 콜라겐 겔</b>의 농도와 탄성률이 한 행에 함께 기재된 "
            f"{len(pts) + len(arrows)}건만 표시했다.")
    b.append(txt(20, H - 40, f"순수 콜라겐 겔의 농도–탄성률 짝 {len(pts)+len(arrows)}건만 표시. "
                             f"복합재(나노입자·나노섬유막 등) {dropped}건은 제외 — "
                             "그 값은 콜라겐 겔이 아니라 복합체의 강성이다.", 10.4, C["faint"]))
    b.append(txt(20, H - 22, "측정 온도·시간·유변계 조건이 행마다 다르므로 추세선을 긋지 않는다.",
                 10.4, C["faint"]))
    return svg(W, H, "".join(b), "콜라겐 농도와 겔 강성")


def fig_crosslinkers(rows):
    """L6 가교제 — 세포를 넣은 채 굳힐 수 있는가가 첫 번째 질문이다."""
    L6 = [r for r in rows if (r.get("layer") or "").strip().upper() == "L6"]
    W = 900
    H = 112 + max(len(L6), 1) * 34
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "가교 수단 비교 — 세포 존재 하 가교 가능 여부",
                   "강성을 올리는 모든 수단이 세포와 함께 쓰일 수 있는 것은 아니다"))
    if not L6:
        b.append(nodata(40, 70, W - 80, 44, "L6 행이 확보되지 않음"))
        return svg(W, H, "".join(b), "가교 수단 비교")

    b.append(txt(24, 66, "가교 수단", 10.5, C["faint"], weight="600"))
    b.append(txt(330, 66, "필수도", 10.5, C["faint"], weight="600"))
    b.append(txt(410, 66, "정량 조건", 10.5, C["faint"], weight="600"))
    b.append(line(20, 72, W - 20, 72, C["line2"], 1))

    y = 78
    for r in L6:
        nm = (r.get("name_ko") or r.get("name_en") or "").strip()
        nec_ = (r.get("necessity") or "").strip()
        qs = (r.get("quant_spec") or "").strip()
        alive = re.search(r"세포\s*(존재|공존|포함|동시|봉입)|in\s*situ|세포와\s*함께", 
                          " ".join([r.get("role_in_collagen_system") or "",
                                    r.get("necessity_basis") or "", qs]))
        b.append(rect(20, y, W - 40, 30, "#FFFFFF" if y // 30 % 2 else "#FAFCFC",
                      rx=5, stroke=C["line"]))
        b.append(txt(30, y + 20, nm[:22], 11.8, C["ink"], weight="600"))
        b.append(rect(330, y + 7, 52, 17, N_SOLID.get(nec_, C["opt"]), rx=8.5))
        b.append(txt(356, y + 19, nec_ or "—", 10, N_TXT.get(nec_, "#fff"), "middle", "600"))
        b.append(txt(410, y + 20, (qs or "정량 근거 없음")[:52], 10.4,
                     C["mut"] if qs and qs != "정량 근거 없음" else C["faint"],
                     mono=bool(qs and qs != "정량 근거 없음")))
        b.append(circ(W - 42, y + 15, 5, C["ok"] if alive else C["bad"]))
        y += 34
    b.append(txt(W - 60, 66, "세포 공존", 10.5, C["faint"], "end", weight="600"))
    b.append(circ(26, H - 24, 4.4, C["ok"]))
    b.append(txt(36, H - 20, "BOM 근거란에 세포 존재 하 가교가 명시된 건", 10.2, C["mut"]))
    b.append(circ(310, H - 24, 4.4, C["bad"]))
    b.append(txt(320, H - 20, "명시되지 않음 — 세포를 넣기 전 처리로 보아야 한다", 10.2, C["mut"]))
    return svg(W, H, "".join(b), "가교 수단 비교")


def fig_med_categories(rows):
    """배지 범주별 성분 수 — 직접 조제가 실제로 몇 개의 구매 항목인지."""
    cats = []
    for r in rows:
        c = (r.get("category") or "").strip()
        if c and c not in cats:
            cats.append(c)
    W = 900
    H = 120 + max(len(cats), 1) * 38
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "배지 범주별 구매 항목 수", "직접 조제란 이만큼의 품번을 관리한다는 뜻이다"))
    if not cats:
        b.append(nodata(40, 70, W - 80, 44, "medium_bom.csv가 비어 있음"))
        return svg(W, H, "".join(b), "배지 범주별 구매 항목 수")

    cnt = {c: {n: 0 for n in NEC} for c in cats}
    for r in rows:
        c = (r.get("category") or "").strip()
        n = (r.get("necessity") or "").strip()
        if c in cnt and n in cnt[c]:
            cnt[c][n] += 1
    mx = max([sum(v.values()) for v in cnt.values()] + [1])
    x0, bw = 210, 560
    y = 66
    for c in cats:
        tot = sum(cnt[c].values())
        b.append(txt(24, y + 18, c[:14], 12, C["ink"]))
        cx = x0
        for n in NEC:
            k = cnt[c][n]
            if not k:
                continue
            w = k / mx * bw
            b.append(rect(cx, y + 3, w, 24, N_FILL[n], rx=3, stroke=C["line2"], sw=.6))
            if w > 20:
                b.append(txt(cx + w / 2, y + 20, str(k), 11,
                             N_TXT[n] if n != "선택" else C["ink"], "middle", "600", mono=True))
            cx += w + 2
        b.append(txt(cx + 8, y + 20, f"합 {tot}", 10.5, C["faint"], mono=True))
        y += 38
    b.append(legend(24, H - 22, [(N_FILL[n], n) for n in NEC[:3]], horiz=True, step=120))
    return svg(W, H, "".join(b), "배지 범주별 구매 항목 수")


def fig_gf_ranges(rows, cats=("니치성장인자", "조직특이성장인자")):
    """성장인자 사용 농도 구간 — 로그축. 단위가 다른 것을 억지로 한 줄에 올리지 않는다."""
    sel = []
    for r in rows:
        if (r.get("category") or "").strip() not in cats:
            continue
        rng = to_ng_ml(r.get("conc_range")) or to_ng_ml(r.get("conc_typical"))
        typ = to_ng_ml(r.get("conc_typical"))
        if rng:
            sel.append((r.get("name_ko") or r.get("name_en") or "", rng,
                        typ[0] if typ else None, (r.get("necessity") or "").strip()))
    sel.sort(key=lambda s: s[1][0])
    W = 900
    H = 126 + max(len(sel), 1) * 27
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "성장인자 사용 농도 구간",
                   "문헌·특허에 기재된 범위를 ng/mL로 환산해 한 축에 올린 것"))
    if not sel:
        b.append(nodata(40, 70, W - 80, 44, "단위 환산이 가능한 농도 범위 행이 없음"))
        return svg(W, H, "".join(b), "성장인자 사용 농도 구간")

    lo = max(min(s[1][0] for s in sel) * .5, 1e-3)
    hi = max(s[1][1] for s in sel) * 2.0
    px0, pw = 236, 580
    X = logscale(lo, hi, px0, pw)
    top, y = 60, 76
    for d in logticks(lo, hi):
        b.append(line(X(d), top, X(d), 76 + len(sel) * 27 - 6, C["line"], 1, dash="3 4"))
        b.append(txt(X(d), top - 4, fmt_si(d) + " ng/mL", 9.3, C["faint"], "middle", mono=True))
    for nm, (a, z), t, nec_ in sel:
        col = N_SOLID.get(nec_, C["opt"])
        b.append(txt(226, y + 14, nm[:20], 11.2, C["ink"], "end"))
        xa, xz = X(a), X(max(z, a * 1.02))
        b.append(rect(xa, y + 5, max(xz - xa, 3), 15, col, rx=7.5, op=.32))
        b.append(line(xa, y + 12.5, xz, y + 12.5, col, 1.6))
        b.append(circ(xa, y + 12.5, 3.2, col)); b.append(circ(xz, y + 12.5, 3.2, col))
        if t:
            b.append(path(f"M{X(t)-4} {y+3} L{X(t)+4} {y+3} L{X(t)} {y+9} Z", col))
        b.append(txt(min(xz + 9, W - 24), y + 16,
                     (f"{fmt_si(a)}~{fmt_si(z)}" if z > a else fmt_si(a)), 9.4,
                     C["faint"], mono=True))
        y += 27
    b.append(legend(24, H - 22, [(N_SOLID[n], n) for n in NEC[:3]], horiz=True, step=110))
    b.append(txt(430, H - 22, "▼ = 대표 농도 · 가로 막대 = 기재된 범위", 10.2, C["faint"]))
    return svg(W, H, "".join(b), "성장인자 사용 농도 구간")


def fig_tissue_heatmap(matrix_rows):
    """조직 × 성분 필수도 격자. 색만으로 구분하지 않고 글자를 함께 찍는다."""
    if not matrix_rows:
        return svg(880, 140, rect(0, 0, 880, 140, C["bg"], rx=0)
                   + nodata(40, 48, 800, 48, "medium_matrix.csv가 비어 있음"),
                   "조직별 배지 조성")
    cols = [c for c in matrix_rows[0].keys() if c and c != "성분"]
    rows = matrix_rows
    cw, rh = 82, 30
    W = 306 + len(cols) * cw + 30
    H = 112 + len(rows) * rh + 44
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "조직별 배지 조성 — 무엇이 어디서 필수인가",
                   "같은 성분이라도 조직이 바뀌면 등급이 바뀐다"))
    x0, y0 = 306, 86
    for j, c in enumerate(cols):
        b.append(txt(x0 + j * cw + cw / 2, y0 - 10, c, 11.5, C["md"], "middle", "700"))
    for i, r in enumerate(rows):
        yy = y0 + i * rh
        b.append(txt(296, yy + 20, (r.get("성분") or "")[:26], 10.9, C["ink"], "end"))
        for j, c in enumerate(cols):
            v = (r.get(c) or "").strip()
            k = next((n for n in NEC if v.startswith(n)), None)
            xx = x0 + j * cw
            b.append(rect(xx + 1.5, yy + 2, cw - 3, rh - 5,
                          N_FILL[k] if k else "#FFFFFF", rx=4,
                          stroke=C["line"], sw=.8))
            if k:
                b.append(txt(xx + cw / 2, yy + 19, k, 9.8,
                             N_TXT[k] if k != "선택" else C["ink"], "middle", "600"))
            else:
                b.append(txt(xx + cw / 2, yy + 19, "—", 10, C["faint"], "middle"))
    b.append(legend(24, H - 20, [(N_FILL[n], n) for n in NEC], horiz=True, step=112))
    b.append(txt(24, H - 40, "괄호 안 농도·단서는 본문 표에 있다. 이 격자는 등급만 보여 준다.",
                 10.2, C["faint"]))
    return svg(W, H, "".join(b), "조직별 배지 조성 격자")


def fig_stage_switch(rows):
    """확장 배지 → 분화 배지. 무엇을 빼고 무엇을 넣는가."""
    exp, dif, both, pulse = [], [], [], []
    for r in rows:
        s = (r.get("stage") or "").strip()
        nm = (r.get("name_ko") or r.get("name_en") or "").strip()
        if not nm:
            continue
        if "계대" in s:
            pulse.append(nm)
        elif "확장" in s and "분화" in s:
            both.append(nm)
        elif "확장" in s:
            exp.append(nm)
        elif "분화" in s:
            dif.append(nm)
        elif "전" in s:
            both.append(nm)
    W, H = 900, 400
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 26, "확장 배지와 분화 배지 — 같은 배지가 아니다",
                   "줄기세포를 늘릴 때와 조직으로 굳힐 때 넣는 것이 다르다"))
    if not (exp or dif or both):
        b.append(nodata(40, 70, W - 80, 44, "stage 열이 채워진 행이 없음"))
        return svg(W, H, "".join(b), "확장 배지와 분화 배지")

    def col(x, w, ttl, sub, items, c, bgc):
        o = [rect(x, 62, w, 300, bgc, rx=10, stroke=c, sw=1.4)]
        o.append(txt(x + 16, 86, ttl, 13, c, weight="700"))
        o.append(txt(x + 16, 103, sub, 10, c, op=.8))
        yy = 124
        for nm in items[:12]:
            o.append(circ(x + 22, yy - 4, 2.6, c))
            o.append(txt(x + 32, yy, nm[:18], 10.8, C["ink"]))
            yy += 18
        if len(items) > 12:
            o.append(txt(x + 32, yy, f"외 {len(items)-12}개 — 본문 표 참조", 10, C["faint"]))
        if not items:
            o.append(nodata(x + 16, 124, w - 32, 36, "해당 행 없음"))
        return "".join(o)

    b.append(col(20, 250, "확장 (expansion)", "줄기세포를 늘린다", exp, C["md"], C["md_bg"]))
    b.append(col(325, 250, "두 단계 공통", "빼지 않는 바탕", both, C["mut"], "#F4F7F8"))
    b.append(col(630, 250, "분화 (differentiation)", "조직으로 굳힌다", dif, C["mx"], C["mx_bg"]))
    b.append(line(272, 212, 320, 212, C["mut"], 1.6, marker="ar"))
    b.append(line(578, 212, 626, 212, C["mut"], 1.6, marker="ar"))
    if pulse:
        b.append(rect(20, 372, W - 40, 22, C["cnd_bg"], rx=6, stroke=C["cnd"]))
        b.append(txt(32, 388, "계대 직후에만: " + " · ".join(pulse[:7])
                     + (f" 외 {len(pulse)-7}개" if len(pulse) > 7 else ""),
                     10.6, C["cnd"], weight="600"))
    return svg(W, H, "".join(b), "확장 배지와 분화 배지")
