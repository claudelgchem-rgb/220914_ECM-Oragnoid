# -*- coding: utf-8 -*-
"""ECMX-004 재료 축 도판.

이 보고서에만 있는 질문 하나를 그린다 — '세 재료 중 무엇을 쓰기로 하면 무엇을 더 사야 하는가.'
같은 층위라도 단일사슬만 쓸 때와 삼중나선을 섞을 때 소요가 달라지므로,
필수 항목 수를 재료 조합별로 세어 보는 것이 곧 구매 의사결정이 된다.
"""
import itertools, re
from figlib2 import *
from figs4_data import NEC, LAYERS

MATS = ("A", "B", "C")
MAT_LABEL = {"A": "I형 단일사슬", "B": "III형 단일사슬", "C": "III형 삼중나선"}
COMBOS = [("A",), ("B",), ("C",), ("A", "B"), ("A", "C"), ("B", "C"), ("A", "B", "C")]


def scope_set(r):
    """material_scope 문자열 → 집합. 읽지 못하면 전 조합으로 보지 않고 빈 집합으로 둔다."""
    s = (r.get("material_scope") or "").strip()
    if not s:
        return set()
    if "전 조합" in s or "전체" in s or "무관" in s:
        return set(MATS)
    return {m for m in MATS if re.search(rf"\b{m}\b", s)}


def applies(r, combo):
    """이 항목이 그 조합에서 필요한가 — scope가 조합과 겹치면 필요하다."""
    sc = scope_set(r)
    if not sc:
        return False
    return bool(sc & set(combo))


def fig_material_load(rows, nec="필수"):
    """그림. 어느 조합을 고르면 몇 개를 사야 하는가.

    재료 선택은 취향이 아니라 소요를 바꾸는 결정이다. 그 크기를 먼저 보여 준다.
    """
    W, H = 920, 380
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, f"재료 조합별 {nec} 항목 수",
                   "같은 층위 목록이라도 어느 재료를 쓰기로 하느냐에 따라 소요가 달라진다"))

    have_scope = [r for r in rows if scope_set(r)]
    if not have_scope:
        b.append(nodata(40, 70, W - 80, 48, "material_scope 열이 채워진 행이 없음"))
        return svg(W, H, "".join(b), "재료 조합별 소요")

    counts = []
    for combo in COMBOS:
        n = sum(1 for r in have_scope
                if (r.get("necessity") or "").strip() == nec and applies(r, combo))
        counts.append((combo, n))
    mx = max([n for _, n in counts] + [1])

    x0, bw = 252, 550
    y = 66
    for combo, n in counts:
        # 재료 칸
        for k, m in enumerate(MATS):
            on = m in combo
            cx = 24 + k * 26
            b.append(rect(cx, y + 3, 22, 22, C["mx"] if on else "#FFFFFF", rx=5,
                          stroke=C["mx"] if on else C["line2"], sw=1.1))
            b.append(txt(cx + 11, y + 19, m, 11, "#FFFFFF" if on else C["faint"],
                         "middle", "700", mono=True))
        lab = " + ".join(combo)
        b.append(txt(110, y + 19, lab, 12, C["ink"], weight="700", mono=True))
        b.append(txt(196, y + 19, f"({len(combo)}종)", 9.6, C["faint"]))
        w = n / mx * bw
        b.append(rect(x0, y + 5, bw, 18, "#FFFFFF", rx=5, stroke=C["line"], sw=.8))
        b.append(rect(x0, y + 5, w, 18, N_FILL[nec], rx=5))
        b.append(txt(x0 + bw + 14, y + 19, str(n), 12.5, C["mx"], "start", "700", mono=True))
        y += 38

    b.append(line(20, y + 4, W - 20, y + 4, C["line"], 1))
    b.append(txt(24, y + 26, "숫자는 그 조합에서 필수로 판정된 지지체 항목 수다. "
                             "재료를 더 넣으면 대체로 소요가 늘지만, 어떤 항목은 "
                             "재료를 바꿔야 비로소 빠진다.", 10.4, C["faint"]))
    b.append(txt(24, y + 44, "material_scope가 비어 있는 행은 세지 않았다 — "
                             f"전체 {len(rows)}행 중 {len(have_scope)}행만 집계.", 10.4, C["faint"]))
    return svg(W, max(H, y + 58), "".join(b), f"재료 조합별 {nec} 항목 수")


