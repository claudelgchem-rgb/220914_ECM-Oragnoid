# -*- coding: utf-8 -*-
"""구조·체계 도식 (L1~L9 층위, 등급 흐름, 연표, 논문 vs 특허 대조)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

SURF = C.get("surface", "#FFFFFF")


def fig_layers(counts=None):
    """그림: 물질 인벤토리 L1~L9 층위 구조도. counts={'L1':n,...}"""
    W, H = 880, 520
    counts = counts or {}
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "ECM 소재 개발에 필요한 물질의 아홉 층위", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "위 네 층은 생체 ECM에서 유래한 '무엇을 흉내 낼 것인가', 가운데 세 층은 '어떻게 만들 것인가',"
                          " 아래 두 층은 '제품이 되려면 무엇을 지켜야 하는가'에 해당한다.", 10.4, C["mut"], "middle"))
    groups = [
        ("생물학적 구성요소 — 생체 ECM을 흉내 내는 부품", C["e0"], [
            ("L1", "구조 단백질", "콜라겐 I/III/IV, 젤라틴, 라미닌 아이소폼, 피브로넥틴, 비트로넥틴, 엘라스틴, 피브린"),
            ("L2", "글리코사미노글리칸·다당", "히알루론산, 헤파란황산, 콘드로이틴황산, 알지네이트, 키토란, 덱스트란, 아가로스"),
            ("L3", "프로테오글리칸·연결분자", "퍼레칸, 니도젠(엔탁틴), 데코린, 아그린, 테나신"),
            ("L4", "성장인자·신호분자", "EGF, 노긴, 알스폰딘, Wnt3a, FGF 계열, BMP, TGF-β  ※배지형/매트릭스결합형 구분 필수"),
        ]),
        ("공정·화학 — 그것을 실제 겔로 만드는 수단", C["acc"], [
            ("L5", "펩타이드 모티프·기능화 리간드", "RGD, IKVAV, YIGSR, GFOGER, MMP 절단 서열, 트랜스글루타미네이스 기질 펩타이드"),
            ("L6", "가교제·개시제·촉매", "미생물 트랜스글루타미네이스, 13인자, 라이실 옥시다제, EDC/NHS, 제니핀, 광개시제, 클릭 시약"),
            ("L7", "합성 백본·하이브리드", "다분지 PEG(비닐설폰·노보넨·티올·말레이미드), PVA, 온도감응성 고분자, 자기조립 펩타이드"),
        ]),
        ("제품 요건 — 재현 가능한 물건이 되기 위한 조건", C["e2"], [
            ("L8", "완충·이온·부형제", "염화나트륨(이온강도), 인산·HEPES 완충계, 칼슘염, 당·동결보호제, pH 조절제"),
            ("L9", "품질·안전 규격 항목", "내독소, 생균수, 마이코플라스마, 동물유래성분, 잔류 가교제·용매, 세포독성, 무균화, 로트 간 G′ 편차"),
        ]),
    ]
    y = 66
    for gname, gcol, rows in groups:
        b.append(rect(28, y, W - 56, 20, gcol, rx=5, op=0.13))
        b.append(txt(38, y + 14.5, gname, 11.2, C["ink"], "start", "bold"))
        y += 25
        for code, name, ex in rows:
            h = 43
            b.append(rect(28, y, W - 56, h, SURF, rx=7, stroke=C["line"]))
            b.append(rect(28, y, 5, h, gcol, rx=2.5))
            b.append(rect(41, y + 10, 34, 22, gcol, rx=5, op=0.2))
            b.append(txt(58, y + 25, code, 12.4, C["ink"], "middle", "bold"))
            b.append(txt(86, y + 19, name, 11.8, C["ink"], "start", "bold"))
            b.append(txt(86, y + 34, ex[:96], 9.5, C["mut"]))
            n = counts.get(code)
            if n is not None:
                b.append(rect(W - 96, y + 11, 56, 21, gcol, rx=10, op=0.16))
                b.append(txt(W - 68, y + 25.5, f"{n}건", 11, C["ink"], "middle", "bold"))
            y += h + 5
        y += 5
    b.append(txt(28, H - 10, "각 층위 옆의 건수는 본 조사에서 실제로 등재한 물질·항목 수다. 어느 한 층위라도 비면 소재는 제품이 되지 못한다.",
                 10.2, C["mut"]))
    return svg(W, H, "".join(b), "물질 인벤토리 L1~L9 층위 구조도")


def fig_grades():
    """그림: 등급 체계 흐름도 (RUO → GMP → 부자재/의료기기)"""
    W, H = 880, 400
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "연구용에서 임상용으로 — 등급 전환의 관문", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "같은 분자라도 등급이 다르면 다른 물건이다. 오른쪽으로 갈수록 요구 문서와 시험이 늘고 가격과 리드타임이 급격히 오른다.",
                 10.4, C["mut"], "middle"))
    stages = [
        (34, C["e3"], "연구용", "Research Use Only (RUO)",
         ["성적서 기본 항목", "동물유래 허용", "로트 편차 관리 느슨"],
         "실험실 배양·논문"),
        (262, C["acc"], "임상 연구용", "준-GMP / 임상시험용",
         ["동물유래 성분 배제 시작", "내독소·생균수 규격 명문화", "변경관리 도입"],
         "임상시험 물질 제조"),
        (490, C["e1"], "의약품 제조 등급", "GMP grade",
         ["전 공정 문서화·추적", "바이러스 안전성 평가", "공급사 감사·이중 공급원"],
         "세포치료제 상업 생산"),
        (718, C["e0"], "부자재 규격 충족", "ancillary material",
         ["최종 제품 잔류 평가", "규제 제출 자료 일부", "약전 기준 적용"],
         "허가 신청 자료 편입"),
    ]
    for x, col, t1, t2, reqs, use in stages:
        w = 148
        b.append(rect(x, 74, w, 218, SURF, rx=9, stroke=col, sw=1.7))
        b.append(rect(x, 74, w, 44, col, rx=9, op=0.15))
        b.append(rect(x, 74, w, 3.5, col, rx=2))
        b.append(txt(x + w/2, 95, t1, 12.4, C["ink"], "middle", "bold"))
        b.append(txt(x + w/2, 110, t2, 9.2, C["mut"], "middle", "normal", 1, True))
        y = 138
        for r in reqs:
            for k, ln in enumerate([r[i:i+13] for i in range(0, len(r), 13)][:3]):
                b.append(txt(x + 12, y, ("· " if k == 0 else "  ") + ln, 9.6, C["ink"])); y += 12.5
            y += 3
        b.append(rect(x + 10, 256, w - 20, 26, col, rx=6, op=0.11))
        b.append(txt(x + w/2, 273, use, 9.6, C["ink"], "middle", "bold"))
    for ax in (190, 418, 646):
        b.append(txt(ax + 21, 188, "▶", 15, C["line2"], "middle", "bold"))
    b.append(rect(34, 306, W - 68, 56, C["e0"], rx=9, op=0.08))
    b.append(rect(34, 306, 4.5, 56, C["e0"], rx=2))
    b.append(txt(50, 325, "등급 전환의 실질적 병목", 11.6, C["ink"], "start", "bold"))
    b.append(txt(50, 342, "분자를 바꾸는 것이 아니라 '증명 체계'를 새로 만드는 일이다. 동물유래 원료 대체, 로트 간 물성 편차의 규격화,",
                 10.2, C["mut"]))
    b.append(txt(50, 355, "공급사의 변경관리 약정 — 이 셋이 확보되지 않으면 연구에서 잘 되던 소재도 임상 단계로 넘어가지 못한다.",
                 10.2, C["mut"]))
    return svg(W, H, "".join(b), "연구용에서 임상용까지의 등급 체계 흐름도")


def fig_paper_vs_patent(rows):
    """그림: 논문 근거 vs 특허 독립항 대조.
    rows: [(성분명, 특허 독립항 기재 건수, 최고 등급 E0~E3, 근거유형요약)]"""
    W = 880
    H = 108 + len(rows) * 30 + 92
    b = [rect(0, 0, W, H, C["bg"], rx=0)]
    b.append(txt(W/2, 24, "특허가 필수라 말하는 것과 논문이 필수라 증명한 것", 15, C["ink"], "middle", "bold"))
    b.append(txt(W/2, 43, "왼쪽 막대는 특허 독립항에 필수 구성요소로 기재된 건수, 오른쪽 칸은 제거·치환·농도반응 실험으로 판정한 필수도 등급이다.",
                 10.3, C["mut"], "middle"))
    b.append(txt(W/2, 59, "둘이 어긋나는 성분은 '업계 관행'과 '생물학적 증명'이 일치하지 않는다는 뜻이다.",
                 10.3, C["mut"], "middle", "bold"))

    x_lab, x_bar, bar_w, x_tier = 186, 196, 300, 530
    mx = max([r[1] for r in rows] + [1])
    b.append(txt(x_lab, 92, "성분", 10.6, C["faint"] if "faint" in C else C["mut"], "end", "bold"))
    b.append(txt(x_bar, 92, "특허 독립항 기재 건수", 10.6, C["faint"] if "faint" in C else C["mut"], "start", "bold"))
    b.append(txt(x_tier, 92, "논문 근거 필수도", 10.6, C["faint"] if "faint" in C else C["mut"], "start", "bold"))
    b.append(txt(x_tier + 118, 92, "판정 근거 유형", 10.6, C["faint"] if "faint" in C else C["mut"], "start", "bold"))
    b.append(line(30, 98, W - 30, 98, C["line2"], 1))

    y = 116
    for name, n, tier, ev in rows:
        bw = (n / mx) * bar_w
        b.append(txt(x_lab, y + 4, name, 11.2, C["ink"], "end", "bold"))
        b.append(rect(x_bar, y - 8, bar_w, 17, C["line"], rx=4, op=0.32))
        b.append(rect(x_bar, y - 8, bw, 17, C["acc"], rx=4, op=0.72))
        b.append(txt(x_bar + max(bw, 16) + 7, y + 4.5, f"{n}", 10.4, C["ink"], "start", "bold"))
        b.append(rect(x_tier, y - 8, 40, 17, TIER_SOLID[tier], rx=4))
        b.append(txt(x_tier + 20, y + 4.5, tier, 10.6, TIER_TXT[tier], "middle", "bold"))
        b.append(txt(x_tier + 50, y + 4.5, {"E0": "절대필수", "E1": "조건부", "E2": "선택", "E3": "대체가능"}[tier],
                     9.8, C["mut"]))
        b.append(txt(x_tier + 118, y + 4.5, ev[:44], 9.6, C["mut"]))
        y += 30

    y += 8
    b.append(line(30, y, W - 30, y, C["line"], 1))
    y += 20
    b.append(rect(30, y - 14, W - 60, 52, C["e1"], rx=8, op=0.09))
    b.append(rect(30, y - 14, 4.5, 52, C["e1"], rx=2))
    b.append(txt(46, y + 2, "읽는 법", 11.2, C["ink"], "start", "bold"))
    b.append(txt(46, y + 18, "특허 독립항에 자주 등장한다는 사실은 '업계가 필수로 취급한다'는 방증일 뿐, 생물학적 필수성의 증명이 아니다.", 10.2, C["mut"]))
    b.append(txt(46, y + 31, "막대는 길지만 등급이 낮은 성분은, 관행이 실험 근거보다 앞서 있는 영역이다.", 10.2, C["mut"]))
    b.append(legend(W - 300, H - 12, [(TIER_SOLID[t], f"{t}") for t in ("E0", "E1", "E2", "E3")], 9.6, horiz=True, box=9))
    return svg(W, H, "".join(b), "논문 근거와 특허 독립항 기재의 대조 도식")
