# -*- coding: utf-8 -*-
"""보고서 조립 기반 — 각주 관리, 표 생성, 배지, 목차."""
import csv, html, os, re

BASE = "/mnt/user-data/outputs/ECMX"


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=False)


class Refs:
    """각주 번호 관리. 본문 [n] ↔ 부록 B 항목 1:1 대응(G9 조건)."""
    def __init__(self):
        self.order = []      # key 순서
        self.meta = {}       # key -> dict
        self.uses = {}       # key -> [본문 앵커 id]

    def cite(self, key, **meta):
        """key: DOI 또는 특허번호. 반환: <sup> 각주 마크업"""
        key = str(key).strip()
        if key not in self.meta:
            self.order.append(key)
            self.meta[key] = meta
            self.uses[key] = []
        elif meta:
            for k, v in meta.items():
                self.meta[key].setdefault(k, v)
        n = self.order.index(key) + 1
        uid = f"cite-{n}-{len(self.uses[key])+1}"
        self.uses[key].append(uid)
        return (f'<sup class="fn"><a id="{uid}" href="#ref-{n}" '
                f'title="{html.escape(self.meta[key].get("title","")[:150], quote=True)}">[{n}]</a></sup>')

    def many(self, *keys):
        return "".join(self.cite(k) for k in keys)

    def render(self):
        out = ['<ol class="reflist">']
        for i, k in enumerate(self.order, 1):
            m = self.meta[k]
            bits = []
            if m.get("authors"): bits.append(esc(m["authors"]))
            if m.get("title"): bits.append(f'<b>{esc(m["title"])}</b>')
            if m.get("journal"): bits.append(f'<i>{esc(m["journal"])}</i>')
            if m.get("year"): bits.append(esc(m["year"]))
            ident = []
            if m.get("kind") == "patent":
                ident.append(f'특허 {esc(k)}')
                if m.get("assignee"): ident.append(f'출원인 {esc(m["assignee"])}')
                if m.get("filedate"): ident.append(f'출원일 {esc(m["filedate"])}')
            else:
                ident.append(f'DOI {esc(k)}')
                if m.get("pmid"): ident.append(f'PMID {esc(m["pmid"])}')
            if m.get("ft"): ident.append("전문 확인")
            if m.get("note"): ident.append(esc(m["note"]))
            body = ". ".join(b for b in bits if b)
            backs = "".join(f'<a class="back" href="#{u}">↩{j+1 if len(self.uses[k])>1 else ""}</a>'
                            for j, u in enumerate(self.uses[k]))
            out.append(f'<li class="ref" id="ref-{i}" value="{i}">{body}. '
                       f'<span class="nw">{" · ".join(ident)}</span> {backs}</li>')
        out.append("</ol>")
        return "\n".join(out)

    def count(self):
        p = sum(1 for k in self.order if self.meta[k].get("kind") == "patent")
        return len(self.order) - p, p


def badge(grade, reason):
    g = (grade or "").strip()
    if g not in ("상", "중", "하"):
        return ""
    return f'<span class="b b-{g}" title="{html.escape(str(reason)[:260], quote=True)}">신뢰도 {g}</span>'


def tier(t):
    t = (t or "").strip()[:2]
    if t not in ("E0", "E1", "E2", "E3"):
        return esc(t)
    nm = {"E0": "절대필수", "E1": "조건부", "E2": "선택", "E3": "대체가능"}[t]
    return f'<span class="t t-{t}">{t} {nm}</span>'


def table(cols, rows, caption="", align=None, cls=""):
    """cols: [열이름]; rows: [[셀…]] (셀은 이미 HTML 허용)"""
    a = align or [""] * len(cols)
    h = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = []
    for r in rows:
        tds = []
        for j, c in enumerate(r):
            k = f' class="{a[j]}"' if j < len(a) and a[j] else ""
            tds.append(f"<td{k}>{c}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    cap = f'<div class="cap">{caption}</div>' if caption else ""
    return (f'<div class="tw {cls}"><table><thead><tr>{h}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>{cap}')


def figure(svg, num, title, source, conf=""):
    c = f' {badge(conf, source)}' if conf else ""
    return (f'<figure><div>{svg}</div>'
            f'<figcaption><b>그림 {num}. {esc(title)}</b><br>'
            f'데이터 출처: {source}{c}</figcaption></figure>')


def read_csv(fn):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def md_section(fn, start_pat, end_pat=None, maxlen=None):
    """산출 .md에서 구간 추출(참고용)."""
    p = os.path.join(BASE, fn)
    if not os.path.exists(p): return ""
    t = open(p, encoding="utf-8").read()
    m = re.search(start_pat, t)
    if not m: return ""
    s = m.start()
    e = len(t)
    if end_pat:
        m2 = re.search(end_pat, t[m.end():])
        if m2: e = m.end() + m2.start()
    out = t[s:e]
    return out[:maxlen] if maxlen else out
