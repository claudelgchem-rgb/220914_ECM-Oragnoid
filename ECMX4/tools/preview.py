# -*- coding: utf-8 -*-
"""도판 육안 검수용 미리보기 HTML 생성."""
import sys, importlib, style2

def build(figs, out="/tmp/claude-0/prev.html"):
    parts = []
    for name, svg in figs:
        parts.append(f'<h3 style="font:600 13px IBM Plex Mono,monospace;color:#4E5C68">{name}</h3>'
                     f'<figure>{svg}</figure>')
    html = ("<!DOCTYPE html><html lang=ko><head><meta charset=utf-8>"
            "<meta name=viewport content='width=device-width,initial-scale=1'>"
            + style2.FONTS + "<style>" + style2.CSS +
            "main{max-width:960px;margin:0 auto;padding:24px}</style></head>"
            "<body><main>" + "".join(parts) + "</main></body></html>")
    open(out, "w", encoding="utf-8").write(html)
    return out
