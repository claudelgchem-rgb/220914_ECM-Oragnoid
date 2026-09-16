# -*- coding: utf-8 -*-
"""ECMX-003 보고서 조립 기반.

ECMX-002의 report_base와 다른 점은 배지 체계다. 저기서는 '근거 등급'이 주인공이었고
여기서는 '사느냐 마느냐'가 주인공이다. 그래서 필수도 배지(필수/조건부/선택/미사용)와
계통 배지(지지체/배지)를 1급 시민으로 둔다. 근거 등급은 필수도 판정의 *사유*로
따라붙는 부차 정보다.
"""
import csv, html, os, re

BASE = "/mnt/user-data/outputs/ECMX2"

NEC = ("필수", "조건부", "선택", "미사용")
# CSS 클래스는 한글 그대로 쓴다 — 별도 매핑을 두면 둘이 어긋날 자리가 생긴다.
TIER_NM = {"E0": "절대필수", "E1": "조건부", "E2": "성능", "E3": "대체가능"}


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=False)


def attr(s):
    return html.escape(str(s if s is not None else ""), quote=True)


class Refs:
    """각주 번호 관리. 본문 [n] ↔ 참고문헌 n 1:1."""

    def __init__(self):
        self.order, self.meta, self.uses = [], {}, {}

    def cite(self, key, **meta):
        key = str(key).strip()
        if not key:
            return ""
        if key not in self.meta:
            self.order.append(key)
            self.meta[key] = dict(meta)
            self.uses[key] = []
        elif meta:
            for k, v in meta.items():
                if v:
                    self.meta[key].setdefault(k, v)
        n = self.order.index(key) + 1
        uid = f"c{n}-{len(self.uses[key]) + 1}"
        self.uses[key].append(uid)
        t = self.meta[key].get("title", "")[:160]
        return (f'<sup class="fn"><a id="{uid}" href="#ref-{n}" title="{attr(t)}">{n}</a></sup>')

    def many(self, *keys):
        return "".join(self.cite(k) for k in keys)

    def render(self):
        out = ['<ol class="reflist">']
        for i, k in enumerate(self.order, 1):
            m = self.meta[k]
            bits = []
            if m.get("authors"):
                bits.append(esc(m["authors"]))
            if m.get("title"):
                bits.append(f'<b>{esc(m["title"])}</b>')
            if m.get("journal"):
                bits.append(f'<i>{esc(m["journal"])}</i>')
            if m.get("year"):
                bits.append(esc(m["year"]))
            ident = []
            if m.get("kind") == "patent":
                ident.append(f'특허 {esc(k)}')
                if m.get("assignee"):
                    ident.append(f'출원인 {esc(m["assignee"])}')
            else:
                ident.append(f'DOI {esc(k)}')
                if m.get("pmid"):
                    ident.append(f'PMID {esc(m["pmid"])}')
            if m.get("ft"):
                ident.append("전문 확인")
            if m.get("note"):
                ident.append(esc(m["note"]))
            backs = "".join(
                f'<a class="back" href="#{u}">↩{j + 1 if len(self.uses[k]) > 1 else ""}</a>'
                for j, u in enumerate(self.uses[k]))
            out.append(f'<li class="ref" id="ref-{i}" value="{i}">'
                       f'{". ".join(b for b in bits if b)}. '
                       f'<span class="nw">{" · ".join(ident)}</span> {backs}</li>')
        out.append("</ol>")
        return "\n".join(out)

    def count(self):
        p = sum(1 for k in self.order if self.meta[k].get("kind") == "patent")
        return len(self.order) - p, p


def nec(v, why=""):
    """필수도 배지."""
    v = (v or "").strip()
    if v not in NEC:
        return esc(v)
    t = f' title="{attr(why)}"' if why else ""
    return f'<span class="n n-{v}"{t}>{v}</span>'


def sysb(kind):
    """계통 배지 — 지지체/배지."""
    k = (kind or "").strip()
    if k.startswith("지지체") or k in ("MX", "매트릭스"):
        return '<span class="sys sys-mx">지지체</span>'
    if k.startswith("배지") or k == "MD":
        return '<span class="sys sys-md">배지</span>'
    return ""


def tier(t):
    t = (t or "").strip()[:2]
    if t not in TIER_NM:
        return esc(t)
    return f'<span class="b b-{t}" title="근거 등급">{t}</span>'


