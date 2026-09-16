# -*- coding: utf-8 -*-
"""ECMX-003 페이지 셸 — 목차·표지·본문 틀.

외부 리소스는 폰트 한 줄뿐이고, 그마저도 없어도 읽히게 시스템 폰트를 뒤에 세워 둔다.
"""
import html, re
import style2


def esc(s):
    return html.escape(str(s or ""), quote=False)


class Page:
    def __init__(self, title, subtitle=""):
        self.title = title
        self.subtitle = subtitle
        self.parts = []
        self.toc = []          # (level, id, label)

    def h2(self, label, hid, cls="", tag=""):
        self.toc.append((1, hid, label))
        c = f' class="{cls}"' if cls else ""
        t = f'<span class="tag">{esc(tag)}</span> ' if tag else ""
        self.parts.append(f'<h2 id="{hid}"{c}>{t}{esc(label)}</h2>')

    def h3(self, label, hid):
        self.toc.append((2, hid, label))
        self.parts.append(f'<h3 id="{hid}">{esc(label)}</h3>')

    def h4(self, label):
        self.parts.append(f'<h4>{esc(label)}</h4>')

    def p(self, htmltext):
        self.parts.append(f'<p>{htmltext}</p>')

    def raw(self, s):
        self.parts.append(s)

    def hr(self):
        self.parts.append("<hr>")

    def _toc_html(self):
        out = ['<nav id="toc" aria-label="목차"><h2>목차</h2><div class="toclist">']
        for lv, hid, lab in self.toc:
            cls = "lv2" if lv == 2 else ""
            out.append(f'<a class="{cls}" href="#{hid}">{esc(lab)}</a>')
        out.append("</div></nav>")
        return "".join(out)

    def render(self, fonts=True, lang="ko"):
        head = [
            '<!DOCTYPE html>', f'<html lang="{lang}">', '<head>',
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
            f'<title>{esc(self.title)}</title>',
            f'<meta name="description" content="{html.escape(self.subtitle, quote=True)}">',
            '<meta name="color-scheme" content="light dark">',
        ]
        if fonts:
            head.append(style2.FONTS)
        head += ['<style>', style2.CSS, '</style>', '</head>', '<body>']
        body = ['<button id="tocBtn" aria-expanded="true" aria-controls="toc">▾ 목차 접기</button>',
                '<div class="wrap">', self._toc_html(),
                '<main>', "".join(self.parts), '</main>', '</div>',
                '<script>', style2.JS, '</script>', '</body>', '</html>']
        return "\n".join(head + body)


def cover(kicker, title, lede, meta_pairs, cards=None):
    o = [f'<header class="cover"><div class="kicker">{esc(kicker)}</div>',
         f'<h1>{esc(title)}</h1>', f'<div class="lede">{lede}</div>']
    if meta_pairs:
        o.append('<div class="meta">' + " · ".join(
            f'<span><b>{esc(k)}</b> {esc(v)}</span>' for k, v in meta_pairs) + '</div>')
    o.append('</header>')
    if cards:
        o.append('<div class="grid">')
        for k, v, d in cards:
            o.append(f'<div class="card"><div class="k">{esc(k)}</div>'
                     f'<div class="v">{esc(v)}</div><div class="d">{d}</div></div>')
        o.append('</div>')
    return "".join(o)
