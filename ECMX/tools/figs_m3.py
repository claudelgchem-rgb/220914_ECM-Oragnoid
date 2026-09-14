# -*- coding: utf-8 -*-
"""M3(오가노이드 필수물질) 전용 그림: 필수도 피라미드, 축별 근거강도, 강성 범위, 조직 히트맵."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *
SURF = C["surface"]


def fig_pyramid(counts, notes):
    """필수도 피라미드 E0~E3. counts={'E0':n,...}, notes={'E0':'설명'}"""
    W, H = 880, 430
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "오가노이드 지지체 필수도 등급 — 무엇을 '필수'라 부를 수 있는가", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "위로 갈수록 요구되는 근거의 수준이 높다. 총설이나 제조사 자료만으로는 아래 두 칸까지밖에 올라갈 수 없다.",
                 10.4, C["mut"], "middle"))
    tiers = [
        ("E0", "절대 필수", "이것이 없으면 오가노이드 형성 자체가 실패한다",
         "필요 근거: 제거·무첨가 대조군 비교 실험(OMIT), 또는 농도 0 조건(DOSE)"),
        ("E1", "조건부 필수", "특정 조직·세포·배양 단계에서만 반드시 필요하다",
         "필요 근거: 위와 동일 + 적용 조건이 원문에 명시"),
        ("E2", "성능 향상용 선택", "없어도 형성되나 효율·형태·성숙도가 유의하게 개선된다",
         "필요 근거: 형성률·크기·표지자 발현 등 정량 비교"),
        ("E3", "대체 가능 / 불필요", "다른 물질로 대체되거나, 필요하다는 근거가 없다",
         "기록 대상: 치환 실험(SUBST) 근거 또는 '근거 부재' 사실"),
    ]
    cx = 330
    top_w, bot_w = 176, 486
    y = 70
    for i, (code, name, defn, req) in enumerate(tiers):
        h = 74
        w0 = top_w + (bot_w - top_w) * (i / 3)
        w1 = top_w + (bot_w - top_w) * ((i + 1) / 3)
        x0, x1 = cx - w0/2, cx + w0/2
        x2, x3 = cx - w1/2, cx + w1/2
        b.append(f'<path d="M {x0} {y} L {x1} {y} L {x3} {y+h} L {x2} {y+h} Z" fill="{TIER_FILL[code]}" '
                 f'stroke="{TIER_SOLID[code]}" stroke-width="1.4"/>')
        n = counts.get(code, 0)
        b.append(txt(cx, y + h/2 - 6, code, 19, TIER_TXT[code], "middle", "bold"))
        b.append(txt(cx, y + h/2 + 12, f"{name} · {n}건", 11.4, TIER_TXT[code], "middle", "bold"))
        # 오른쪽 설명
        bx = 600
        b.append(txt(bx, y + 22, defn, 11, C["ink"], "start", "bold"))
        b.append(wrap(bx, y + 38, req, 9.7, 30, 12.5, C["mut"]))
        nt = notes.get(code)
        if nt:
            b.append(txt(bx, y + 64, nt[:52], 9.5, TIER_SOLID[code], "start", "bold"))
        y += h + 4
    b.append(rect(30, H - 52, W - 60, 42, C["e0"], rx=8, op=0.08))
    b.append(rect(30, H - 52, 4.5, 42, C["e0"], rx=2))
    b.append(txt(46, H - 34, "핵심 규칙", 11, C["ink"], "start", "bold"))
    b.append(txt(46, H - 19, "총설(REVIEW)이나 제조사 자료(VENDOR)만 있는 항목에는 E0·E1을 부여하지 않았다. "
                             "관행적으로 '필수 성분'이라 불리더라도 실험 근거가 없으면 E3로 내렸다.", 10.1, C["mut"]))
    return svg(W, H, "".join(b), "필수도 등급 피라미드")


def fig_axis_strength(rows):
    """축별 근거 강도 막대. rows=[(축코드, 축이름, n_omit, n_subst, n_dose, n_weak)]"""
    W = 880
    H = 104 + len(rows) * 34 + 74
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "아홉 개 요구 축별 근거의 강도", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "막대 길이는 확보한 근거 건수, 색은 근거의 종류다. 진한 색(제거·치환·농도반응)만이 '절대 필수' 판정을 지지할 수 있다.",
                 10.4, C["mut"], "middle"))
    cols = [(C["e0"], "OMIT 제거·무첨가 실험"), (C["acc"], "SUBST 치환 실험"),
            (C["e2"], "DOSE 농도반응"), (C["e3"], "REVIEW·VENDOR (약한 근거)")]
    b.append(legend(200, 68, cols, 9.8, horiz=True, box=9))
    x_lab, x_bar, bar_w = 250, 258, 500
    mx = max([sum(r[2:]) for r in rows] + [1])
    y = 106
    for code, name, *vals in rows:
        b.append(txt(x_lab - 6, y + 4, code, 11, C["ink"], "end", "bold"))
        b.append(txt(x_lab - 44, y + 4, "", 10))
        b.append(txt(x_bar, y - 13, name, 10.2, C["mut"], "start"))
        cx = x_bar
        for v, (col, _) in zip(vals, cols):
            w = (v / mx) * bar_w
            if w > 0:
                b.append(rect(cx, y - 6, w, 16, col, rx=2.5, op=0.88))
                if w > 22:
                    b.append(txt(cx + w/2, y + 5.5, str(v), 9.4,
                                 "#fff" if col in (C["e0"], C["acc"]) else C["ink"], "middle", "bold"))
            cx += w
        tot = sum(vals)
        b.append(txt(cx + 8, y + 5, f"계 {tot}", 9.8, C["mut"], "start", "bold"))
        y += 34
    b.append(txt(30, H - 40, "축마다 근거의 두께가 다르다. 근거가 얇은 축은 결론을 강하게 쓸 수 없는 영역이며, 본문에서 그렇게 명시했다.",
                 10.2, C["mut"]))
    b.append(txt(30, H - 24, "'약한 근거'만 있는 축은 E2 이하로만 판정했다.", 10.2, C["mut"]))
    return svg(W, H, "".join(b), "축별 근거 강도 막대 그래프")


def fig_stiffness(bands, lo=10.0, hi=5e4):
    """조직별 강성 범위 구간 차트 (로그 스케일).
    bands = [(라벨, 최소Pa, 최대Pa, 최적Pa 또는 None, 측정법, 출처표시, 색키)]
    """
    W = 880
    H = 118 + len(bands) * 31 + 92
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "오가노이드 배양에 보고된 기질 강성 범위", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "가로축은 로그 눈금이며 단위는 파스칼(Pa)이다. 막대는 해당 문헌이 시험한 범위, 세로 표시(◆)는 최적으로 보고된 값이다.",
                 10.4, C["mut"], "middle"))
    b.append(txt(W/2, 59, "측정법이 다르면 같은 재료도 값이 달라진다. 각 행에 측정법을 함께 적은 이유다.",
                 10.4, C["mut"], "middle", "bold"))

    x0, bw = 246, 470
    X, ticks = logticks(lo, hi, bw, x0)
    ytop, ybot = 96, H - 84
    # 눈금
    for v in ticks:
        x = X(v)
        b.append(line(x, ytop, x, ybot, C["line"], 1, "2 3", 0.8))
        b.append(txt(x, ytop - 6, fmt_pa(v), 9.2, C["faint"], "middle"))
    b.append(line(x0, ybot, x0 + bw, ybot, C["line2"], 1.2))
    b.append(txt(x0 + bw/2, ybot + 26, "기질 강성 (로그 눈금)", 10.4, C["mut"], "middle", "bold"))

    y = ytop + 20
    for lab, mn, mx_, opt, meth, src, ck in bands:
        col = C.get(ck, C["acc"])
        b.append(txt(x0 - 10, y + 4, lab, 10.8, C["ink"], "end", "bold"))
        b.append(txt(x0 - 10, y + 15, meth, 8.6, C["faint"], "end"))
        xa, xb = X(max(mn, lo)), X(min(mx_, hi))
        b.append(rect(xa, y - 6, max(xb - xa, 3), 15, col, rx=3, op=0.34))
        b.append(rect(xa, y - 6, max(xb - xa, 3), 15, "none", rx=3, stroke=col, sw=1.1))
        b.append(line(xa, y - 8, xa, y + 11, col, 1.6))
        b.append(line(xb, y - 8, xb, y + 11, col, 1.6))
        if opt:
            xo = X(opt)
            b.append(f'<path d="M {xo} {y-9} L {xo+5.4} {y+1.5} L {xo} {y+12} L {xo-5.4} {y+1.5} Z" '
                     f'fill="{col}" stroke="#fff" stroke-width="1"/>')
        b.append(txt(x0 + bw + 10, y + 4, src, 9, C["faint"], "start"))
        y += 31
    b.append(rect(30, H - 58, W - 60, 46, C["acc"], rx=8, op=0.07))
    b.append(rect(30, H - 58, 4.5, 46, C["acc"], rx=2))
    b.append(txt(46, H - 40, "해석 시 주의", 11, C["ink"], "start", "bold"))
    b.append(txt(46, H - 25, "저장탄성률(G′)과 영률(E)은 서로 다른 물리량이며 단순 환산이 불가능하다. 유변계 진동측정과 원자간력현미경은 "
                             "같은 시료에서도 값이 다르게 나온다.", 10.1, C["mut"]))
    b.append(txt(46, H - 12, "따라서 이 그림은 '절대적 최적값'이 아니라 '각 문헌이 자기 측정법으로 보고한 작동 범위'로 읽어야 한다.",
                 10.1, C["mut"]))
    return svg(W, H, "".join(b), "조직별 기질 강성 범위 구간 차트")


def fig_heatmap(cols, rows):
    """조직 × 요구사항 히트맵. cols=[열이름], rows=[(조직명,[셀값...])] 셀값은 'E0'~'E3' 시작"""
    W = 880
    lead = 116
    cw = max(58, min(88, int((W - lead - 30) / max(1, len(cols)))))
    H = 152 + len(rows) * 40 + 86
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "조직별 요구 차이 매트릭스", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "같은 '오가노이드'라도 조직마다 지지체에 요구하는 것이 다르다. 한 조직에서 필수인 것이 다른 조직에서는 선택이 된다.",
                 10.4, C["mut"], "middle"))
    b.append(legend(240, 68, [(TIER_FILL[t], f"{t} {n}") for t, n in
                              (("E0", "절대필수"), ("E1", "조건부"), ("E2", "선택"), ("E3", "대체가능·근거없음"))],
                    9.8, horiz=True, box=10))
    y0 = 96
    for j, cname in enumerate(cols):
        x = lead + j * cw
        b.append(f'<g transform="translate({x+cw/2},{y0+44}) rotate(-42)">'
                 f'<text x="0" y="0" font-size="9.4" fill="{C["mut"]}" text-anchor="start" '
                 f'font-weight="bold">{esc(cname[:16])}</text></g>')
    y = y0 + 52
    for i, (tissue, cells) in enumerate(rows):
        b.append(rect(10, y, W - 20, 38, C["line"], rx=5, op=0.16 if i % 2 else 0.05))
        b.append(txt(lead - 10, y + 23, tissue, 10.8, C["ink"], "end", "bold"))
        for j, v in enumerate(cells[:len(cols)]):
            x = lead + j * cw
            t = (v or "").strip()[:2]
            fill = TIER_FILL.get(t, TIER_FILL["E3"])
            solid = TIER_SOLID.get(t, C["e3"])
            b.append(rect(x + 3, y + 5, cw - 6, 28, fill, rx=4, stroke=solid, sw=1))
            b.append(txt(x + cw/2, y + 23, t or "-", 11, TIER_TXT.get(t, C["ink"]), "middle", "bold"))
        y += 40
    b.append(txt(20, H - 56, "색만으로 구분하지 않도록 각 칸에 등급 글자를 함께 표기했다. 괄호 안의 단서 조건은 본문 표에 실었다.",
                 10.2, C["mut"]))
    b.append(txt(20, H - 40, "E3가 '필요 없다'를 뜻하는 경우와 '근거를 찾지 못했다'를 뜻하는 경우가 섞여 있으므로 본문 판정 사유를 함께 보아야 한다.",
                 10.2, C["mut"]))
    b.append(txt(20, H - 24, "빈 칸이 없도록 8개 조직 전부를 채웠으며, 근거가 없는 칸은 E3(근거없음)으로 명시했다.",
                 10.2, C["mut"], "start", "bold"))
    return svg(W, H, "".join(b), "조직별 요구사항 히트맵")