def table(cols, rows, caption="", align=None, cls="", num=None, widths=None):
    a = align or [""] * len(cols)
    h = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = []
    for r in rows:
        tds = []
        for j, c in enumerate(r):
            k = f' class="{a[j]}"' if j < len(a) and a[j] else ""
            tds.append(f"<td{k}>{c}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    cap = ""
    if caption:
        lab = f"<b>표 {num}.</b> " if num else ""
        cap = f'<div class="cap">{lab}{caption}</div>'
    cg = ("<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
          ) if widths else ""
    return (f'<div class="tw {cls}"><table>{cg}<thead><tr>{h}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>{cap}')


def figure(svg, num, title, source, note=""):
    n = f'<br><span class="fnote">{note}</span>' if note else ""
    return (f'<figure id="fig{num}"><div class="figbox">{svg}</div>'
            f'<figcaption><b>그림 {num}. {esc(title)}</b><br>'
            f'출처: {source}{n}</figcaption></figure>')


def steps(items, cls=""):
    """조리법형 단계 목록. items: [(제목, 본문HTML)]"""
    li = "".join(f'<li><b>{esc(t)}</b><div>{b}</div></li>' for t, b in items)
    return f'<ol class="steps {cls}">{li}</ol>'


def box(title, body, kind=""):
    k = f" {kind}" if kind else ""
    return f'<div class="box{k}"><b>{esc(title)}</b>{body}</div>'


def read_csv(fn):
    p = fn if os.path.isabs(fn) else os.path.join(BASE, fn)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def q(v, unit=""):
    """수치는 반드시 모노스페이스로. 단위 없는 수치는 이 보고서에서 오류다."""
    if v is None or str(v).strip() == "":
        return '<span class="na">—</span>'
    return f'<span class="q">{esc(v)}{esc(unit)}</span>'


# ── ECMX-004 추가 ────────────────────────────────────────────
MATS = ("A", "B", "C")
MAT_NAME = {"A": "I형 단일사슬", "B": "III형 단일사슬", "C": "III형 삼중나선"}
MAT_FORM = {"A": "단일사슬", "B": "단일사슬", "C": "삼중나선"}

XENO_CLS = {
    "이종유래 없음": "0", "동물유래 포함": "1",
    "동물유래 — 대체재 있음": "2", "동물유래 — 대체재 없음": "1",
    "불명(확보 실패)": "3",
}


def mats(scope):
    """material_scope 문자열 → A/B/C 칸 표시.

    '전 조합'이나 'A+B+C'는 셋 다 켠다. 읽지 못한 값은 켜지 않고 그대로 둔다 —
    모르는 것을 켜 놓으면 표가 거짓말을 한다.
    """
    s = (scope or "").strip()
    if not s:
        return ""
    on = set(MATS) if ("전 조합" in s or "전체" in s) else {m for m in MATS if m in s}
    cells = "".join(
        f'<i class="{"on" if m in on else ""}{" helix" if m == "C" and m in on else ""}">{m}</i>'
        for m in MATS)
    title = ("적용 재료: " + ", ".join(f"{m}({MAT_NAME[m]})" for m in sorted(on))
             if on else f"적용 범위: {s}")
    return f'<span class="mat" title="{attr(title)}">{cells}</span>'


def form(kind):
    """삼중나선 / 단일사슬 배지. 이 보고서의 물리적 분기점이다."""
    k = (kind or "").strip()
    if "삼중" in k or k == "C":
        return '<span class="form form-th">삼중나선</span>'
    if "단일" in k or k in ("A", "B"):
        return '<span class="form form-sc">단일사슬</span>'
    return ""


def xeno(v):
    v = (v or "").strip()
    c = XENO_CLS.get(v)
    if not c:
        return esc(v)
    return f'<span class="xeno xeno-{c}">{esc(v)}</span>'


def change(prev, new):
    """이전 판정 → 새 판정. 같으면 '유지'라고 적는다."""
    p, n = (prev or "").strip(), (new or "").strip()
    if not p and not n:
        return ""
    if p == n:
        return f'<span class="chg"><span class="now">{esc(n)}</span> <span class="was">유지</span></span>'
    return (f'<span class="chg"><span class="was">{esc(p or "—")}</span>'
            f'<span class="arr">→</span><span class="now">{esc(n or "—")}</span></span>')
