# -*- coding: utf-8 -*-
"""ECMX-003 보고서 조립.

이 파일은 '틀'만 갖는다. 문장은 text2.py, 표는 tables2.py, 그림은 figs3_*.py에 있다.
한 파일에 다 넣으면 11만 줄짜리 build_report.py가 또 나오기 때문이다(ECMX-002의 실물).
"""
import collections, csv, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import page2, tables2, text2
import report_base2 as B
import figs3_concept as FC
import figs3_data as FD
import figs3_extra as FE

BASE = "/mnt/user-data/outputs/ECMX2"
META = json.load(open(os.path.join(BASE, "tools", "citemeta3.json"), encoding="utf-8"))

DATE = "2026-09-16"
RUN = "ECMX-003"


def load(fn):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


class Ctx:
    """조립 중 공유하는 상태 — 각주·그림번호·표번호."""

    def __init__(self):
        self.refs = B.Refs()
        self._meta = META
        self.fig_n = 0
        self.tab_n = 0
        self.scaf = load("scaffold_bom.csv")
        self.par = load("collagen_params.csv")
        self.med = load("medium_bom.csv")
        self.mat = load("medium_matrix.csv")

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

    def nec_count(self, rows, n):
        return sum(1 for r in rows if (r.get("necessity") or "").strip() == n)


def build():
    c = Ctx()
    pg = page2.Page(
        "콜라겐 지지체와 배지 명세",
        "콜라겐 I형·III형을 구조 단백질로 쓴다는 전제에서, L1~L9 각 층위와 배지 조성에 "
        "무엇이 필수이고 무엇이 조건부인지를 논문·특허 근거로 정리한 명세서")
    text2.write(pg, c, tables2, FC, FD, FE)

    # 참고문헌
    pg.h2("참고문헌", "refs")
    npap, npat = c.refs.count()
    pg.p(f"본문에서 인용한 논문 {npap}편, 특허 {npat}건. 번호는 본문 등장 순서이며, "
         f"각 항목 끝의 ↩ 표시를 누르면 인용 위치로 돌아간다.")
    pg.raw(c.refs.render())

    out = os.path.join(BASE, "ECMX003_report.html")
    open(out, "w", encoding="utf-8").write(pg.render(fonts=False))
    art = os.path.join(BASE, "ECMX003_report_artifact.html")
    open(art, "w", encoding="utf-8").write(pg.render(fonts=True))
    print(f"작성: {out} ({os.path.getsize(out):,} B) · 그림 {c.fig_n} · 표 {c.tab_n} · "
          f"논문 {npap} · 특허 {npat}")
    return c


if __name__ == "__main__":
    build()