def fig_layer_material_grid(rows):
    """그림. 층위 × 재료 격자 — 어느 재료가 어느 층위에서 무엇을 요구하는가."""
    have = [r for r in rows if scope_set(r)]
    cw, rh = 150, 34
    W = 250 + len(MATS) * cw + 40
    H = 116 + len(LAYERS) * rh + 56
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "층위 × 재료 — 무엇을 어디에 요구하는가",
                   "칸의 숫자는 그 재료를 쓸 때 그 층위에서 필요한 항목 수(필수 / 조건부)"))
    if not have:
        b.append(nodata(40, 70, W - 80, 48, "material_scope 열이 채워진 행이 없음"))
        return svg(W, H, "".join(b), "층위 × 재료 격자")

    x0, y0 = 250, 92
    for j, m in enumerate(MATS):
        cx = x0 + j * cw + cw / 2
        b.append(txt(cx, y0 - 22, m, 13, C["mx"], "middle", "700", mono=True))
        b.append(txt(cx, y0 - 8, MAT_LABEL[m], 9.8, C["mut"], "middle"))
    for i, (L, nm) in enumerate(LAYERS):
        yy = y0 + i * rh
        b.append(txt(36, yy + 22, L, 11.5, C["mx"], weight="700", mono=True))
        b.append(txt(66, yy + 22, nm, 11, C["ink"]))
        for j, m in enumerate(MATS):
            sel = [r for r in have
                   if (r.get("layer") or "").strip().upper() == L and m in scope_set(r)]
            req = sum(1 for r in sel if (r.get("necessity") or "").strip() == "필수")
            cnd = sum(1 for r in sel if (r.get("necessity") or "").strip() == "조건부")
            xx = x0 + j * cw
            if not sel:
                tone, fill = "#FFFFFF", C["faint"]
            elif req:
                tone, fill = N_FILL["필수"], "#FFFFFF"
            elif cnd:
                tone, fill = N_FILL["조건부"], "#FFFFFF"
            else:
                tone, fill = N_FILL["선택"], C["ink"]
            b.append(rect(xx + 2, yy + 3, cw - 4, rh - 7, tone, rx=5,
                          stroke=C["line"], sw=.8))
            if not sel:
                b.append(txt(xx + cw / 2, yy + 23, "—", 11, C["faint"], "middle"))
            elif not req and not cnd:
                b.append(txt(xx + cw / 2, yy + 23, f"선택 {len(sel)}", 10.6, fill,
                             "middle", "600", mono=True))
            else:
                b.append(txt(xx + cw / 2 - 14, yy + 23, str(req), 13, fill,
                             "middle", "700", mono=True))
                b.append(txt(xx + cw / 2, yy + 23, "/", 10.5, fill, "middle", op=.7))
                b.append(txt(xx + cw / 2 + 16, yy + 23, str(cnd), 11.5, fill,
                             "middle", "600", mono=True, op=.85))
    yy = y0 + len(LAYERS) * rh
    b.append(legend(24, yy + 22, [(N_FILL["필수"], "필수 항목 있음"),
                                  (N_FILL["조건부"], "조건부만 있음"),
                                  (N_FILL["선택"], "선택만 있음"),
                                  ("#FFFFFF", "해당 항목 없음")], horiz=True, step=180))
    b.append(txt(24, yy + 44, "칸 표기는 필수 / 조건부 순이다. 한 항목이 여러 재료에 걸치면 "
                              "해당 재료 칸마다 세었다.", 10.3, C["faint"]))
    return svg(W, H, "".join(b), "층위 × 재료 격자")


def fig_tm(params, body_temp=37.0):
    """그림. 재조합 콜라겐의 융해온도 — 37 ℃ 선을 넘는가.

    삼중나선이 체온에서 풀려 버리면 '삼중나선 재료'라는 말이 배양 안에서는 성립하지 않는다.
    그래서 이 그림에는 세로선이 하나 있고, 그 선 왼쪽은 쓸 수 없다는 뜻이다.
    """
    sel = []
    for r in params:
        u = (r.get("unit") or "").strip()
        nm = (r.get("param_name") or "")
        if not re.search(r"°?\s*C\b|℃", u) and "℃" not in u:
            continue
        if not re.search(r"융해|변성|Tm|열\s*안정|melting|denatur|thermal", nm, re.I):
            continue
        v = re.findall(r"[-+]?\d+(?:\.\d+)?", str(r.get("value") or ""))
        if not v:
            continue
        sel.append((float(v[0]), (r.get("material") or "").strip(),
                    (r.get("condition") or "")[:46], nm))
    W = 920
    H = 150 + max(len(sel), 1) * 26
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "재조합 콜라겐의 삼중나선 융해온도",
                   "세로선이 배양 온도다 — 왼쪽에 있으면 배양 중에 나선이 풀린다"))
    if not sel:
        b.append(nodata(40, 70, W - 80, 48,
                        "융해온도(Tm) 값이 확보되지 않음 — 입고 검사에서 CD 융해곡선으로 직접 재야 한다"))
        return svg(W, H, "".join(b), "재조합 콜라겐 융해온도")

    sel.sort(key=lambda s: s[0])
    lo = min(min(v for v, *_ in sel) - 4, body_temp - 6)
    hi = max(max(v for v, *_ in sel) + 4, body_temp + 6)
    px0, pw = 300, 520
    def X(v): return px0 + (v - lo) / (hi - lo) * pw

    top, y = 64, 84
    bot = 84 + len(sel) * 26
    for tk in range(int(lo // 5 * 5), int(hi) + 6, 5):
        if not (lo <= tk <= hi):
            continue
        b.append(line(X(tk), top + 8, X(tk), bot, C["line"], 1, dash="3 4"))
        b.append(txt(X(tk), top, f"{tk} ℃", 9.4, C["faint"], "middle", mono=True))
    b.append(line(X(body_temp), top + 4, X(body_temp), bot + 6, C["bad"], 2))
    b.append(txt(X(body_temp), bot + 20, f"배양 {body_temp:g} ℃", 10.4, C["bad"],
                 "middle", "700"))

    for v, mat, cond, nm in sel:
        ok = v >= body_temp
        col = C["ok"] if ok else C["bad"]
        b.append(txt(292, y + 14, (cond or nm)[:32], 10.4, C["ink"], "end"))
        if mat:
            b.append(txt(292, y + 25, f"재료 {mat}", 9.2, C["faint"], "end", mono=True))
        b.append(line(X(lo), y + 11, X(v), y + 11, col, 1.2, op=.35))
        b.append(circ(X(v), y + 11, 5.2, col, "#FFFFFF", 1.3))
        b.append(txt(X(v) + 10, y + 15, f"{v:g} ℃", 9.8, col, mono=True, weight="600"))
        y += 26
    b.append(txt(24, H - 22, "값은 rc_params.csv에서 단위가 온도이고 이름에 융해·변성·열안정이 "
                             "들어간 행만 옮긴 것이다. 측정법은 본문 표에 있다.", 10.3, C["faint"]))
    return svg(W, H, "".join(b), "재조합 콜라겐 융해온도")
