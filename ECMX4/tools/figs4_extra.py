# -*- coding: utf-8 -*-
"""ECMX-004 나머지 도판 — Wnt 공급 방식, 저분자 투여 시점, 전체 합계, 품질 규격."""
import re
from figlib2 import *
from figs4_data import NEC, LAYERS


def fig_wnt_options(opts=None):
    """그림. Wnt3a를 어떻게 공급할 것인가 — 직접 조제에서 가장 먼저 막히는 지점.

    Wnt3a는 지질(팔미톨레오일)이 붙은 단백질이라 물에 잘 안 녹고, 혈청 단백질
    afamin 같은 운반체 없이는 역가가 빠르게 떨어진다. 그래서 '재조합 단백질을 사서
    넣는다'가 다른 성장인자만큼 간단하지 않다. 세 갈래를 나란히 놓는다.
    """
    opts = opts or [
        ("재조합 Wnt3a 단백질", "정의성 높음", C["md"],
         [("정의성", 5), ("로트 재현성", 3), ("역가 안정성", 2), ("비용 효율", 1), ("조제 수고", 4)],
         "가장 '정의된' 선택지지만, 용액 상태에서 역가가 떨어지는 것이 문제다."),
        ("조건배지 (L-WRN · Wnt3a-CM)", "실험실 표준 관행", C["mx"],
         [("정의성", 1), ("로트 재현성", 2), ("역가 안정성", 4), ("비용 효율", 5), ("조제 수고", 1)],
         "세포주를 직접 키워 상등액을 쓴다. 싸지만 배치마다 역가가 달라 매번 검정이 필요하다."),
        ("afamin-Wnt3a · Wnt 대체물", "운반체를 붙인 형태", C["cnd"],
         [("정의성", 4), ("로트 재현성", 4), ("역가 안정성", 5), ("비용 효율", 2), ("조제 수고", 4)],
         "운반체와 복합하거나 수용체를 직접 묶는 설계로 안정성 문제를 우회한다."),
    ]
    W, H = 940, 374
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "Wnt3a 공급 방식 세 갈래",
                   "막대는 근거 문헌의 서술을 5단계로 순위화한 것이다 — 측정값이 아니다"))

    cw = 296
    for i, (nm, tag, col, bars, note) in enumerate(opts):
        x = 20 + i * (cw + 12)
        b.append(rect(x, 56, cw, 258, "#FFFFFF", rx=10, stroke=col, sw=1.5))
        b.append(rect(x, 56, cw, 34, col, rx=10))
        b.append(rect(x, 80, cw, 10, col))
        b.append(txt(x + 14, 78, nm, 12.4, "#FFFFFF", weight="700"))
        b.append(txt(x + 14, 108, tag, 10.4, col, weight="600"))
        yy = 128
        for lab, v in bars:
            b.append(txt(x + 14, yy + 9, lab, 10.2, C["mut"]))
            bx, bwid = x + 108, cw - 130
            b.append(rect(bx, yy, bwid, 11, "#EEF2F4", rx=5.5))
            b.append(rect(bx, yy, bwid * v / 5, 11, col, rx=5.5))
            for k in range(1, 5):
                b.append(line(bx + bwid * k / 5, yy, bx + bwid * k / 5, yy + 11, "#FFFFFF", 1.2))
            yy += 24
        b.append(line(x + 14, yy + 6, x + cw - 14, yy + 6, C["line"], 1))
        wtxt, n = wrap(x + 14, yy + 26, note, 10.2, width=22, lh=14, fill=C["mut"])
        b.append(wtxt)

    b.append(rect(20, 330, W - 40, 32, C["cnd_bg"], rx=7, stroke=C["cnd"]))
    b.append(txt(34, 350,
                 "어느 쪽을 고르든 역가 검정(TCF/LEF 리포터 등)을 배치마다 걸지 않으면 "
                 "'왜 안 자라는지' 를 나중에 되짚을 수 없다.", 10.8, C["cnd"], weight="600"))
    return svg(W, H, "".join(b), "Wnt3a 공급 방식 세 갈래 비교")


_STAGE_KEYS = [("계대 직후", ("계대",)), ("확장 전 기간", ("확장",)),
               ("분화 전환 후", ("분화",)), ("전 단계 상시", ("전 단계", "전단계", "상시"))]


