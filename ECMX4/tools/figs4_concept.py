# -*- coding: utf-8 -*-
"""ECMX-004 개념도.

이 보고서의 축은 하나 더 있다 — 재료가 삼중나선이냐 단일사슬이냐.
그 구분이 인테그린 결합과 섬유형성 양쪽을 가르므로, 개념도는 전부 그 분기를 그린다.
판정(가능/불가)은 인자로 받는다. 근거가 정하지 내가 정하지 않는다.
"""
import math
from figlib2 import *

MAT = {
    "A": ("A", "재조합 인간 I형", "단일사슬", "sc"),
    "B": ("B", "재조합 인간 III형", "단일사슬", "sc"),
    "C": ("C", "재조합 인간 III형", "삼중나선", "th"),
}
C_TH = C["mx"]          # 삼중나선 — 계통색
C_SC = "#B87A14"        # 단일사슬 — 조건부색


def _chain(x, y, w, amp=5.0, period=26, col=None, sw=2.0, dash=None, phase=0.0):
    """폴리펩타이드 한 가닥을 물결선으로."""
    pts = []
    n = int(w / 3) + 1
    for i in range(n + 1):
        t = i / n
        px = x + t * w
        py = y + amp * math.sin(2 * math.pi * (t * w / period) + phase)
        pts.append(f"{px:.1f} {py:.1f}")
    return path("M" + " L".join(pts), "none", col or C["ink"], sw, dash=dash)


def _helix(x, y, w, col=None, sw=2.0):
    """세 가닥이 서로 꼬인 삼중나선."""
    col = col or C_TH
    out = []
    for k, ph in enumerate((0.0, 2.094, 4.189)):
        out.append(_chain(x, y, w, amp=7.5, period=34, col=col, sw=sw, phase=ph))
    # 꼬임을 읽히게 하는 가로 묶음
    n = int(w / 17)
    for i in range(1, n):
        px = x + i * w / n
        out.append(line(px, y - 7.5, px, y + 7.5, col, 0.9, op=.35))
    return "".join(out)


def fig_three_materials(verdicts=None):
    """그림. 손에 쥔 세 재료 — 무엇이 물리적으로 다른가.

    verdicts: {재료코드: [(항목, '가능'|'불가'|'조건부'|'미확인', 한 줄 설명)]}
    """
    W, H = 960, 414
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "손에 쥔 세 재료",
                   "차이는 '어느 형(type)이냐'가 아니라 '삼중나선이냐 아니냐'에서 먼저 갈린다"))

    cw, gap = 300, 12
    for i, key in enumerate(("A", "B", "C")):
        code, nm, frm, kind = MAT[key]
        col = C_TH if kind == "th" else C_SC
        x = 20 + i * (cw + gap)
        b.append(rect(x, 52, cw, 330, "#FFFFFF", rx=11, stroke=col, sw=1.6))
        # 머리
        b.append(rect(x, 52, cw, 40, col, rx=11))
        b.append(rect(x, 76, cw, 16, col))
        b.append(circ(x + 26, 72, 12, "#FFFFFF", op=.22))
        b.append(txt(x + 26, 77, code, 14, "#FFFFFF", "middle", "700", mono=True))
        b.append(txt(x + 48, 70, nm, 12.4, "#FFFFFF", weight="700"))
        b.append(txt(x + 48, 84, frm, 10.4, "#FFFFFF", op=.88, mono=True))

        # 분자 모식
        b.append(rect(x + 14, 104, cw - 28, 74, "#FAFCFC", rx=7, stroke=C["line"]))
        if kind == "th":
            b.append(_helix(x + 30, 141, cw - 60, col, 2.0))
            b.append(txt(x + cw / 2, 170, "세 가닥이 꼬여 하나의 막대를 이룸", 9.4, C["mut"], "middle"))
        else:
            for k, dy in enumerate((-16, 0, 16)):
                b.append(_chain(x + 30, 141 + dy, cw - 60, amp=5.2, period=24,
                                col=col, sw=1.8, dash="6 4", phase=k * 1.7))
            b.append(txt(x + cw / 2, 170, "가닥이 따로 떠 있음 — 꼬이지 않음", 9.4, C["mut"], "middle"))

        # 판정
        yy = 196
        vs = (verdicts or {}).get(key) or [
            ("인테그린 결합", "미확인", "근거 대기"),
            ("자발 섬유형성", "미확인", "근거 대기"),
            ("37 ℃ 구조 유지", "미확인", "근거 대기"),
            ("구조 기여", "미확인", "근거 대기"),
        ]
        for lab, v, note in vs[:5]:
            vc = {"가능": C["ok"], "불가": C["bad"], "조건부": C["cnd"],
                  "미확인": C["faint"]}.get(v, C["faint"])
            b.append(txt(x + 18, yy + 11, lab, 10.6, C["ink"], weight="600"))
            tw = len(v) * 9.4 + 12
            b.append(rect(x + cw - 18 - tw, yy, tw, 16, vc, rx=8))
            b.append(txt(x + cw - 18 - tw / 2, yy + 12, v, 9.6, "#FFFFFF", "middle", "600"))
            b.append(txt(x + 18, yy + 26, note[:34], 9.3, C["mut"]))
            b.append(line(x + 14, yy + 34, x + cw - 14, yy + 34, C["line"], 1))
            yy += 44
    b.append(txt(20, H - 10,
                 "판정은 본문 근거에서 가져온 것이며, 근거를 찾지 못한 칸은 '미확인'으로 둔다.",
                 10.2, C["faint"]))
    return svg(W, H, "".join(b), "세 재료의 물리적 차이와 판정")


