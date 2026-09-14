# -*- coding: utf-8 -*-
"""개념 도식 그림들 (자체 제작 인라인 SVG, R-14)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *


def fig_signals():
    """그림: ECM이 세포에 주는 신호 4종 모식도"""
    W, H = 880, 430
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 26, "세포외기질이 세포에 전달하는 네 가지 신호", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 45, "가운데는 세포, 바깥 네 상자는 각 신호가 작용하는 경로", 11.5, C["mut"], "middle"))

    cx, cy = W/2, 232
    # 세포
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="76" ry="56" fill="{C["acc"]}" opacity="0.11"/>')
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="76" ry="56" fill="none" stroke="{C["acc"]}" stroke-width="2"/>')
    b.append(f'<ellipse cx="{cx}" cy="{cy-4}" rx="27" ry="21" fill="{C["acc"]}" opacity="0.32"/>')
    b.append(txt(cx, cy - 1, "세포", 13.5, C["ink"], "middle", "bold"))
    b.append(txt(cx, cy + 16, "(핵)", 10, C["mut"], "middle"))
    b.append(txt(cx, cy + 78, "부착 · 증식 · 분화 · 형태형성", 11.5, C["mut"], "middle", "bold"))

    boxes = [
        (36, 72, C["e0"], "① 접착 리간드", "adhesion ligand",
         "인테그린이 붙잡을 자리.\nRGD·IKVAV·GFOGER 같은\n짧은 모티프 또는 라미닌\n같은 전장 단백질이 제공한다.",
         "없으면 세포가 기질을 잡지 못한다"),
        (612, 72, C["e1"], "② 기계적 강성·점탄성", "stiffness / viscoelasticity",
         "겔이 얼마나 단단한가(G′),\n그리고 힘을 주었을 때\n얼마나 빨리 풀어지는가\n(응력완화).",
         "세포는 당겨보고 단단함을 읽는다"),
        (36, 300, C["e2"], "③ 분해성·리모델링", "degradability",
         "세포가 기질을 잘라내며\n공간을 넓힐 수 있는가.\nMMP 절단 서열 도입 여부가\n이를 좌우한다.",
         "자랄 자리를 스스로 만든다"),
        (612, 300, C["acc"], "④ 결합된 성장인자", "matrix-bound growth factor",
         "헤파란황산 등이 성장인자를\n붙잡아 두어 국소 농도를\n높인다. 배지에 푸는 것과는\n작용이 다르다.",
         "신호를 '제자리에' 붙든다"),
    ]
    for x, y, col, t1, t2, body, tag in boxes:
        w, h = 232, 118
        b.append(rect(x, y, w, h, C["surface"] if "surface" in C else "#fff", rx=9, stroke=col, sw=1.8))
        b.append(rect(x, y, 4.5, h, col, rx=2))
        b.append(txt(x + 14, y + 21, t1, 12.6, C["ink"], "start", "bold"))
        b.append(txt(x + 14, y + 35, t2, 9.6, C["mut"], "start", "normal", 1, True))
        for i, ln in enumerate(body.split("\n")):
            b.append(txt(x + 14, y + 52 + i * 13.5, ln, 10.4, C["mut"]))
        b.append(txt(x + 14, y + h - 8, tag, 9.8, col, "start", "bold"))

    # 화살표
    for (x, y, col, anchor) in [(268, 131, C["e0"], "l"), (612, 131, C["e1"], "r"),
                                (268, 359, C["e2"], "l"), (612, 359, C["acc"], "r")]:
        if anchor == "l":
            d = f"M {x} {y} C {x+60} {y}, {cx-110} {cy-40}, {cx-78} {cy-16}"
            tip = (cx - 78, cy - 16)
        else:
            d = f"M {x} {y} C {x-60} {y}, {cx+110} {cy-40}, {cx+78} {cy-16}"
            tip = (cx + 78, cy - 16)
        if y > 300:
            if anchor == "l":
                d = f"M {x} {y} C {x+60} {y}, {cx-110} {cy+40}, {cx-78} {cy+16}"
                tip = (cx - 78, cy + 16)
            else:
                d = f"M {x} {y} C {x-60} {y}, {cx+110} {cy+40}, {cx+78} {cy+16}"
                tip = (cx + 78, cy + 16)
        b.append(path(d, "none", col, 2.1, op=0.72))
        b.append(f'<circle cx="{tip[0]}" cy="{tip[1]}" r="3.6" fill="{col}"/>')

    b.append(txt(20, H - 10, "네 신호는 독립적이지 않다. 강성을 바꾸면 리간드 밀도와 분해성도 함께 변하는 경우가 많아, 한 축만 분리해 시험하려면 설계가 필요하다.",
                 10.2, C["faint"] if "faint" in C else C["mut"]))
    return svg(W, H, "".join(b), "ECM이 세포에 주는 네 가지 신호 모식도")


def fig_classes():
    """그림: 소재 5계열 분류 트리"""
    W, H = 900, 460
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "ECM 소재의 다섯 계열", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "왼쪽으로 갈수록 생체 조성에 가깝고 성능이 검증되어 있으나 정의성이 낮다. 오른쪽으로 갈수록 정의성·재현성이 높으나 생물학적 단서를 직접 넣어야 한다.",
                 10.4, C["mut"], "middle"))

    b.append(rect(40, 60, W - 80, 16, C["acc"], rx=8, op=0.09))
    b.append(txt(52, 72, "◀ 생체 유사·고성능 / 정의성 낮음", 10, C["mut"], "start", "bold"))
    b.append(txt(W - 52, 72, "정의성·재현성 높음 / 생물학적 단서 부족 ▶", 10, C["mut"], "end", "bold"))

    cols = [
        ("①천연 유래", "탈세포화 조직,\n기저막추출물(EHS)", C["e0"],
         ["조성이 생체와 가장 유사", "형성 효율 높음"],
         ["로트 간 편차 큼", "동물유래·면역원성", "성분 미정의"]),
        ("②정제 단백질", "콜라겐·젤라틴·\n피브린·라미닌", C["e1"],
         ["성분이 특정됨", "재조합 생산 가능"],
         ["물성 조절 폭 좁음", "재조합품 고가"]),
        ("③다당 기반", "히알루론산·알지네이트\n·키토산·나노셀룰로스", C["e2"],
         ["물성 조절 쉬움", "면역원성 낮음", "동물유래 회피"],
         ["접착 리간드 없음", "별도 기능화 필요"]),
        ("④합성 기반", "다분지 PEG,\n자기조립 펩타이드", C["acc"],
         ["완전 정의 조성", "물성 독립 제어", "로트 재현성 높음"],
         ["리간드·분해성을\n직접 설계해야 함", "설계 난도 높음"]),
        ("⑤하이브리드", "위 계열의 조합\n(예: PEG+라미닌)", C["e3"],
         ["장점 조합 가능", "실무에서 가장 흔함"],
         ["복잡도 상승", "규격 관리 부담"]),
    ]
    x0, w, gap = 40, 156, 9
    for i, (name, ex, col, pros, cons) in enumerate(cols):
        x = x0 + i * (w + gap)
        b.append(rect(x, 96, w, 344, "#fff" if C["bg"] == "#FFFFFF" else C["surface"] if "surface" in C else "#fff",
                      rx=9, stroke=C["line"]))
        b.append(rect(x, 96, w, 46, col, rx=9, op=0.14))
        b.append(rect(x, 96, w, 3.5, col, rx=2))
        b.append(txt(x + w/2, 117, name, 12.4, C["ink"], "middle", "bold"))
        for j, ln in enumerate(ex.split("\n")):
            b.append(txt(x + w/2, 131 + j * 11.5, ln, 9.6, C["mut"], "middle"))
        y = 166
        b.append(txt(x + 11, y, "장점", 10.2, C["e3"], "start", "bold"))
        y += 15
        for p in pros:
            for k, ln in enumerate(p.split("\n")):
                b.append(txt(x + 15, y, ("+ " if k == 0 else "  ") + ln, 9.8, C["ink"]))
                y += 13
        y += 9
        b.append(txt(x + 11, y, "한계", 10.2, C["e3"], "start", "bold"))
        y += 15
        for cn in cons:
            for k, ln in enumerate(cn.split("\n")):
                b.append(txt(x + 15, y, ("− " if k == 0 else "  ") + ln, 9.8, C["mut"]))
                y += 13
    return svg(W, H, "".join(b), "ECM 소재 5계열 분류 트리")


def fig_2d3d():
    """그림: 2D 배양 vs 3D 지지체 vs 오가노이드 비교"""
    W, H = 880, 350
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "2차원 배양 · 3차원 지지체 배양 · 오가노이드는 무엇이 다른가", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "같은 '세포를 키운다'는 말이지만 기질이 하는 일과 세포가 만들어내는 구조가 전혀 다르다", 10.6, C["mut"], "middle"))

    panes = [
        (30, "2차원 배양", "코팅된 평면 위",
         "기질은 '바닥'일 뿐이다. 세포는\n납작하게 퍼지고 극성이 왜곡된다.",
         "코팅 단백질(라미닌·비트로넥틴)은\n2D 기질이지 3D 매트릭스가 아니다."),
        (313, "3차원 지지체 배양", "겔 안에 분산",
         "세포가 사방에서 기질에 둘러싸인다.\n구형 집합체를 이루지만 조직 구조는\n반드시 생기지 않는다.",
         "스페로이드(spheroid)는 여기까지다."),
        (596, "오가노이드", "겔 안에서 자기조직화",
         "줄기세포가 스스로 극성을 세우고\n내강(lumen)을 만들고 싹눈(budding)을\n내어 조직 구조를 재현한다.",
         "기질이 '신호'를 주어야만 도달한다."),
    ]
    for x, title, sub, body, foot in panes:
        w = 254
        b.append(rect(x, 62, w, 268, C["surface"] if "surface" in C else "#fff", rx=10, stroke=C["line"]))
        b.append(txt(x + w/2, 84, title, 12.8, C["ink"], "middle", "bold"))
        b.append(txt(x + w/2, 99, sub, 10, C["mut"], "middle"))
        cx, cy = x + w/2, 158
        if title.startswith("2"):
            b.append(rect(x + 30, cy + 26, w - 60, 7, C["acc"], rx=3, op=.28))
            b.append(txt(x + w/2, cy + 48, "코팅층", 9, C["mut"], "middle"))
            for dx in (-62, -21, 20, 61):
                b.append(f'<ellipse cx="{cx+dx}" cy="{cy+19}" rx="20" ry="7.5" fill="{C["acc"]}" opacity="0.5"/>')
                b.append(f'<ellipse cx="{cx+dx}" cy="{cy+19}" rx="6" ry="3.4" fill="{C["ink"]}" opacity="0.42"/>')
        elif title.startswith("3"):
            b.append(rect(x + 26, cy - 42, w - 52, 96, C["e2"], rx=8, op=.16))
            b.append(rect(x + 26, cy - 42, w - 52, 96, "none", rx=8, stroke=C["line2"] if "line2" in C else C["line"]))
            for dx, dy, r in ((-58, -14, 15), (-8, 16, 18), (46, -18, 14), (30, 26, 11)):
                b.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r}" fill="{C["acc"]}" opacity="0.46"/>')
                b.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r}" fill="none" stroke="{C["acc"]}" stroke-width="1.2"/>')
            b.append(txt(x + w/2, cy + 68, "겔 기질", 9, C["mut"], "middle"))
        else:
            b.append(rect(x + 26, cy - 42, w - 52, 96, C["e2"], rx=8, op=.16))
            b.append(rect(x + 26, cy - 42, w - 52, 96, "none", rx=8, stroke=C["line2"] if "line2" in C else C["line"]))
            b.append(f'<circle cx="{cx}" cy="{cy+4}" r="34" fill="{C["acc"]}" opacity="0.30"/>')
            b.append(f'<circle cx="{cx}" cy="{cy+4}" r="34" fill="none" stroke="{C["acc"]}" stroke-width="1.8"/>')
            b.append(f'<circle cx="{cx}" cy="{cy+4}" r="16" fill="{C["bg"]}"/>')
            b.append(f'<circle cx="{cx}" cy="{cy+4}" r="16" fill="none" stroke="{C["acc"]}" stroke-width="1.2" stroke-dasharray="3 2"/>')
            b.append(txt(cx, cy + 8, "내강", 8.6, C["mut"], "middle"))
            for ang, rr in ((-125, 36), (-60, 36), (10, 36), (78, 36), (145, 36)):
                import math as _m
                bx = cx + rr * _m.cos(_m.radians(ang)); by = cy + 4 + rr * _m.sin(_m.radians(ang))
                b.append(f'<circle cx="{bx}" cy="{by}" r="10.5" fill="{C["e1"]}" opacity="0.62"/>')
            b.append(txt(x + w/2, cy + 68, "싹눈(budding) 구조", 9, C["mut"], "middle"))
        yy = 246
        for ln in body.split("\n"):
            b.append(txt(x + 15, yy, ln, 10.2, C["ink"])); yy += 13.5
        yy += 4
        for ln in foot.split("\n"):
            b.append(txt(x + 15, yy, ln, 9.5, C["mut"], "start", "normal", 1, True)); yy += 12
    for ax in (290, 573):
        b.append(txt(ax, 196, "→", 21, C["line2"] if "line2" in C else C["line"], "middle", "bold"))
    return svg(W, H, "".join(b), "2D 배양·3D 지지체·오가노이드 비교 도식")
