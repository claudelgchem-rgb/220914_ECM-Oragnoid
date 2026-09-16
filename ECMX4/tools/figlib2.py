# -*- coding: utf-8 -*-
"""ECMX-003 그림 라이브러리 (R-14: 전 도판 자체 제작).

ECMX-002의 figlib은 '근거 등급(E0~E3)'을 칠하는 팔레트였다. 이 보고서는
등급이 아니라 **구매 결정**을 그린다. 그래서 축이 둘이다.
  1) 계통 — 지지체(청록) vs 배지(자주). 이 둘을 섞는 것이 이 분야 최빈 오류다.
  2) 필수도 — 필수 / 조건부 / 선택 / 미사용.
색만으로 구분하지 않는다. 필수도는 반드시 글자나 패턴을 함께 싣는다.
"""
import math, html

C = {
    # 계통
    "mx": "#0E6B5E", "mx_bg": "#E6F2EF", "mx_ln": "#7FBDB1",
    "md": "#6B3FA0", "md_bg": "#F0EAF8", "md_ln": "#B49ADA",
    # 필수도
    "req": "#0B5E52", "req_bg": "#CFE7E1",
    "cnd": "#B87A14", "cnd_bg": "#FBEED5",
    "opt": "#63737F", "opt_bg": "#E7ECEF",
    "non": "#A7B3BD", "non_bg": "#F1F4F6",
    # 지면
    "ink": "#121A20", "mut": "#4E5C68", "faint": "#8494A1",
    "line": "#D7E0E5", "line2": "#AFBCC5", "bg": "#FFFFFF",
    "bad": "#9B2226", "warn": "#8A5A00", "ok": "#1B6B47",
}

N_FILL = {"필수": "url(#nReq)", "조건부": "url(#nCnd)", "선택": "url(#nOpt)", "미사용": "url(#nNon)"}
N_SOLID = {"필수": C["req"], "조건부": C["cnd"], "선택": C["opt"], "미사용": C["non"]}
N_TXT = {"필수": "#FFFFFF", "조건부": "#FFFFFF", "선택": "#FFFFFF", "미사용": C["ink"]}

DEFS = """
<defs>
 <pattern id="nReq" width="7" height="7" patternUnits="userSpaceOnUse">
   <rect width="7" height="7" fill="%(req)s"/></pattern>
 <pattern id="nCnd" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
   <rect width="7" height="7" fill="%(cnd)s"/>
   <line x1="0" y1="0" x2="0" y2="7" stroke="#fff" stroke-width="2.2" opacity=".55"/></pattern>
 <pattern id="nOpt" width="7" height="7" patternUnits="userSpaceOnUse">
   <rect width="7" height="7" fill="%(opt_bg)s"/>
   <circle cx="3.5" cy="3.5" r="1.3" fill="%(opt)s" opacity=".85"/></pattern>
 <pattern id="nNon" width="7" height="7" patternUnits="userSpaceOnUse">
   <rect width="7" height="7" fill="%(non_bg)s"/></pattern>
 <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
   <path d="M0 0 L10 5 L0 10 z" fill="%(mut)s"/></marker>
 <marker id="arMx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
   <path d="M0 0 L10 5 L0 10 z" fill="%(mx)s"/></marker>
 <marker id="arMd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
   <path d="M0 0 L10 5 L0 10 z" fill="%(md)s"/></marker>
</defs>""" % C


def esc(s):
    return html.escape(str(s), quote=True)


def svg(w, h, body, label=""):
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" preserveAspectRatio="xMidYMid meet" '
            f'role="img" aria-label="{esc(label)}" xmlns="http://www.w3.org/2000/svg" '
            f'style="max-width:100%;height:auto;'
            f'font-family:\'IBM Plex Sans KR\',system-ui,-apple-system,sans-serif">'
            + DEFS + body + '</svg>')


def txt(x, y, s, size=12, fill=None, anchor="start", weight="400", op=1.0,
        ital=False, mono=False, ls=None):
    f = ' font-family="IBM Plex Mono,ui-monospace,monospace"' if mono else ''
    i = ' font-style="italic"' if ital else ''
    l = f' letter-spacing="{ls}"' if ls else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill or C["ink"]}" '
            f'text-anchor="{anchor}" font-weight="{weight}" opacity="{op}"{f}{i}{l}>{esc(s)}</text>')


def rect(x, y, w, h, fill, rx=3, stroke=None, sw=1, op=1.0, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(0,w):.1f}" height="{max(0,h):.1f}" '
            f'rx="{rx}" fill="{fill}"{s}{d} opacity="{op}"/>')


def line(x1, y1, x2, y2, stroke=None, sw=1, dash=None, op=1.0, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = f' marker-end="url(#{marker})"' if marker else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke or C["line2"]}" stroke-width="{sw}"{d}{m} opacity="{op}"/>')