def fig_integrin_gate(th_ok="미확인", sc_ok="미확인", note_th="", note_sc="",
                      ints_th=("", ""), ints_sc=("", "")):
    """그림. 세포는 무엇을 보고 붙는가 — 삼중나선이 있어야 보이는 자리.

    이 보고서의 중심 개념이다. 콜라겐의 인테그린 결합부위는 세 가닥이 꼬여 있을 때만
    입체적으로 완성되므로, 가닥이 풀리면 그 자리가 사라진다. 대신 평소 숨어 있던
    자리가 드러나 다른 인테그린이 붙는다 — 같은 단백질인데 세포가 다르게 읽는다.
    """
    W, H = 960, 356
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "세포는 무엇을 보고 붙는가",
                   "같은 단백질이라도 삼중나선이 풀리면 세포가 읽는 자리가 바뀐다"))

    for i, (ttl, sub, kind, col, verdict, note) in enumerate([
        ("삼중나선일 때", "세 가닥이 꼬여 있음", "th", C_TH, th_ok, note_th),
        ("단일사슬일 때", "가닥이 풀려 있음", "sc", C_SC, sc_ok, note_sc),
    ]):
        x = 20 + i * 470
        b.append(rect(x, 52, 450, 254, "#FFFFFF", rx=11, stroke=col, sw=1.5))
        b.append(txt(x + 20, 76, ttl, 13, col, weight="700"))
        b.append(txt(x + 20, 92, sub, 10.4, C["mut"]))

        # 분자
        my = 132
        if kind == "th":
            b.append(_helix(x + 30, my, 390, col, 2.1))
            # 결합부위 표시
            for px in (x + 130, x + 260):
                b.append(rect(px - 22, my - 15, 44, 30, "none", rx=6, stroke=C["ok"], sw=1.8))
                b.append(txt(px, my - 20, "GFOGER", 8.8, C["ok"], "middle", "700", mono=True))
        else:
            for k, dy in enumerate((-18, 0, 18)):
                b.append(_chain(x + 30, my + dy, 390, amp=5.4, period=24, col=col,
                                sw=1.7, dash="6 4", phase=k * 1.7))
            for px in (x + 130, x + 260):
                b.append(rect(px - 22, my - 15, 44, 30, "none", rx=6, stroke=C["bad"],
                              sw=1.4, dash="3 3"))
                b.append(txt(px, my - 26, "자리 소실", 8.8, C["bad"], "middle", "700"))
            if note_sc:
                b.append(txt(x + 340, my + 34, "가닥이 풀린 상태", 9.2, C["cnd"], "middle"))

        # 세포 쪽
        cy = 178
        b.append(rect(x + 20, cy, 410, 56, C["mx_bg"] if kind == "th" else "#FBF2E0",
                      rx=8, stroke=col, sw=.9))
        b.append(txt(x + 34, cy + 22, "세포가 쓰는 인테그린", 10.4, C["mut"], weight="600"))
        ints = (ints_th if kind == "th" else ints_sc)
        if not ints[0]:
            ints = ("근거 대기", "")
        b.append(txt(x + 34, cy + 42, ints[0], 12, C["ink"], weight="700", mono=True))
        b.append(txt(x + 250, cy + 42, ints[1], 10.2, C["mut"]))

        # 판정
        vc = {"가능": C["ok"], "불가": C["bad"], "조건부": C["cnd"]}.get(verdict, C["faint"])
        b.append(rect(x + 20, 242, 410, 52, "#FFFFFF", rx=8, stroke=vc, sw=1.4))
        tw = len(verdict) * 10 + 16
        b.append(rect(x + 34, 256, tw, 20, vc, rx=10))
        b.append(txt(x + 34 + tw / 2, 271, verdict, 10.6, "#FFFFFF", "middle", "700"))
        wtxt, _ = wrap(x + 34 + tw + 12, 263, note or "근거 대기", 10, width=32, lh=13,
                       fill=C["mut"])
        b.append(wtxt)

    b.append(rect(20, 318, W - 40, 26, C["cnd_bg"], rx=7, stroke=C["cnd"]))
    b.append(txt(34, 335,
                 "이 그림이 이 보고서의 분기점이다 — 접착 리간드(L5)를 따로 사야 하는지가 여기서 갈린다.",
                 10.8, C["cnd"], weight="600"))
    return svg(W, H, "".join(b), "삼중나선 유무에 따른 인테그린 결합 경로")


