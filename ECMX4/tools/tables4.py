# -*- coding: utf-8 -*-
"""ECMX-004 BOM 행 → 표 마크업.

표는 두 종류다.
  · 요약표 — 화면에서 바로 읽는 것. 열 5~6개를 넘기지 않는다.
  · 전체표 — <details> 안에 접어 두는 것. 구매 담당이 펼쳐서 품번을 본다.
좁은 화면에서 열 12개짜리 표를 그대로 펼치면 아무도 읽지 않으므로 이렇게 나눈다.
"""
import html, re
from report_base2 import nec, tier, q, esc, attr, table, mats, xeno, change, form


def _ref_links(s, refs, meta):
    """evidence_ref 문자열 → 각주 번호들."""
    out, seen = [], set()
    ids = re.findall(r"10\.\d{4,9}/[^\s;,)\]\"']+", str(s or ""))
    ids += re.findall(r"\b(?:US|WO|EP|KR|JP|CN)[\s-]?\d{4,}[A-Z0-9]*\b", str(s or ""))
    ids += re.findall(r"\bPMC\d{5,}\b", str(s or ""))
    for k in ids:
        k = re.sub(r"[.,;)\]]+$", "", k)
        m = meta.get(k.lower()) or {}
        key = (m.get("doi") or k)
        if m.get("kind") == "patent":
            key = k
        if key in seen:
            continue
        seen.add(key)
        out.append(refs.cite(key, **{a: b for a, b in m.items() if a != "cited"}))
    if len(out) <= 4:
        return "".join(out)
    # 넷을 넘으면 뒤는 접어 둔다 — 번호가 줄줄이 붙으면 아무도 읽지 않는다.
    return ("".join(out[:4])
            + f'<span class="more" title="같은 항목의 근거 {len(out)-4}건 더">'
              f'{"".join(out[4:])}</span>')


def _trim(s, n):
    s = str(s or "").strip()
    return s if len(s) <= n else s[:n - 1] + "…"


def bom_summary(rows, refs, meta, cols=None, caption="", num=None, cls="mx"):
    """요약표 — 물질 / 적용 재료 / 역할 / 필수도+근거 / 정량 조건.

    '적용 재료' 열이 ECMX-003에는 없던 열이다. 같은 물질이라도 어느 재료 조합에서
    필요한지가 다르므로, 이 열 없이는 구매 목록을 만들 수 없다.
    """
    head = ["물질", "적용 재료", "이 계통에서 하는 일", "필수도", "정량 조건"]
    body = []
    for r in rows:
        nm = (r.get("name_ko") or "").strip()
        en = (r.get("name_en") or "").strip()
        nmc = f'<b>{esc(nm)}</b>' + (f'<br><span class="en">{esc(en)}</span>' if en and en != nm else "")
        role = _trim(r.get("role_in_rc_system") or r.get("role_in_collagen_system")
                     or r.get("function"), 78)
        why = (r.get("necessity_basis") or r.get("confidence_reason") or "")
        badge = nec(r.get("necessity"), why)
        ev = (r.get("evidence_type") or "").strip()
        evs = f' <span class="evt" title="근거의 성격">{esc(ev)}</span>' if ev else ""
        cites = _ref_links(r.get("evidence_ref"), refs, meta)
        qs = (r.get("quant_spec") or r.get("conc_typical") or "").strip()
        qcell = q(_trim(qs, 60)) if qs and qs != "정량 근거 없음" else '<span class="na">정량 근거 없음</span>'
        body.append([nmc, mats(r.get("material_scope")), esc(role),
                      badge + evs + cites, qcell])
    return table(head, body, caption, ["", "", "", "", "q"], cls, num,
                 widths=["18%", "9%", "26%", "22%", "25%"])


def bom_full(rows, caption="", cls="mx", label="전체 명세 — 공급사 · 품번 · 등급 · 대체재 · 위험"):
    """접어 두는 전체표."""
    head = ["ID", "층위/범주", "물질", "재료", "필수도", "정량", "공급사", "품번",
            "등급", "대체재", "위험", "신뢰도"]
    body = []
    for r in rows:
        body.append([
            f'<span class="q">{esc(r.get("item_id"))}</span>',
            esc(r.get("layer") or r.get("category")),
            f'<b>{esc(r.get("name_ko"))}</b>',
            mats(r.get("material_scope")) or esc(r.get("xeno_status") or ""),
            nec(r.get("necessity")),
            f'<span class="q">{esc(_trim(r.get("quant_spec") or r.get("conc_typical"), 44))}</span>',
            esc(_trim(r.get("supplier"), 28)),
            f'<span class="q">{esc(_trim(r.get("catalog_no"), 26))}</span>',
            esc(_trim(r.get("grade"), 26)),
            esc(_trim(r.get("alternatives"), 40)),
            esc(_trim(r.get("risk"), 46)),
            f'<span class="b b-{esc(r.get("confidence"))}" title="{attr(r.get("confidence_reason"))}">'
            f'{esc(r.get("confidence"))}</span>',
        ])
    t = table(head, body, caption,
              ["q", "", "", "", "", "q", "", "q", "", "", "", ""], cls)
    return f'<details><summary>{esc(label)} — {len(rows)}행</summary>{t}</details>'