def path(d, fill="none", stroke=None, sw=1.5, dash=None, op=1.0, marker=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    m = f' marker-end="url(#{marker})"' if marker else ''
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke or C["ink"]}" stroke-width="{sw}"{ds}{m} '
            f'opacity="{op}" stroke-linejoin="round" stroke-linecap="round"/>')


def circ(cx, cy, r, fill, stroke=None, sw=1, op=1.0):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{s} opacity="{op}"/>'


def chip(x, y, label, kind="필수", size=10.5, pad=6, h=17):
    """필수도 배지 — 색과 글자를 항상 함께."""
    w = len(label) * (size * 0.98) + pad * 2
    return (rect(x, y, w, h, N_SOLID.get(kind, C["opt"]), rx=h / 2)
            + txt(x + w / 2, y + h - 5, label, size, N_TXT.get(kind, "#fff"),
                  "middle", "600"), w)


def wrap(x, y, s, size=11, width=26, lh=14, fill=None, anchor="start", weight="400",
         maxlines=8, mono=False):
    """한글 기준 글자 수 줄바꿈. 끊을 자리가 없으면 강제로 끊는다."""
    lines, cur = [], ""
    for ch in str(s):
        cur += ch
        if len(cur) >= width:
            if ch in " ,·/)]+":
                lines.append(cur); cur = ""
            elif len(cur) >= width + 6:
                lines.append(cur); cur = ""
    if cur:
        lines.append(cur)
    out = []
    for i, l in enumerate(lines[:maxlines]):
        out.append(txt(x, y + i * lh, l.strip(), size, fill, anchor, weight, mono=mono))
    return "".join(out), len(lines[:maxlines])


def legend(x, y, items, size=11, gap=17, horiz=False, box=12, step=None):
    """items: [(fill, label)]"""
    out = []
    for i, (f, lab) in enumerate(items):
        dx = x + (i * (step or 130) if horiz else 0)
        dy = y + (0 if horiz else i * gap)
        out.append(rect(dx, dy - box + 2, box, box, f, rx=2.5, stroke=C["line2"]))
        out.append(txt(dx + box + 6, dy, lab, size, C["mut"]))
    return "".join(out)


def axis_x(x0, x1, y, ticks, fmt=lambda v: str(v), scale=None, size=9.5, tickup=4):
    """ticks: [값]. scale: 값→x 함수."""
    out = [line(x0, y, x1, y, C["line2"], 1)]
    for v in ticks:
        X = scale(v)
        out.append(line(X, y, X, y + tickup, C["line2"], 1))
        out.append(txt(X, y + tickup + 10, fmt(v), size, C["faint"], "middle", mono=True))
    return "".join(out)


def logscale(lo, hi, x0, w):
    l0, l1 = math.log10(lo), math.log10(hi)
    return lambda v: x0 + (math.log10(max(v, lo * 1e-6)) - l0) / (l1 - l0) * w


def decades(lo, hi):
    out, e = [], int(math.floor(math.log10(lo)))
    while 10 ** e <= hi * 1.001:
        if 10 ** e >= lo * 0.999:
            out.append(10 ** e)
        e += 1
    return out


def fmt_si(v, unit=""):
    a = abs(v)
    if a == 0: return "0" + unit
    for d, s in ((1e9, "G"), (1e6, "M"), (1e3, "k"), (1, ""), (1e-3, "m"), (1e-6, "µ"), (1e-9, "n")):
        if a >= d:
            q = v / d
            return (f"{q:g}{s}{unit}")
    return f"{v:g}{unit}"


def title(x, y, main, sub=None, size=13):
    out = txt(x, y, main, size, C["ink"], weight="600")
    if sub:
        out += txt(x, y + 15, sub, 10.5, C["faint"])
    return out


def nodata(x, y, w, h, msg="정량 근거 없음"):
    """근거가 없는 구간은 비워 두지 않고 그렇게 적는다 (R-04)."""
    return (rect(x, y, w, h, "none", rx=4, stroke=C["line2"], sw=1, dash="4 3")
            + txt(x + w / 2, y + h / 2 + 4, msg, 10, C["faint"], "middle", ital=True))


def logticks(lo, hi, dense=None):
    """로그축 눈금. 범위가 좁으면 1·2·3·5 배수까지 내려간다.

    decades()만 쓰면 0.7~8 같은 구간에서 눈금이 하나만 남아 축이 축 노릇을 못 한다.
    """
    span = math.log10(hi) - math.log10(lo)
    mult = (1, 2, 3, 5) if (dense if dense is not None else span < 2.2) else (1,)
    out, e = [], int(math.floor(math.log10(lo)))
    while 10 ** e <= hi * 1.001:
        for m in mult:
            v = m * 10 ** e
            if lo * 0.999 <= v <= hi * 1.001:
                out.append(v)
        e += 1
    return out