def fig_gel_decision(spontaneous="미확인", routes=None):
    """그림. 겔을 어떻게 세울 것인가 — 자발 겔화가 안 될 때의 갈림길."""
    W, H = 960, 420
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "겔을 세우는 경로",
                   "동물유래 콜라겐은 중화하고 데우면 굳는다. 재조합 재료도 그런가에서 시작한다"))

    # 질문
    qx, qy, qw = 300, 56, 360
    b.append(rect(qx, qy, qw, 46, "#FFFFFF", rx=10, stroke=C["ink"], sw=1.6))
    b.append(txt(qx + qw / 2, qy + 20, "중화 후 37 ℃ 승온만으로 굳는가?", 12.4, C["ink"],
                 "middle", "700"))
    b.append(txt(qx + qw / 2, qy + 36, "= 고전적 섬유형성(fibrillogenesis)", 9.6, C["faint"], "middle"))

    vc = {"가능": C["ok"], "불가": C["bad"], "조건부": C["cnd"]}.get(spontaneous, C["faint"])
    b.append(line(qx + qw / 2, qy + 46, qx + qw / 2, 128, vc, 2, marker="ar"))
    tw = len(spontaneous) * 11 + 20
    b.append(rect(qx + qw / 2 - tw / 2, 108, tw, 22, vc, rx=11))
    b.append(txt(qx + qw / 2, 124, spontaneous, 11.4, "#FFFFFF", "middle", "700"))

    routes = routes or [
        ("화학 가교", "굳은 뒤가 아니라 굳히기 위해 넣는다", "L6", C["mx"], "근거 대기"),
        ("광가교 플랫폼", "메타크릴화 재조합 콜라겐 + 개시제", "L6", C["cnd"], "근거 대기"),
        ("하이브리드 백본", "다른 고분자가 망을 세우고 콜라겐은 신호를 준다", "L7", C["md"], "근거 대기"),
    ]
    cw = (W - 40 - (len(routes) - 1) * 14) / len(routes)
    for i, (nm, desc, lay, col, note) in enumerate(routes):
        x = 20 + i * (cw + 14)
        b.append(line(qx + qw / 2, 138, x + cw / 2, 168, C["line2"], 1.4, dash="4 3"))
        b.append(rect(x, 172, cw, 186, "#FFFFFF", rx=10, stroke=col, sw=1.5))
        b.append(rect(x, 172, cw, 30, col, rx=10))
        b.append(rect(x, 190, cw, 12, col))
        b.append(txt(x + 14, 192, nm, 12.4, "#FFFFFF", weight="700"))
        b.append(txt(x + cw - 14, 192, lay, 10.4, "#FFFFFF", "end", "700", mono=True))
        wt, n = wrap(x + 14, 224, desc, 10.6, width=24, lh=15, fill=C["ink"])
        b.append(wt)
        b.append(line(x + 12, 224 + n * 15 + 6, x + cw - 12, 224 + n * 15 + 6, C["line"], 1))
        wt2, _ = wrap(x + 14, 224 + n * 15 + 24, note, 10, width=25, lh=14, fill=C["mut"])
        b.append(wt2)

    b.append(rect(20, 372, W - 40, 30, C["mx_bg"], rx=7, stroke=C["mx_ln"]))
    b.append(txt(34, 391,
                 "어느 경로를 고르든 첫 질문은 같다 — 세포를 넣은 채로 굳힐 수 있는가.",
                 10.8, C["mx"], weight="600"))
    return svg(W, H, "".join(b), "겔화 경로 결정도")


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
    b.append(txt(46, 78, "세포를 담는 고체 — 재조합 콜라겐 겔", 10.5, C["mx"], op=.85))
    mx_items = [
        ("L1", "재조합 콜라겐 A · B · C", "I형 단일 · III형 단일 · III형 삼중"),
        ("L6", "가교제 · 광개시제", "자발 겔화가 없으면 여기서 망을 세운다"),
        ("L5", "접착 리간드 · 라미닌", "세포가 붙을 자리를 공급"),
        ("L7", "하이브리드 백본", "다른 고분자가 구조를 맡는 경우"),
        ("L8·L9", "완충액 · 입고 검사 규격", "용해 조건과 로트 관리"),
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