def med_summary(rows, refs, meta, caption="", num=None):
    head = ["성분", "하는 일", "필수도", "대표 농도", "이종유래"]
    body = []
    for r in rows:
        nm = (r.get("name_ko") or "").strip()
        en = (r.get("name_en") or "").strip()
        nmc = f'<b>{esc(nm)}</b>' + (f'<br><span class="en">{esc(en)}</span>' if en and en != nm else "")
        ev = (r.get("evidence_type") or "").strip()
        evs = f' <span class="evt">{esc(ev)}</span>' if ev else ""
        body.append([
            nmc,
            esc(_trim(r.get("function"), 66)),
            nec(r.get("necessity"), r.get("confidence_reason")) + evs
            + _ref_links(r.get("evidence_ref"), refs, meta),
            q(_trim(r.get("conc_typical"), 34)),
            xeno(r.get("xeno_status")) + (
                f'<br><span class="q sm">{esc(_trim(r.get("stage"), 16))}</span>'
                if (r.get("stage") or "").strip() else ""),
        ])
    return table(head, body, caption, ["", "", "", "q", ""], "md", num,
                 widths=["18%", "29%", "22%", "21%", "10%"])


def stock_table(rows, caption="", num=None):
    """저장액·보관 — 직접 조제하는 팀이 실제로 매일 보는 표."""
    sel = [r for r in rows if (r.get("stock_storage") or "").strip()]
    head = ["성분", "형태", "저장액 · 보관", "공급사 · 품번"]
    body = []
    for r in sel:
        body.append([
            f'<b>{esc(r.get("name_ko"))}</b>',
            esc(_trim(r.get("form"), 16)),
            f'<span class="q">{esc(_trim(r.get("stock_storage"), 110))}</span>',
            esc(_trim(r.get("supplier"), 22)) +
            f'<br><span class="q">{esc(_trim(r.get("catalog_no"), 24))}</span>',
        ])
    return table(head, body, caption, ["", "", "", ""], "md", num,
                 widths=["20%", "13%", "46%", "21%"])


def params_table(rows, refs, meta, caption="", num=None):
    head = ["파라미터", "재료", "조건", "값", "측정법", "결과 · 해석"]
    body = []
    for r in rows:
        v = (r.get("value") or "").strip()
        u = (r.get("unit") or "").strip()
        body.append([
            f'<b>{esc(r.get("param_name"))}</b>',
            f'<span class="q">{esc(_trim(r.get("material"), 14))}</span>',
            esc(_trim(r.get("condition"), 44)),
            q(v, (" " + u) if u else ""),
            esc(_trim(r.get("method"), 30)),
            esc(_trim(r.get("effect"), 72)) + _ref_links(r.get("evidence_ref"), refs, meta),
        ])
    return table(head, body, caption, ["", "q", "", "q", "", ""], "mx", num,
                 widths=["17%", "8%", "20%", "12%", "15%", "28%"])


def matrix_table(rows, caption="", num=None):
    if not rows:
        return ""
    cols = [c for c in rows[0].keys() if c and c != "성분"]
    head = ["성분"] + cols
    body = []
    for r in rows:
        line = [f'<b>{esc(r.get("성분"))}</b>']
        for c in cols:
            v = (r.get(c) or "").strip()
            k = next((n for n in ("필수", "조건부", "선택", "미사용") if v.startswith(n)), None)
            detail = v[len(k):].strip(" ()") if k else ""
            cell = nec(k, detail) if k else '<span class="na">—</span>'
            if detail:
                cell += f'<br><span class="q sm">{esc(_trim(detail, 22))}</span>'
            line.append(cell)
        body.append(line)
    return table(head, body, caption, [""] * len(head), "md", num)



def delta_table(rows, caption="", num=None):
    """ECMX-003 대비 무엇이 달라졌는가. 이 보고서에만 있는 표다."""
    head = ["성분", "판정 변화", "농도 변화", "종류", "왜 바뀌었는가"]
    body = []
    for r in rows:
        body.append([
            f'<b>{esc(r.get("name_ko"))}</b>',
            change(r.get("prev_necessity"), r.get("new_necessity")),
            change(r.get("prev_conc"), r.get("new_conc")),
            esc(_trim(r.get("change_kind"), 14)),
            esc(_trim(r.get("reason"), 110)),
        ])
    return table(head, body, caption, ["", "", "", "", ""], "md", num,
                 widths=["18%", "17%", "19%", "12%", "34%"])
