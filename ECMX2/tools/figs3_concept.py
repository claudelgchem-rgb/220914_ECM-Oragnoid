# -*- coding: utf-8 -*-
"""ECMX-003 개념도 — 수치를 주장하지 않는 구조 도판.

여기 그림들은 '무엇이 어디에 들어가는가'라는 배치 문제를 다룬다. 수치가 필요한
도판은 figs3_data.py에 있고, 그쪽은 CSV에서 값을 받아야만 그려진다.
"""
from figlib2 import *


def fig_two_systems():
    """그림 1. 지지체 계통과 배지 계통 — 이 보고서의 뼈대.

    이 분야 문헌에서 가장 흔한 혼동이 '배지에 넣는 EGF'와 '매트릭스에 붙이는 EGF'를
    같은 줄에 적는 것이다. 그래서 첫 그림이 이 분리다.
    """
    W, H = 880, 430
    b = [rect(0, 0, W, H, C["bg"], rx=0)]

    # 가운데 세포/오가노이드
    cx, cy = W / 2, 208
    b.append(circ(cx, cy, 62, "#FFFFFF", C["ink"], 1.6))
    b.append(circ(cx, cy, 40, "#F4F7F8", C["line2"], 1))
    for i, (dx, dy) in enumerate([(-22, -14), (0, -24), (22, -12), (-24, 12), (2, 20), (24, 10)]):
        b.append(circ(cx + dx, cy + dy, 9.5, "#FFFFFF", C["mut"], 1.2))
    b.append(txt(cx, cy + 86, "오가노이드", 13, C["ink"], "middle", "600"))
    b.append(txt(cx, cy + 102, "상피 줄기세포 유래 3차원 조직", 10, C["faint"], "middle"))

    # 왼쪽 — 지지체
    b.append(rect(26, 34, 300, 344, C["mx_bg"], rx=12, stroke=C["mx"], sw=1.6))
    b.append(txt(46, 60, "지지체 계통 (매트릭스)", 14, C["mx"], weight="700"))
    b.append(txt(46, 78, "세포를 담는 고체 — 콜라겐 I/III 겔", 10.5, C["mx"], op=.85))
    mx_items = [
        ("L1", "콜라겐 I형·III형", "골격 섬유를 만드는 본체"),
        ("L8", "중화 염기·10× 완충액·NaCl", "pH·이온강도가 섬유 굵기를 정한다"),
        ("L5", "라미닌/기저막 성분", "상피 극성을 세우는 접착 리간드"),
        ("L6", "가교제", "굳은 뒤의 강성과 분해 저항"),
        ("L2·L7", "히알루론산·알지네이트·PEG", "점탄성·응력완화 조절"),
    ]
    y = 100
    for tag, nm, desc in mx_items:
        b.append(rect(44, y, 264, 44, "#FFFFFF", rx=7, stroke=C["mx_ln"]))
        b.append(txt(54, y + 18, tag, 10, C["mx"], weight="700", mono=True))
        b.append(txt(88, y + 18, nm, 12.2, C["ink"], weight="600"))
        b.append(txt(54, y + 34, desc, 10, C["mut"]))
        b.append(line(310, y + 22, cx - 68, cy, C["mx"], 1.2, dash="3 3", op=.5))
        y += 54

    # 오른쪽 — 배지
    b.append(rect(554, 34, 300, 344, C["md_bg"], rx=12, stroke=C["md"], sw=1.6))
    b.append(txt(574, 60, "배지 계통 (액상)", 14, C["md"], weight="700"))
    b.append(txt(574, 78, "매일 갈아주는 액체 — 직접 조제", 10.5, C["md"], op=.85))
    md_items = [
        ("기본", "Advanced DMEM/F-12", "당·아미노산·염의 바탕"),
        ("보충", "B-27 · N-2 · NAC", "혈청을 대신하는 정의 보충제"),
        ("니치", "EGF · Noggin · R-spondin · Wnt3a", "줄기세포를 유지시키는 신호"),
        ("저분자", "Y-27632 · A83-01 · CHIR99021", "넣는 시점이 정해져 있다"),
        ("완충", "HEPES · GlutaMAX · 중탄산", "pH·삼투압"),
    ]
    y = 100
    for tag, nm, desc in md_items:
        b.append(rect(572, y, 264, 44, "#FFFFFF", rx=7, stroke=C["md_ln"]))
        b.append(txt(582, y + 18, tag, 10, C["md"], weight="700", mono=True))
        b.append(txt(614, y + 18, nm, 11.4, C["ink"], weight="600"))
        b.append(txt(582, y + 34, desc, 10, C["mut"]))
        b.append(line(570, y + 22, cx + 68, cy, C["md"], 1.2, dash="3 3", op=.5))
        y += 54

    # 경계 경고
    b.append(rect(cx - 150, 392, 300, 26, "#FFFFFF", rx=13, stroke=C["bad"], sw=1.3))
    b.append(txt(cx, 409, "두 계통을 한 표에 섞어 적는 것이 최빈 오류", 11, C["bad"],
                 "middle", "600"))
    return svg(W, H, "".join(b),
               "지지체 계통과 배지 계통을 분리한 개념도")


