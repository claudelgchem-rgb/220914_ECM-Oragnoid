# ECMX-002 — Extracellular Matrix material eXplorer

ECM(세포외기질) 소재 개발 분야 개요 · 소재 물질 인벤토리 · **오가노이드 3차원 지지체 필수 물질 문헌 확정** 조사 산출물.

- **실행 ID**: ECMX-002
- **데이터 기준일**: 2026-09-14
- **주 산출물**: `ECMX/ECMX_report.html` (외부 자원 없이 단독으로 열리는 자체 완결형 단일 HTML)
- **부속 데이터**: `ECMX/ECMX_materials.xlsx`

## 구조
| 경로 | 내용 |
|---|---|
| `ECMX/ECMX_report.html` | 주 보고서 (본문 + 자체 제작 SVG 그림) |
| `ECMX/11_essential_materials.md` | M3 오가노이드 지지체 필수 물질 — 논문 근거 |
| `ECMX/12_patent_essentials.md` | M3 특허 독립항 기반 필수 구성요소 |
| `ECMX/essential_items.csv` | 필수 물질 등급표 (E0~E3) |
| `ECMX/essential_matrix.csv` | 조직 × 요구사항 매트릭스 |
| `ECMX/material_inventory.csv` | M2 물질 인벤토리 L1~L9 |
| `ECMX/evidence_ledger.md` | 근거 대장 (논문·특허 전체) |
| `ECMX/gaps.md` | 확보 실패·결측 항목 |
| `ECMX/tools/validate.py` | 스키마·게이트·금지수치·외부자원 자동 검사 |

## 근거 원칙
- 모든 논문 서지는 Europe PMC 직접 조회로 확정했다. 인용 DOI는 전수 대조 검증한다.
- 특허는 청구항 **원문**을 직접 취득해 분석했다. 요약서 기반 추정은 금지한다.
- "필수"라는 표현은 제거·치환·농도반응 실험 근거를 충족한 경우에만 사용한다.
- 본 보고서는 전수조사가 아니며 자유실시(FTO) 판단 근거로 사용할 수 없다.