def fig_smallmol_timing(rows, cats=("저분자",)):
    """저분자는 '넣느냐'보다 '언제 빼느냐'가 중요하다."""
    sel = [r for r in rows if (r.get("category") or "").strip() in cats]
    W = 940
    H = 140 + max(len(sel), 1) * 30
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "저분자 화합물의 투여 구간",
                   "계대 직후 며칠만 넣는 것과 내내 넣는 것을 구분하지 않으면 표현형이 흔들린다"))
    if not sel:
        b.append(nodata(40, 68, W - 80, 44, "저분자 범주 행이 없음"))
        return svg(W, H, "".join(b), "저분자 투여 구간")

    x0, seg = 250, (W - 300) / 4.0
    heads = ["계대 직후", "확장기", "분화 전환", "상시"]
    for i, h in enumerate(heads):
        b.append(txt(x0 + seg * i + seg / 2, 66, h, 10.6, C["faint"], "middle", "600"))
        b.append(line(x0 + seg * i, 72, x0 + seg * i, 78 + len(sel) * 30, C["line"], 1, dash="3 4"))
    b.append(line(x0 + seg * 4, 72, x0 + seg * 4, 78 + len(sel) * 30, C["line"], 1, dash="3 4"))

    y = 80
    for r in sel:
        nm = (r.get("name_ko") or r.get("name_en") or "").strip()
        st = (r.get("stage") or "")
        nec_ = (r.get("necessity") or "").strip()
        col = N_SOLID.get(nec_, C["opt"])
        b.append(txt(240, y + 18, nm[:22], 11.2, C["ink"], "end"))
        hits = []
        if "계대" in st: hits.append(0)
        if "확장" in st: hits.append(1)
        if "분화" in st: hits.append(2)
        if ("전 단계" in st) or ("전단계" in st) or ("상시" in st): hits = [0, 1, 2, 3]
        if not hits:
            b.append(nodata(x0 + 4, y + 4, seg * 4 - 8, 19, "단계 미기재"))
        else:
            for k in range(min(hits), max(hits) + 1):
                if k in hits or (max(hits) - min(hits) > 0 and min(hits) < k < max(hits)):
                    b.append(rect(x0 + seg * k + 3, y + 4, seg - 6, 19, col, rx=5, op=.82))
            for k in hits:
                b.append(txt(x0 + seg * k + seg / 2, y + 18, nec_[:3], 9.6,
                             N_TXT.get(nec_, "#fff"), "middle", "600"))
        y += 30
    b.append(legend(24, H - 22, [(N_SOLID[n], n) for n in NEC[:3]], horiz=True, step=110))
    b.append(txt(430, H - 22, "구간 없음 = BOM의 stage 열이 비어 있는 행", 10.2, C["faint"]))
    return svg(W, H, "".join(b), "저분자 투여 구간")


def fig_totals(scaf, med):
    """이 보고서 전체의 결론을 한 장으로 — 사야 할 품목이 몇 개인가."""
    W, H = 900, 288
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "두 계통을 합친 구매 품목 수",
                   "'직접 만든다'가 실제로 몇 개의 품번을 뜻하는지"))

    def tally(rows):
        d = {n: 0 for n in NEC}
        for r in rows:
            n = (r.get("necessity") or "").strip()
            if n in d:
                d[n] += 1
        return d

    sets = [("지지체 (콜라겐 I/III 겔)", tally(scaf), C["mx"], C["mx_bg"], C["mx_ln"]),
            ("배지 (직접 조제)", tally(med), C["md"], C["md_bg"], C["md_ln"])]
    x = 20
    for nm, d, col, bgc, lnc in sets:
        tot = sum(d.values())
        b.append(rect(x, 56, 424, 184, bgc, rx=10, stroke=lnc, sw=1.4))
        b.append(txt(x + 18, 82, nm, 13, col, weight="700"))
        b.append(txt(x + 18, 128, str(tot), 40, col, weight="700"))
        b.append(txt(x + 18 + len(str(tot)) * 24 + 10, 128, "품목", 13, col, op=.8))
        yy = 154
        BW = 300
        for n in NEC[:3]:
            w = (d[n] / max(tot, 1)) * BW
            b.append(txt(x + 18, yy + 13, n, 10.2, col, weight="600"))
            b.append(rect(x + 66, yy, BW, 16, "#FFFFFF", rx=5, stroke=lnc, sw=.7))
            b.append(rect(x + 66, yy, w, 16, N_FILL[n], rx=5))
            b.append(txt(x + 66 + BW + 12, yy + 13, str(d[n]), 12, col, "start", "700", mono=True))
            yy += 24
        if tot == 0:
            b.append(nodata(x + 18, 154, 388, 64, "BOM이 아직 비어 있음"))
        x += 436
    b.append(txt(20, 266,
                 "필수만 세어도 두 계통을 합친 수가 실제 구매 목록의 하한이다. "
                 "조건부는 조직·단계에 따라 켜지고 꺼진다.", 10.8, C["faint"]))
    return svg(W, H, "".join(b), "두 계통을 합친 구매 품목 수")


def fig_qc(rows):
    """L9 품질 규격 — 콜라겐에서만 생기는 항목들."""
    L9 = [r for r in rows if (r.get("layer") or "").strip().upper() == "L9"]
    W = 900
    H = 104 + max(len(L9), 1) * 32
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(title(20, 24, "입고 검사 항목 — 콜라겐계에서만 생기는 것들",
                   "로트가 바뀌면 겔이 달라진다. 그것을 잡아내는 규격"))
    if not L9:
        b.append(nodata(40, 66, W - 80, 44, "L9 행이 확보되지 않음"))
        return svg(W, H, "".join(b), "입고 검사 항목")
    b.append(line(20, 68, W - 20, 68, C["line2"], 1))
    b.append(txt(26, 62, "검사 항목", 10.4, C["faint"], weight="600"))
    b.append(txt(300, 62, "필수도", 10.4, C["faint"], weight="600"))
    b.append(txt(376, 62, "규격값", 10.4, C["faint"], weight="600"))
    y = 76
    for r in L9:
        nm = (r.get("name_ko") or r.get("name_en") or "").strip()
        nec_ = (r.get("necessity") or "").strip()
        qs = (r.get("quant_spec") or "").strip()
        b.append(rect(20, y, W - 40, 28, "#FFFFFF", rx=5, stroke=C["line"]))
        b.append(txt(30, y + 19, nm[:20], 11.4, C["ink"], weight="600"))
        b.append(rect(300, y + 6, 52, 17, N_SOLID.get(nec_, C["opt"]), rx=8.5))
        b.append(txt(326, y + 18, nec_ or "—", 9.8, N_TXT.get(nec_, "#fff"), "middle", "600"))
        ok = qs and qs != "정량 근거 없음"
        b.append(txt(376, y + 19, (qs or "정량 근거 없음")[:58], 10.4,
                     C["mut"] if ok else C["faint"], mono=bool(ok)))
        y += 32
    return svg(W, H, "".join(b), "입고 검사 항목")