def fig_gel_flow(neutral_note="pH 7.2~7.4", temp_note="37 ℃", conc_note="2~4 mg/mL"):
    """그림. 콜라겐 I/III 겔 제조 흐름 — 시간축 위의 되돌릴 수 없는 지점들.

    수치는 인자로 받는다. CL 에이전트가 확정한 값만 들어간다.
    """
    W, H = 950, 392
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "콜라겐 겔 제조 — 시간축", "얼음 위에서 섞고, 37 ℃에서 굳힌다"))

    x0, x1, ty = 40, 920, 176
    b.append(line(x0, ty, x1, ty, C["line2"], 2))

    b.append(rect(x0, 196, 470 - x0, 22, "#DCEAF2", rx=4, stroke="#8FB8CE"))
    b.append(txt((x0 + 470) / 2, 211, "4 ℃ — 얼음 위 (섬유 생성 억제)", 10.5, "#2C5F8D", "middle", "600"))
    b.append(rect(470, 196, x1 - 470, 22, "#FBE7DC", rx=4, stroke="#D89A7A"))
    b.append(txt((470 + x1) / 2, 211, f"{temp_note} — 인큐베이터 (섬유 생성 진행)", 10.5,
                 "#9A4B18", "middle", "600"))

    steps_ = [
        ("콜라겐 원액", f"산성 용액 {conc_note}", "해동 후 기포 없이", "mx"),
        ("10× 완충액", "부피의 1/10", "이온강도를 맞춘다", "mx"),
        ("염기로 중화", f"목표 {neutral_note}", "★ 되돌릴 수 없음", "req"),
        ("세포 현탁", "중화 직후 · 차가울 때", "따뜻해지면 늦다", "req"),
        ("분주 · 겔화", f"{temp_note}, 30분", "건드리지 않는다", "mx"),
        ("배지 얹기", "굳은 뒤에만", "배지 계통으로 인계", "md"),
    ]
    bw, gap = 132, 148
    for k, (nm, d1, d2) in enumerate([(a, c, d) for a, c, d, _ in steps_]):
        kind = steps_[k][3]
        col = {"mx": C["mx"], "md": C["md"], "req": C["bad"]}[kind]
        bx = x0 + 4 + k * gap
        cxp = bx + bw / 2
        b.append(rect(bx, 52, bw, 58, "#FFFFFF", rx=7, stroke=col, sw=1.3))
        b.append(txt(bx + 11, 72, nm, 11.8, C["ink"], weight="600"))
        b.append(txt(bx + 11, 88, d1, 9.5, C["mut"]))
        b.append(txt(bx + 11, 101, d2, 9.5, C["bad"] if d2.startswith("★") else C["mut"],
                     weight="600" if d2.startswith("★") else "400"))
        b.append(line(cxp, 110, cxp, ty - 9, C["line"], 1))
        b.append(circ(cxp, ty, 8, "#FFFFFF", col, 2.4))
        b.append(circ(cxp, ty, 3.4, col))

    b.append(rect(x0, 244, x1 - x0, 122, "#FFFFFF", rx=8, stroke=C["line"]))
    b.append(txt(x0 + 16, 267, "이 흐름에서 실패가 나는 자리", 11.8, C["ink"], weight="600"))
    fails = [
        ("중화 부족", "pH가 7 아래면 섬유가 성글게 서거나 아예 서지 않는다"),
        ("상온 방치", "중화 뒤 미지근해지면 세포를 넣기 전에 굳기 시작한다"),
        ("기포 · 교반", "거품이 섬유망을 끊어 겔이 불균일해진다"),
        ("세포 늦은 투입", "굳는 중에 넣으면 세포가 표면에만 몰린다"),
    ]
    for i2, (a, d) in enumerate(fails):
        yy = 291 + i2 * 19
        b.append(circ(x0 + 24, yy - 4, 2.8, C["bad"]))
        b.append(txt(x0 + 36, yy, a, 10.6, C["bad"], weight="600"))
        b.append(txt(x0 + 148, yy, d, 10.4, C["mut"]))
    return svg(W, H, "".join(b), "콜라겐 겔 제조 시간축과 실패 지점")


