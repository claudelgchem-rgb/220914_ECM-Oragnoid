#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ECMX 보고서용 인라인 SVG 그림 라이브러리 (R-14: 전부 자체 제작, 외부 도판 복제 금지).

설계 원칙
- 색은 5색 이내 + 범례 필수. 색맹 대응을 위해 패턴·라벨 병행.
- 근거 없는 수치는 그리지 않는다. 근거가 없으면 '정량 근거 없음' 구간으로 표시.
- 모든 좌표는 뷰박스 기준. 반응형을 위해 width=100%, preserveAspectRatio 지정.
- 다크모드에서도 읽히도록 색은 CSS 변수로 빼지 않고, 명도 대비가 충분한 고정색 + 배경 무관 스트로크 사용.
"""
import math, html

# 5색 팔레트 (색맹 대응: 명도 차이를 크게)
C = {
    "e0": "#B3261E",   # 진한 적 — E0 절대필수
    "e1": "#E8710A",   # 주황 — E1 조건부
    "e2": "#F2C744",   # 노랑 — E2 선택
    "e3": "#BFC6CC",   # 회색 — E3 대체가능/근거없음
    "ink": "#1F2933",
    "mut": "#6B7785",
    "line": "#C3CBD3",
    "acc": "#2C5F8D",   # 강조 청
    "bg": "#FFFFFF",
    "surface": "#FFFFFF",
    "line2": "#9AA5AF",
    "faint": "#8B96A1",
}
# E0~E3 패턴 id (색맹 대응)
PATTERNS = """
<defs>
 <pattern id="pE0" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
   <rect width="6" height="6" fill="%(e0)s"/><line x1="0" y1="0" x2="0" y2="6" stroke="#fff" stroke-width="2.4" opacity=".55"/></pattern>
 <pattern id="pE1" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
   <rect width="6" height="6" fill="%(e1)s"/><line x1="0" y1="0" x2="0" y2="6" stroke="#fff" stroke-width="1.8" opacity=".5"/></pattern>
 <pattern id="pE2" width="6" height="6" patternUnits="userSpaceOnUse">
   <rect width="6" height="6" fill="%(e2)s"/><circle cx="3" cy="3" r="1.1" fill="#fff" opacity=".65"/></pattern>
 <pattern id="pE3" width="6" height="6" patternUnits="userSpaceOnUse">
   <rect width="6" height="6" fill="%(e3)s"/></pattern>
</defs>""" % C

TIER_FILL = {"E0": "url(#pE0)", "E1": "url(#pE1)", "E2": "url(#pE2)", "E3": "url(#pE3)"}
TIER_SOLID = {"E0": C["e0"], "E1": C["e1"], "E2": C["e2"], "E3": C["e3"]}
TIER_TXT = {"E0": "#FFFFFF", "E1": "#FFFFFF", "E2": "#1F2933", "E3": "#1F2933"}


def esc(s):
    return html.escape(str(s), quote=True)


def svg(w, h, body, label=""):
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" preserveAspectRatio="xMidYMid meet" '
            f'role="img" aria-label="{esc(label)}" xmlns="http://www.w3.org/2000/svg" '
            f'style="max-width:100%;height:auto;font-family:system-ui,-apple-system,\'Malgun Gothic\',sans-serif">'
            + PATTERNS + body + '</svg>')


def txt(x, y, s, size=12, fill=None, anchor="start", weight="normal", op=1.0, ital=False):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill or C["ink"]}" '
            f'text-anchor="{anchor}" font-weight="{weight}" opacity="{op}"'
            + (' font-style="italic"' if ital else '') + f'>{esc(s)}</text>')


def rect(x, y, w, h, fill, rx=3, stroke=None, sw=1, op=1.0):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{max(0,w)}" height="{max(0,h)}" rx="{rx}" fill="{fill}"{s} opacity="{op}"/>'


def line(x1, y1, x2, y2, stroke=None, sw=1, dash=None, op=1.0):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke or C["line"]}" '
            f'stroke-width="{sw}"{d} opacity="{op}"/>')


def path(d, fill="none", stroke=None, sw=1.5, dash=None, op=1.0):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke or C["ink"]}" stroke-width="{sw}"{ds} '
            f'opacity="{op}" stroke-linejoin="round" stroke-linecap="round"/>')


def wrap(x, y, s, size=11, width=30, lh=15, fill=None, anchor="start", weight="normal"):
    """한글 줄바꿈 — width는 글자 수 기준."""
    out, cur, lines = [], "", []
    for ch in str(s):
        cur += ch
        if len(cur) >= width and ch in " ,·/)]":
            lines.append(cur); cur = ""
    if cur: lines.append(cur)
    for i, l in enumerate(lines[:6]):
        out.append(txt(x, y + i * lh, l.strip(), size, fill, anchor, weight))
    return "".join(out)


def legend(x, y, items, size=11, gap=15, horiz=False, box=11):
    """items: [(색 또는 url(#p), 라벨)]"""
    out = []
    for i, (f, lab) in enumerate(items):
        dx = x + (i * 150 if horiz else 0)
        dy = y + (0 if horiz else i * gap)
        out.append(rect(dx, dy - box + 2, box, box, f, rx=2, stroke=C["line"]))
        out.append(txt(dx + box + 5, dy, lab, size, C["ink"]))
    return "".join(out)


def logticks(lo, hi, w, x0):
    """로그 스케일 눈금 위치 계산. lo/hi 단위 Pa."""
    l0, l1 = math.log10(lo), math.log10(hi)
    def X(v): return x0 + (math.log10(v) - l0) / (l1 - l0) * w
    ticks = []
    e = int(math.floor(l0))
    while e <= math.ceil(l1):
        for m in (1, 3):
            v = m * 10 ** e
            if lo <= v <= hi: ticks.append(v)
        e += 1
    return X, ticks


def fmt_pa(v):
    if v >= 1e6: return f"{v/1e6:g} MPa"
    if v >= 1e3: return f"{v/1e3:g} kPa"
    return f"{v:g} Pa"
