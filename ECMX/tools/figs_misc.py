# -*- coding: utf-8 -*-
"""연표, 공급사 분포, 요약 도식."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *
SURF = C["surface"]


def fig_timeline(events):
    """연표. events=[(연도, 제목, 한줄설명, 중요도 1~3)]"""
    W = 880
    rowh = 46
    H = 104 + len(events) * rowh + 60
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "ECM 소재와 오가노이드 지지체의 기술 계보", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "굵게 표시한 항목은 지지체 소재 관점에서 방향을 바꾼 전환점이다. 각 항목은 본문에서 근거 문헌과 함께 다룬다.",
                 10.4, C["mut"], "middle"))
    ax = 120
    y0 = 76
    y1 = y0 + len(events) * rowh
    b.append(line(ax, y0, ax, y1, C["line2"], 2))
    for i, (yr, title, desc, imp) in enumerate(events):
        y = y0 + i * rowh + 22
        r = 4 + imp * 1.9
        col = [C["e3"], C["acc"], C["e1"], C["e0"]][min(imp, 3)]
        b.append(f'<circle cx="{ax}" cy="{y}" r="{r+3}" fill="{C["bg"]}"/>')
        b.append(f'<circle cx="{ax}" cy="{y}" r="{r}" fill="{col}" stroke="#fff" stroke-width="1.6"/>')
        b.append(txt(ax - 16, y + 4.5, str(yr), 11.6, C["ink"], "end", "bold" if imp >= 2 else "normal"))
        b.append(txt(ax + 18, y - 1, title, 11.8 if imp >= 2 else 11.2, C["ink"], "start",
                     "bold" if imp >= 2 else "normal"))
        b.append(txt(ax + 18, y + 14, desc[:96], 9.8, C["mut"]))
    b.append(legend(ax + 500, H - 44, [(C["e0"], "최대 전환점"), (C["e1"], "주요 전환점"),
                                       (C["acc"], "중요 진전"), (C["e3"], "배경 흐름")], 9.6, gap=13, box=9))
    b.append(txt(20, H - 16, "연도는 해당 성과가 처음 공개 보고된 해를 기준으로 한다.", 10, C["faint"]))
    return svg(W, H, "".join(b), "기술 계보 연표")


def fig_supply(cats):
    """공급 구조 도식. cats=[(카테고리, 건수, 가격확인건수, 한줄 리스크)]"""
    W = 880
    H = 106 + len(cats) * 52 + 74
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "카테고리별 공급 현황과 조달 리스크", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "막대는 본 조사에서 공급 정보를 확인한 품목 수이고, 진한 부분은 공개 카탈로그에서 가격까지 확인된 품목이다.",
                 10.4, C["mut"], "middle"))
    b.append(legend(300, 68, [(C["acc"], "가격까지 확인"), (C["line"], "품목만 확인")], 9.8, horiz=True, box=9))
    x_lab, x_bar, bw = 214, 224, 300
    mx = max([c[1] for c in cats] + [1])
    y = 104
    for name, n, npx, risk in cats:
        b.append(txt(x_lab - 6, y + 14, name, 11.2, C["ink"], "end", "bold"))
        w = (n / mx) * bw
        wp = (npx / mx) * bw
        b.append(rect(x_bar, y + 4, w, 20, C["line"], rx=4, op=0.5))
        b.append(rect(x_bar, y + 4, wp, 20, C["acc"], rx=4, op=0.82))
        b.append(txt(x_bar + w + 9, y + 18, f"{n}건 (가격 {npx})", 10, C["mut"], "start", "bold"))
        b.append(txt(x_bar, y + 40, "리스크: " + risk[:74], 9.6, C["e1"]))
        y += 52
    b.append(rect(30, H - 58, W - 60, 46, C["e1"], rx=8, op=0.08))
    b.append(rect(30, H - 58, 4.5, 46, C["e1"], rx=2))
    b.append(txt(46, H - 40, "가격 정보의 한계", 11, C["ink"], "start", "bold"))
    b.append(txt(46, H - 25, "여기의 가격은 모두 공개 카탈로그 기준이며 대량 구매·계약 단가와는 다르다. 의약품 제조 등급 품목은",
                 10.1, C["mut"]))
    b.append(txt(46, H - 12, "애초에 공개 가격을 두지 않고 견적으로만 거래되는 경우가 많아, 표에 '가격 미표시'로 남은 항목이 적지 않다.",
                 10.1, C["mut"]))
    return svg(W, H, "".join(b), "카테고리별 공급 현황 도식")


def fig_summary(findings):
    """핵심 결론 요약 도식. findings=[(번호, 제목, 한줄, 등급색키)]"""
    W = 880
    H = 92 + len(findings) * 64 + 30
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 26, "이 보고서의 핵심 발견", 16, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 46, "각 항목은 본문의 해당 장에서 근거 문헌과 함께 다룬다. 오른쪽 표시는 그 결론을 지지하는 근거의 강도다.",
                 10.4, C["mut"], "middle"))
    y = 72
    for i, (num, title, one, ck) in enumerate(findings):
        col = C.get(ck, C["acc"])
        b.append(rect(24, y, W - 48, 56, SURF, rx=9, stroke=C["line"]))
        b.append(rect(24, y, 4.5, 56, col, rx=2))
        b.append(f'<circle cx="{56}" cy="{y+28}" r="15" fill="{col}" opacity="0.16"/>')
        b.append(txt(56, y + 33, str(num), 15, col, "middle", "bold"))
        b.append(txt(84, y + 22, title, 12.4, C["ink"], "start", "bold"))
        b.append(txt(84, y + 40, one[:104], 10.4, C["mut"]))
        y += 64
    return svg(W, H, "".join(b), "핵심 결론 요약 도식")