def fig_collagen_source():
    """그림. 콜라겐 원료 선택 — 텔로/아텔로/재조합.

    축은 둘이다: 이종 항원 위험(세로)과 확보 난이도·단가(가로). 눈금을 그리지 않는다.
    정량 축을 그리면 근거에 없는 수치를 만들어내는 셈이 되기 때문이다.
    """
    W, H = 940, 470
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "콜라겐 원료 선택지의 정성적 배치",
                   "눈금 없는 순위 배치 — 정량 비교가 아니다"))

    px0, py0, pw, ph = 96, 58, 700, 292
    b.append(rect(px0, py0, pw, ph, "#FCFDFD", rx=8, stroke=C["line"]))
    b.append(line(px0, py0 + ph, px0 + pw, py0 + ph, C["line2"], 1.4, marker="ar"))
    b.append(line(px0, py0 + ph, px0, py0, C["line2"], 1.4, marker="ar"))
    b.append(txt(px0 + pw / 2, py0 + ph + 32, "확보 난이도 · 단가 →", 11, C["mut"], "middle"))
    # 세로축 라벨은 회전시키지 않는다. 한글은 회전하면 읽는 속도가 눈에 띄게 떨어진다.
    b.append(txt(px0 + 10, py0 + 20, "↑ 이종 항원 · 로트 편차 위험", 10.5, C["mut"]))

    # (fx, fy, 이름, 설명, 색, 라벨방향)
    pts = [
        (0.06, 0.90, "랫 꼬리건 콜라겐 I", "텔로펩타이드 보존 · 겔화 안정", "연구용 표준", C["mx"], "r"),
        (0.30, 0.66, "소 진피 텔로콜라겐", "고전적 표준", "TSE/BSE 서류 필요", C["mx"], "r"),
        (0.44, 0.40, "돼지 · 소 아텔로콜라겐", "텔로펩타이드 제거", "면역원성을 낮춘 형태", C["mx"], "l"),
        (0.66, 0.24, "인간 태반 콜라겐 I · III", "인간 유래", "공급량 · 로트가 제한", C["cnd"], "l"),
        (0.92, 0.06, "재조합 인간 콜라겐", "동물유래 없음", "단가와 겔화 거동이 관건", C["req"], "l"),
    ]
    for fx, fy, nm, d1, d2, col, side in pts:
        X = px0 + 40 + fx * (pw - 110)
        Y = py0 + 30 + fy * (ph - 74)
        b.append(circ(X, Y, 9, "#FFFFFF", col, 2.6))
        b.append(circ(X, Y, 3.6, col))
        if side == "r":
            lx, an = X + 16, "start"
        else:
            lx, an = X - 16, "end"
        b.append(txt(lx, Y - 12, nm, 11.8, C["ink"], "600" if False else an, "600"))
        b.append(txt(lx, Y + 3, d1, 9.7, C["mut"], an))
        b.append(txt(lx, Y + 16, d2, 9.7, C["mut"], an))

    b.append(rect(px0, py0 + ph + 48, pw, 56, C["mx_bg"], rx=7, stroke=C["mx_ln"]))
    b.append(txt(px0 + 16, py0 + ph + 70, "III형 콜라겐은 이 축 위에 따로 놓이지 않는다", 11.5,
                 C["mx"], weight="600"))
    b.append(txt(px0 + 16, py0 + ph + 89,
                 "I형에 섞어 쓰는 첨가 성분이므로, 선택은 'I형을 무엇으로 하느냐' 다음에 온다.",
                 10.6, C["mut"]))
    return svg(W, H, "".join(b), "콜라겐 원료 선택지의 정성적 배치")
