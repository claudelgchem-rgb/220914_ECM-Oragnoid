#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gaps.md 생성 — 각 산출물의 '확보 실패' 기록을 모은다. 유예 표현 없이 실패로만 기록한다(R-03)."""
import os, re

BASE = "/mnt/user-data/outputs/ECMX"
FILES = {
    "01_overview_core.md": "M1 분야 개요 (A)",
    "02_trends.md": "M1 기술 계보·동향 (B)",
    "03_materials_bio.md": "M2 생물유래 물질 L1~L4 (C)",
    "04_materials_chem.md": "M2 화학·합성 물질 L5~L7 (D)",
    "05_specs_regulatory.md": "M2 규격·품질·규제 L8~L9 (E)",
    "06_supply.md": "공급·조달 (F)",
    "07_patents.md": "특허 랜드스케이프 (G)",
    "11_essential_materials.md": "M3 필수물질 논문 근거 (N)",
    "12_patent_essentials.md": "M3 특허 독립항 (P)",
}
PAT = re.compile(r"확보\s*실패\s*[:：]\s*([^\n|]{8,320})")


def clean(s):
    s = re.sub(r"\*\*|__|`|<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip(" .|-—·")


def split_item(s):
    for sep in (" — ", " – ", " - ", ". 사유", ", 사유"):
        if sep in s:
            a, b = s.split(sep, 1)
            return clean(a)[:120], clean(b)[:260]
    m = re.match(r"(.{6,80}?)[\(\[](.+)[\)\]]\s*$", s)
    if m:
        return clean(m.group(1))[:120], clean(m.group(2))[:260]
    return clean(s)[:120], "사유가 원문에 항목과 분리되어 기재되지 않음 — 원문 절 참조"


def main():
    rows, per = [], {}
    for fn, label in FILES.items():
        p = os.path.join(BASE, fn)
        if not os.path.exists(p):
            rows.append([label, f"{fn} 산출물 자체", "해당 산출물이 생성되지 않음"])
            continue
        t = open(p, encoding="utf-8", errors="replace").read()
        seen, n = set(), 0
        for m in PAT.finditer(t):
            item, why = split_item(m.group(1))
            k = item[:52]
            if k in seen or len(item) < 5:
                continue
            seen.add(k)
            rows.append([label, item, why])
            n += 1
        per[label] = n
    return rows, per


def render(rows, per):
    L = ["---", "agent: O", "status: complete", "date_checked: 2026-09-14",
         f"items_count: {len(rows)}", "evidence_count: {papers: 0, patents: 0}",
         f"unresolved: {len(rows)}", "---", "",
         "# 확보 실패·결측 항목 (gaps)", "",
         "이 문서는 **이번 조사에서 확보에 실패한 항목**의 기록이다.",
         "\"이후 조사하겠다\"거나 \"추가 확인이 필요하다\"는 유예 표현을 쓰지 않는다(R-03).",
         "실패는 실패로 기록하고, 그 사실이 결론에 어떤 한계를 만드는지 밝힌다.", "",
         "- **데이터 기준일**: 2026-09-14", "",
         "## 1. 산출물별 실패 건수", "",
         "| 산출물 | 확보 실패 건수 |", "|---|---:|"]
    for k, v in per.items():
        L.append(f"| {k} | {v} |")
    L.append(f"| **합계** | **{len(rows)}** |")

    L += ["", "## 2. 실패 항목 전체", "",
          "| 구분 | 확보하지 못한 것 | 실패 사유 |", "|---|---|---|"]
    for r in rows:
        L.append(f"| {r[0]} | {r[1].replace('|','/')} | {r[2].replace('|','/')} |")

    L += ["", "## 3. 실패가 결론에 만드는 한계", "",
          "### 3-1. 회수 가능성(AX-7) 축의 근거가 얇다",
          "매트릭스 계열별로 오가노이드 회수 효율을 **같은 조건에서 비교한 문헌을 찾지 못했다.**",
          "회수는 계대·분석·이식에 직결되는 실무적 요구인데도 정량 비교 근거가 없다.",
          "따라서 이 축의 판정은 다른 축보다 신뢰도가 낮으며, 보고서 본문에도 그렇게 적었다.",
          "이것은 본 조사의 한계인 동시에 **분야 전체의 공백**으로 보인다.", "",
          "### 3-2. 비공개 논문의 정량 조건은 초록 범위로만 확인했다",
          "핵심 논문 여러 편이 오픈액세스가 아니어서 본문을 직접 읽지 못했다.",
          "해당 항목은 실험 조건·조성비를 추정해 서술하지 않았고(R-07), 근거 대장에",
          "`본문 미확인`으로 표시했다. 이 항목들의 신뢰도는 '상'이 될 수 없다.", "",
          "### 3-3. 미공개 특허 출원은 원리적으로 확인 불가능하다",
          "출원 후 일정 기간이 지나지 않은 건은 공개되지 않는다. 따라서 본 보고서의 특허 분석은",
          "**자유실시(FTO) 판단 근거가 될 수 없다.** 사업적 판단에는 유료 상용 데이터베이스와",
          "변리사 검토가 별도로 필요하다.", "",
          "### 3-4. 가격·규격 일부는 제조사 접근 차단으로 확인하지 못했다",
          "여러 제조사 페이지가 자동 접근을 차단(HTTP 403/503)해 1차 확인에 실패했다.",
          "해당 항목은 그 사실을 필드에 기록하고 신뢰도를 낮췄다. 또한 의약품 제조 등급 품목은",
          "애초에 공개 가격이 없고 견적으로만 거래되는 경우가 많다 — 이는 조사 실패가 아니라",
          "**그 시장의 거래 관행**이며, 그 자체가 조달 계획에 반영되어야 할 정보다.", "",
          "### 3-5. 조사 인프라 수준의 접근 차단 기록",
          "다음 경로는 이번 실행에서 사용할 수 없었다. 대체 경로로 목표 건수를 달성했으므로",
          "게이트 판정에는 영향이 없으나, 재현 시 참고를 위해 남긴다.", "",
          "| 시도한 경로 | 결과 | 대체 수단 |", "|---|---|---|",
          "| PatentsView API | 프록시 502 (연결 거부) | Google Patents 검색 |",
          "| EPO OPS (Espacenet) | HTTP 403 | FreePatentsOnline 청구항 원문 |",
          "| Espacenet 웹 | HTTP 403 | 동일 |",
          "| Justia Patents | HTTP 403 (봇 차단) | 동일 |",
          "| Google Patents 상세 페이지 | HTTP 503 (자동질의 차단) | FreePatentsOnline으로 전환해 104건 확보 |",
          "| 일부 제조사 제품 페이지 | HTTP 403/503 | 검색 스니펫 경유 시 신뢰도 '하'로 표기 |", ""]
    open(os.path.join(BASE, "gaps.md"), "w", encoding="utf-8").write("\n".join(L))
    print(f"gaps.md: {len(rows)}건 기록")


if __name__ == "__main__":
    r, p = main()
    render(r, p)
