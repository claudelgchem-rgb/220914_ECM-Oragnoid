# -*- coding: utf-8 -*-
"""ECMX-004 보고서 조립."""
import collections, csv, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import page2, tables4, text4
import report_base2 as B
import figs4_concept as FC
import figs4_data as FD
import figs4_extra as FE
import figs4_mat as FM

BASE = "/mnt/user-data/outputs/ECMX4"
META = json.load(open(os.path.join(BASE, "tools", "citemeta4.json"), encoding="utf-8"))
DATE = "2026-09-16"


def load(fn):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


class Ctx:
    def __init__(self):
        self.refs = B.Refs()
        self._meta = META
        self.fig_n = 0
        self.tab_n = 0
        self.scaf = load("scaffold_bom.csv")
        self.par = load("rc_params.csv")
        self.med = load("medium_bom.csv")
        self.delta = load("medium_delta.csv")

    def fig(self, svg, title, source, note=""):
        self.fig_n += 1
        return B.figure(svg, self.fig_n, title, source, note)

    def tab(self):
        self.tab_n += 1
        return self.tab_n

    def layer(self, L):
        return [r for r in self.scaf if (r.get("layer") or "").strip().upper() == L]

    def cat(self, *cs):
        return [r for r in self.med if (r.get("category") or "").strip() in cs]

    def nec(self, rows, n):
        return sum(1 for r in rows if (r.get("necessity") or "").strip() == n)


def build():
    c = Ctx()
    pg = page2.Page(
        "재조합 콜라겐 지지체 명세",
        "재조합 인간 콜라겐 세 가지(I형 단일사슬 · III형 단일사슬 · III형 삼중나선)만으로 "
        "오가노이드 지지체를 세우고 배지를 직접 조제할 때, 층위별로 무엇이 필수이고 "
        "무엇이 조건부인지를 논문·특허 근거로 정리한 명세서")
    text4.write(pg, c, tables4, FC, FD, FE, FM)

    pg.h2("참고문헌", "refs")
    npap, npat = c.refs.count()
    pg.p(f"본문에서 인용한 논문 {npap}편, 특허 {npat}건. 번호는 본문 등장 순서이며, "
         f"각 항목 끝의 ↩ 를 누르면 인용 위치로 돌아간다.")
    pg.raw(c.refs.render())

    out = os.path.join(BASE, "ECMX004_report.html")
    open(out, "w", encoding="utf-8").write(pg.render(fonts=False))
    art = os.path.join(BASE, "ECMX004_report_artifact.html")
    open(art, "w", encoding="utf-8").write(pg.render(fonts=True))
    print(f"작성: {out} ({os.path.getsize(out):,} B) · 그림 {c.fig_n} · 표 {c.tab_n} · "
          f"논문 {npap} · 특허 {npat}")
    return c


if __name__ == "__main__":
    build()
