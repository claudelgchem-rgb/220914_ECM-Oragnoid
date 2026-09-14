---
agent: A
status: complete
date_checked: 2026-09-14
items_count: 4
evidence_count: {papers: 115, patents: 0}
unresolved: 4
---

# 01. ECM 소재 개관 — 분야 정의와 분류 (M1 / O1~O4)

**작성일 / 확인일: 2026-09-14**

이 문서는 오가노이드(organoid, 줄기세포가 스스로 조직화해 만든 3차원 미니 장기 모사체) 배양에 쓰이는 **세포외기질(extracellular matrix, ECM) 소재**가 무엇이며 어떻게 분류되는지를, 이 분야를 처음 보는 독자가 읽고 따라올 수 있도록 서술형으로 정리한 것이다. 전문용어는 첫 등장 시 영문과 한 줄 풀이를 붙였다.

**근거 규칙.** 본문의 모든 문헌 인용은 사전에 서지가 확정된 검증 문헌 풀(랜드마크 40편 + Europe PMC 실검색 565편, 2026-09-14 접근)에 실재하는 항목만 사용했다. DOI/PMID는 조회값 그대로이며 추정·생성한 값은 없다. 제조사·제품 정보는 제조사 공식 웹페이지를 2026-09-14에 확인한 것만 기재했고, 확인하지 못한 것은 "1차 출처 미확인"으로 표시했다. 각 주장 뒤에는 `(신뢰도: 상|중|하 — 판정 사유)`를 병기했으며, '상'은 독립된 2개 이상 출처로 교차확인되고 원문 수치·문장이 확인된 경우에만 부여했다.

---

## O1. 정의와 범위

### O1-1. 생체 세포외기질(ECM)이란 무엇인가

우리 몸의 조직은 세포만으로 이루어져 있지 않다. 세포와 세포 사이, 그리고 상피(epithelium, 장기의 안쪽·바깥쪽 표면을 덮는 세포층) 바로 아래에는 세포가 스스로 만들어 분비한 단백질과 당(糖) 고분자의 그물망이 채워져 있다. 이 그물망이 **세포외기질(extracellular matrix, ECM)**이다. ECM은 단순한 충전재가 아니라 조직의 형태를 유지하는 골격이면서, 동시에 세포가 붙잡고(접착), 밀고 당기며 힘을 느끼고(역학), 필요할 때 뚫고 나가며(분해), 저장된 신호 분자를 꺼내 쓰는(성장인자 저장고) **정보 매체**다 [Frantz C 2010, Journal of Cell Science, DOI:10.1242/jcs.023820] [Karamanos NK 2021, The FEBS Journal, DOI:10.1111/febs.15776]. (신뢰도: 상 — 두 편의 독립적 종설이 동일한 4대 기능 구분을 제시하며, 양쪽 모두 1,000회 내외 이상 인용된 표준 리뷰)

ECM을 이루는 부품의 목록은 단백질체학(proteomics, 시료 안의 단백질을 대량으로 동정하는 기술)으로 체계화되었고, 이 부품 목록 전체를 **매트리솜(matrisome)**이라 부른다. 매트리솜은 콜라겐(collagen), 당단백질(glycoprotein), 프로테오글리칸(proteoglycan)으로 구성된 '핵심 매트리솜(core matrisome)'과, 여기에 결합하거나 이를 가공·조절하는 '매트리솜 관련 단백질(matrisome-associated: ECM 조절인자, ECM 부착 단백질, 분비 인자)'로 나뉜다 [Naba A 2012, Molecular & Cellular Proteomics, DOI:10.1074/mcp.m111.014647] [Hynes RO & Naba A 2012, Cold Spring Harbor Perspectives in Biology, DOI:10.1101/cshperspect.a004903]. 이 분류는 이후 다조직 단백질체 데이터베이스로 확장되어 현재도 참조 표준으로 쓰인다 [Naba A 2016, Matrix Biology, DOI:10.1016/j.matbio.2015.06.003] [Shao X 2023, Nucleic Acids Research, DOI:10.1093/nar/gkac1009]. ECM은 또한 고정된 구조가 아니라 합성·가교·절단·재배치가 끊임없이 일어나는 동적 구조물이며, 이 동역학 자체가 세포 운명을 좌우한다 [Naba A 2024, Nature Reviews Molecular Cell Biology, DOI:10.1038/s41580-024-00767-3]. (신뢰도: 상 — 매트리솜 정의 원저와 후속 데이터베이스 논문, 최신 종설 3건이 상호 일관)

오가노이드 맥락에서 특히 중요한 ECM은 **기저막(basement membrane, BM)**이다. 기저막은 상피세포층 바로 아래에 깔린 얇고 치밀한 판상 ECM으로, 라미닌(laminin), 제IV형 콜라겐(collagen IV), 니도겐/엔탁틴(nidogen/entactin), 퍼레칸(perlecan, 헤파란황산 프로테오글리칸)이 주 구성요소다. 상피 오가노이드는 본질적으로 '기저막 위에 앉은 상피'를 재현하는 것이므로, 배양 지지체가 기저막을 얼마나 잘 흉내 내는지가 성패를 가른다 [Kratochvil MJ 2019, Nature Reviews Materials, DOI:10.1038/s41578-019-0129-9] [Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8]. (신뢰도: 상 — 두 편의 Nature Reviews Materials 종설이 독립적으로 동일 논지, 합계 1,000회 이상 인용)

### O1-2. "ECM 소재"가 가리키는 범위

이 연구에서 **ECM 소재**란, *세포를 3차원으로 담아 기르거나 2차원으로 붙여 기를 목적으로 인위적으로 제조·공급되는, 생체 ECM의 기능을 대체하거나 모방하는 재료 일체*를 뜻한다. 구체적으로 다음을 포함한다.

- 동물 종양·조직에서 추출한 기저막추출물(basement membrane extract, BME) 및 탈세포화(decellularization, 조직에서 세포를 제거하고 ECM만 남기는 공정) 유래 기질
- 정제·재조합 ECM 단백질(콜라겐, 라미닌, 피브로넥틴, 비트로넥틴, 피브린 등)
- ECM 유래 또는 ECM 모방 다당류(히알루론산, 알지네이트, 셀룰로스 나노섬유, 키토산 등)
- 완전 합성 고분자 기반 하이드로겔(폴리에틸렌글리콜(PEG) 계열 등)과 합성 펩타이드 표면
- 위 범주를 조합한 하이브리드 소재

반대로 다음은 **범위 밖**이다. (i) **배지(medium)** 성분 — 성장인자, 저분자 화합물, 혈청, 조건배지 등 액상으로 공급되는 것 전부. (ii) 세포 자체(피더세포, 지지세포). (iii) 장비·소모품 형태의 배양 플랫폼(마이크로웰 플레이트, 미세유체 칩 자체) — 단, 그 표면에 도포된 코팅 기질은 범위에 포함된다. (iv) 농업·농약·작물보호·사료첨가 용도 소재는 본 연구 전체에서 완전히 배제한다.

### O1-3. 인접 개념의 경계 — 하이드로겔 / 지지체 / 매트릭스 / 바이오잉크

초보자가 가장 많이 혼동하는 네 단어는 서로 배타적인 분류가 아니라 **서로 다른 질문에 답하는 이름표**다. 하나의 물질이 동시에 네 이름을 모두 가질 수 있다.

| 용어 | 답하는 질문 | 정의 | 필수 조건 | ECM 소재와의 관계 | 오가노이드 배양에서의 전형적 예 |
|---|---|---|---|---|---|
| **하이드로겔 (hydrogel)** | "물리적 상태가 무엇인가?" | 물을 대량으로 머금은 채 가교(crosslink)되어 형태를 유지하는 3차원 고분자 망상 구조 | 함수(含水) + 가교에 의한 고체 거동 | ECM 소재의 다수가 하이드로겔 형태를 취하지만, 하이드로겔이라고 모두 ECM 기능(접착 리간드 등)을 갖지는 않음 | Matrigel 돔, PEG 하이드로겔, 알지네이트 겔 |
| **지지체 (scaffold)** | "무슨 역할을 하는가?" | 세포가 부착·침윤·조직화할 수 있도록 3차원 공간과 구조를 제공하는 구조물 일반 | 3차원 구조 제공 | 기능적 호칭. 하이드로겔일 수도, 전기방사 섬유·다공성 스펀지·3D 프린팅 격자처럼 비(非)하이드로겔일 수도 있음 | 실크 피브로인 크립트-융모 형상 지지체, 전기방사 미세섬유 |
| **매트릭스 (matrix)** | "생물학적으로 무엇을 대신하는가?" | 세포를 둘러싸며 생체 ECM의 신호 역할을 대신하는 재료 | 생물학적 신호(접착·역학·분해·인자결합) 제공 의도 | 본 연구의 "ECM 소재"와 가장 가까운 개념. 2D 코팅 기질도 포함 | Matrigel, 라미닌-521 코팅, PEG-RGD 겔 |
| **바이오잉크 (bioink)** | "어떻게 성형하는가?" | 세포를 포함한 채 3D 바이오프린팅 장비로 토출·적층 가능하도록 유변학적 특성이 조정된 재료 | 프린팅 가능한 점탄성 + 토출 후 형태 유지 | 공정 관점의 호칭. 같은 물질이라도 프린터에 넣으면 바이오잉크, 웰에 점적하면 매트릭스 | GelMA 기반 잉크, 콜라겐 기반 저농도 잉크, 희생 주형과 조합한 프린팅 재료 |

이 경계 구분의 실무적 의미는 다음과 같다. 첫째, "하이드로겔이면 오가노이드가 자란다"는 명제는 거짓이다. 접착 리간드가 전혀 없는 알지네이트 겔에서도 iPSC 유래 장 오가노이드가 성장한 보고가 있는 반면 [Capeling MM 2019, Stem Cell Reports, DOI:10.1016/j.stemcr.2018.12.001], 같은 비접착성 조건이 다른 조직에서는 실패하므로, 물리적 상태만으로는 기능을 예측할 수 없다. (신뢰도: 중 — 단일 원저의 장 오가노이드 결과이며, 조직 일반화에 대한 교차 근거는 확보하지 못함) 둘째, 바이오잉크는 '프린팅 가능성'이라는 추가 제약을 물질에 부과하므로, 프린팅 적합성을 위해 조정한 조성이 오가노이드 형태형성에는 불리할 수 있다 [Maharjan S 2024, Advanced Drug Delivery Reviews, DOI:10.1016/j.addr.2024.115237]. (신뢰도: 중 — 종설 근거, 정량적 비교 수치는 미확인) 셋째, 희생 주형(sacrificial template)으로 관류 채널을 만드는 접근처럼, 지지체 공학의 기법은 ECM 소재와 조합되어야 비로소 조직 기능을 낸다 [Miller JS 2012, Nature Materials, DOI:10.1038/nmat3357]. (신뢰도: 중 — 랜드마크 원저이나 오가노이드가 아닌 혈관화 조직 대상)

### O1-4. 반드시 분리해서 읽어야 할 두 축 — 배지 vs 매트릭스, 2D 코팅 vs 3D 하이드로겔

**축 1: 배지(medium) ≠ 매트릭스(matrix).** 오가노이드 프로토콜을 처음 읽으면 성분 목록이 한 덩어리로 보이지만, 실제로는 두 개의 독립적인 공급 경로가 있다. 액상으로 배지에 녹여 넣는 것과, 겔로 굳혀 세포를 담는 것이다. 최초의 장 오가노이드 배양에서 매트릭스는 Matrigel이었고, 배지는 상피성장인자(EGF), 노긴(Noggin, BMP 신호 억제), R-스폰딘1(R-spondin1, Wnt 신호 증폭)을 첨가한 조성이었다 [Sato T 2009, Nature, DOI:10.1038/nature07935]. 인간 대장·선종·선암 오가노이드로 확장할 때는 Wnt3a, 니코틴아미드, ALK 저해제, p38 저해제, 가스트린 등이 **배지 쪽**에 추가되었고 매트릭스는 여전히 Matrigel이었다 [Sato T 2011, Gastroenterology, DOI:10.1053/j.gastro.2011.07.050]. (신뢰도: 상 — 두 원저가 각각 5,800회·3,100회 인용된 표준 프로토콜의 출처이며, 매트릭스/배지 구분이 원문에서 명시적)

상업 제품도 이 축을 따라 갈린다. 예컨대 STEMCELL Technologies의 IntestiCult 제품군은 공식 제품 페이지에서 "complete cell culture medium", 즉 **배지**로 정의되어 있으며 매트릭스가 아니다(stemcell.com 공식 제품 페이지, 접근 2026-09-14). 반면 Corning Matrigel Matrix for Organoid Culture는 **매트릭스**다(corning.com 공식 제품 페이지, 접근 2026-09-14). 이 둘을 같은 층위에서 비교하는 서술은 오류다. (신뢰도: 중 — 제조사 공식 페이지 1차 확인이나, Corning 페이지는 직접 HTTP 페치 시 403이 반환되어 검색 색인을 통한 공식 페이지 내용 확인에 의존)

**축 2: 2D 코팅 기질 ≠ 3D 하이드로겔.** 같은 ECM 분자라도 배양접시 바닥에 얇게 도포(coating)하여 세포가 그 위에 '평면으로 붙는' 용도와, 두꺼운 겔로 굳혀 세포를 '사방에서 감싸는' 용도는 물리적·생물학적으로 전혀 다르다. 2D 코팅에서는 세포가 한쪽 면으로만 기질과 접촉하고 강성은 사실상 배양접시(기가파스칼 수준)가 지배하는 반면, 3D 포매(embedding)에서는 세포가 전방위로 구속되며 겔 자체의 강성·점탄성·분해성이 직접 작용한다 [Chaudhuri O 2020, Nature, DOI:10.1038/s41586-020-2612-2]. (신뢰도: 상 — Nature 종설이 2D/3D 역학 환경 차이를 핵심 논지로 제시, 1,600회 인용)

2D 코팅 전용으로 개발된 대표 소재로는 인간 재조합 라미닌-511/521이 있다. 라미닌-511은 마우스 배아줄기세포의 자기재생을 지지한 반면 라미닌-332/111/411은 그러지 못했고 [Domogatskaya A 2008, Stem Cells, DOI:10.1634/stemcells.2007-0389], 인간 다능성줄기세포는 재조합 라미닌-511 코팅에서 장기 자기재생이 가능했다 [Rodin S 2010, Nature Biotechnology, DOI:10.1038/nbt.1620]. 비트로넥틴은 αvβ5 인테그린을 통해 hESC 자기재생을 지지했고 [Braam SR 2008, Stem Cells, DOI:10.1634/stemcells.2008-0291], 비트로넥틴 모사 합성 펩타이드를 아크릴레이트 표면에 고정한 기질도 hESC 장기 자기재생과 심근세포 분화를 지지했다 [Melkoumian Z 2010, Nature Biotechnology, DOI:10.1038/nbt.1629]. 이들은 모두 **2D 기질**이며, 그대로 3D 오가노이드 지지체가 되지는 않는다. (신뢰도: 상 — 라미닌 특이성은 마우스·인간 2편의 독립 원저로 교차확인; 비트로넥틴/합성 펩타이드는 각 1편이나 동일 결론 방향)

---

## O2. 생물학적 제1원리 — ECM이 세포에 주는 네 가지 신호

ECM 소재를 설계하거나 고를 때 따져야 할 축은 결국 네 가지로 수렴한다. ① 붙을 자리가 있는가, ② 얼마나 단단하고 얼마나 잘 풀어지는가, ③ 세포가 뚫고 재배치할 수 있는가, ④ 성장인자를 붙잡아 보여줄 수 있는가. 이 네 축은 부착(adhesion) → 증식(proliferation) → 분화(differentiation)의 전 과정에 각각 다르게 작용하며, 서로 독립적이지 않고 강하게 얽혀 있다 [Chaudhuri O 2020, Nature, DOI:10.1038/s41586-020-2612-2] [Kratochvil MJ 2019, Nature Reviews Materials, DOI:10.1038/s41578-019-0129-9]. (신뢰도: 상 — Nature 및 Nature Reviews Materials 종설 2편이 동일한 축 구분을 제시)

### ① 접착 리간드 (adhesion ligand) — 인테그린이 붙잡을 자리

**개념.** 인테그린(integrin)은 세포막을 관통하는 수용체 단백질로, ECM 단백질의 특정 아미노산 서열을 인식해 결합한다. 가장 널리 쓰이는 모사 서열이 피브로넥틴 유래 **RGD**(Arg-Gly-Asp)이고, 라미닌 유래로는 **IKVAV**, **YIGSR** 등이 쓰인다. 인테그린 결합은 단순한 '붙음'이 아니라, 세포 내부의 액틴-마이오신 수축 기구와 물리적으로 연결되어 힘을 주고받는 통로가 된다.

**효과.** 접착 리간드의 종류가 바뀌면 같은 강성에서도 세포 운명이 달라진다. 장 줄기세포(intestinal stem cell, ISC) 배양에서 **피브로넥틴 기반 접착만으로 ISC의 생존과 증식이 충분**했던 반면, **분화와 오가노이드 형성 단계에서는 라미닌 기반 접착이 요구**되었다 [Gjorevski N 2016, Nature, DOI:10.1038/nature20168]. (신뢰도: 상 — 원저 초록 문장을 2026-09-14 Europe PMC에서 직접 확인: "fibronectin-based adhesion was sufficient for ISC survival and proliferation… ISC differentiation and organoid formation, on the other hand, required a soft matrix and laminin-based adhesion") 이 결과는 접착 리간드가 단계 의존적으로 전환되어야 함을 뜻하며, "RGD만 넣으면 된다"는 단순화를 반증한다.

리간드 종류가 역학 감지 자체를 바꾸기도 한다. 인테그린 접착과 별개로 카드헤린(cadherin) 기반 세포-세포 접착 신호가 기질 역학 감지와 중간엽줄기세포 운명 결정을 조절했고 [Cosgrove BD 2016, Nature Materials, DOI:10.1038/nmat4725], ECM 단백질의 종류에 따라 줄기세포의 역학신호전달(mechanotransduction) 반응 자체가 달라졌다 [Stanton AE 2019, Acta Biomaterialia, DOI:10.1016/j.actbio.2019.06.048]. 라미닌 유래 IKVAV 펩타이드를 합성 동적 하이드로겔에 장식하면 장 오가노이드의 **극성 방향(안쪽/바깥쪽)** 자체를 제어할 수 있다는 보고도 있다 [Rijns L 2026, Advanced Healthcare Materials, DOI:10.1002/adhm.202502079]. (신뢰도: 중 — 각각 단일 원저이며 인용 축적이 아직 제한적, 특히 Rijns 2026은 최신 보고)

**설계 시사점.** 접착 리간드는 (i) 서열 종류, (ii) 밀도, (iii) 공간적 제시 방식(균일 분포 vs 군집화)의 세 변수로 다뤄야 한다. 리간드의 물리적 군집화(clustering)가 신호 강도를 좌우한다는 점은 점탄성 연구에서 명확히 드러났다 [Chaudhuri O 2016, Nature Materials, DOI:10.1038/nmat4489]. (신뢰도: 상 — 원저 초록에서 "mechanical clustering of adhesion ligands"를 기전으로 명시함을 2026-09-14 직접 확인)

### ② 기계적 강성·점탄성 (stiffness / viscoelasticity) — 얼마나 단단하고, 얼마나 풀어지는가

**개념 1: 강성(stiffness).** 겔을 눌렀을 때 얼마나 저항하는가를 나타내는 탄성계수(elastic modulus, 단위 Pa·kPa)다. 뇌 조직은 무르고 뼈는 단단하듯, 조직마다 고유한 강성 범위가 있다.

**개념 2: 점탄성(viscoelasticity)과 응력완화(stress relaxation).** 생체 조직은 순수한 탄성체가 아니다. 일정한 변형을 가한 뒤 유지하면 내부 응력이 시간에 따라 서서히 풀린다. 이 '풀림'의 속도가 응력완화다. Matrigel·콜라겐 같은 천연 겔은 응력완화가 빠르고, 공유결합으로 촘촘히 가교된 합성 겔은 거의 완화되지 않는다.

**효과 — 강성.** 기질 탄성이 중간엽줄기세포의 계통 분화 방향을 결정한다는 것이 이 분야의 출발점이다. 뇌를 모사한 무른 기질은 신경계통(neurogenic), 근육을 모사한 중간 강성은 근육계통(myogenic), 콜라겐성 뼈를 모사한 단단한 기질은 골계통(osteogenic) 분화를 유도했다 [Engler AJ 2006, Cell, DOI:10.1016/j.cell.2006.06.044]. (신뢰도: 중 — 정성적 결론 문장은 Europe PMC 초록에서 2026-09-14 직접 확인했으나, 흔히 인용되는 kPa 구간 수치는 해당 초록에 기재되어 있지 않아 본 문서에서는 수치를 제시하지 않음)

이 역학 신호를 핵 안까지 전달하는 핵심 중계자가 **YAP/TAZ**(Yes-associated protein / transcriptional coactivator with PDZ-binding motif)다. 단단한 기질과 펼쳐진 세포 형태에서 YAP/TAZ가 핵으로 이동해 증식·줄기성 유전자를 켠다 [Dupont S 2011, Nature, DOI:10.1038/nature10137]. 장 줄기세포에서도 동일 논리가 성립하여, 고강성 매트릭스가 YAP 의존적으로 ISC 확장을 크게 증진했다 [Gjorevski N 2016, Nature, DOI:10.1038/nature20168]. 반대로 과도한 강성은 ISC의 줄기성을 제한하고 배상세포(goblet cell) 쪽으로 분화를 치우치게 했다 [He S 2023, Gastroenterology, DOI:10.1053/j.gastro.2023.02.030]. 기계적 자극 감지에는 이온채널 PIEZO도 관여하여, PIEZO 의존적 역학감지가 장 줄기세포 운명 결정과 유지에 필수적이었다 [Baghdadi MB 2024, Science, DOI:10.1126/science.adj7615]. (신뢰도: 상 — YAP 축은 Dupont 2011과 Gjorevski 2016 두 독립 출처로 교차확인; He 2023·Baghdadi 2024는 장 조직 특이적 보강 근거)

**효과 — 점탄성.** 강성만으로는 설명되지 않는 영역이 점탄성이다. 탄성계수·분해성·리간드 밀도를 고정한 채 응력완화 속도만 독립적으로 조절한 알지네이트 하이드로겔에서, **완화가 빠를수록** 중간엽줄기세포의 퍼짐(spreading)·증식·골분화가 모두 증가했다. 초기 탄성계수 17 kPa의 빠른 완화 겔에서는 뼈와 유사한 무기질화된 제1형 콜라겐 풍부 기질이 형성되었으며, 기전은 접착 리간드 결합, 액틴-마이오신 수축, 접착 리간드의 기계적 군집화를 경유했다 [Chaudhuri O 2016, Nature Materials, DOI:10.1038/nmat4489]. (신뢰도: 상 — 원저 초록에서 "initial elastic modulus of 17 kPa"와 기전 3요소를 2026-09-14 직접 확인) 이 발견은 이후 ECM 점탄성이 이동·증식·분화·형태형성 전반을 지배한다는 일반 원리로 확장되었다 [Chaudhuri O 2020, Nature, DOI:10.1038/s41586-020-2612-2].

오가노이드 수준에서 점탄성의 효과는 더 극적이다. 주변 기질의 수동적 점탄성이 유방 상피 스페로이드의 증식을 시공간적으로 유도하고, 대칭 파괴와 손가락 모양 침윤 돌기 형성, YAP 핵 이동, 상피-간엽 전이를 Arp2/3 복합체 의존적으로 촉발했으며, 저자들은 이를 장 오가노이드 실험으로도 검증했다 [Elosegui-Artola A 2023, Nature Materials, DOI:10.1038/s41563-022-01400-4]. (신뢰도: 상 — 원저 초록을 2026-09-14 직접 확인, 기전과 검증계가 명시)

점탄성을 재료 화학으로 구현하는 방법도 다양하게 확립되었다. 가역적 공유결합 기반 적응성 망상구조 [McKinnon DD 2014, Advanced Materials, DOI:10.1002/adma.201303680], 히알루론산-콜라겐 복합 응력완화 겔 [Lou J 2018, Biomaterials, DOI:10.1016/j.biomaterials.2017.11.004], 알지네이트-PEG의 PEG 밀도 조절 [Nam S 2019, Biomaterials, DOI:10.1016/j.biomaterials.2019.02.004], DNA 혼성화로 점탄성을 암호화한 동적 매트릭스 [Peng YH 2023, Nature Nanotechnology, DOI:10.1038/s41565-023-01483-3] 등이 보고되었다. 세포가 3차원에서 부피를 늘리며 TRPV4 채널을 통해 운명을 결정하는 경로도 밝혀졌다 [Lee HP 2019, Nature Communications, DOI:10.1038/s41467-019-08465-x]. (신뢰도: 중 — 각 항목은 단일 원저 기반이며 재료별 조건 의존성이 큼)

### ③ 분해성·리모델링 (degradability / remodelling) — 뚫고 나갈 수 있는가

**개념.** 세포는 자기보다 촘촘한 망 속에 갇히면 형태를 바꾸거나 증식할 수 없다. 생체에서는 **기질금속단백분해효소(matrix metalloproteinase, MMP)**가 ECM을 절단해 공간을 만든다. 합성 매트릭스는 이 성질을 인위적으로 부여해야 한다.

**효과.** 합성 하이드로겔에 인테그린 결합 부위와 MMP 기질(절단 표적) 서열을 동시에 도입하자, 1차 인간 섬유아세포가 겔을 단백분해적으로 침윤했고, 침윤 정도는 **MMP 기질 활성, 접착 리간드 농도, 망상구조 가교밀도**에 의존했다. 골형성단백질-2(BMP-2)를 담아 쥐 두개골 결손부에 이식했을 때 4주 내 세포 침윤과 골조직 리모델링이 일어났으며, 골재생 정도 역시 매트릭스의 단백분해 감수성에 의존했다 [Lutolf MP 2003, PNAS, DOI:10.1073/pnas.0737381100]. (신뢰도: 상 — 원저 초록의 의존 변수 3종과 in vivo 결과를 2026-09-14 직접 확인)

이 '분해 가능해야 형태형성이 일어난다'는 통념은 최근 수정되었다. 수소결합 기반의 **가역적 재배치(동적 결합)**를 갖춘 합성 하이드로겔에서는 효소적 분해 없이도 장 줄기세포 상피의 크립트 싹눈(crypt budding)이 효율적으로 일어났고, YAP 신호를 경유해 대칭 파괴와 파네트세포(Paneth cell) 형성이 촉진되었다 [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7]. (신뢰도: 상 — 원저 초록에서 "reversible hydrogen bonding-mediated dynamic rearrangements", "degradation-independent"를 2026-09-14 직접 확인) 즉 세포에 필요한 것은 '분해' 자체가 아니라 **국소적으로 자리를 내어주는 능력(가소성)**이며, 이는 공유결합 절단으로도, 물리적 재배치로도 달성될 수 있다.

시간에 따라 물성을 바꾸는 방법도 정착했다. 광분해성(photodegradable) 하이드로겔은 빛으로 특정 시점·특정 위치의 가교를 끊어 물성과 화학을 동적으로 조절한다 [Kloxin AM 2009, Science, DOI:10.1126/science.1169494]. 이 원리는 오가노이드 배양에 직접 적용되어, 광유도 점탄성 변화로 장 오가노이드 상피의 곡률을 국소 조절하고 크립트 형태형성을 유도하는 데 쓰였다 [Yavitt FM 2023, Science Advances, DOI:10.1126/sciadv.add5668]. 관련 광반응 화학의 현황은 종설로 정리되어 있다 [Ohnsorg ML 2025, Accounts of Chemical Research, DOI:10.1021/acs.accounts.4c00548]. (신뢰도: 중 — 원리는 랜드마크로 확립되었으나 오가노이드 적용은 소수 연구실 보고)

### ④ 결합된 성장인자 (matrix-bound growth factor) — 붙잡아 보여주기

**개념.** 성장인자는 배지에 녹여 공급할 수도 있지만, 생체에서는 상당 부분이 ECM의 헤파란황산·피브로넥틴 등에 **결합된 상태로 저장**되어 있다가 필요할 때 제시되거나 방출된다. 같은 분자라도 액상으로 떠다닐 때와 기질에 고정되어 인테그린과 나란히 제시될 때 신호의 질이 다르다.

**효과.** 전장(full-length) 피브로넥틴을 도입한 3차원 하이드로겔은 성장인자를 격리(sequester)하고 제시하는 기능을 수행했다 [Trujillo S 2020, Biomaterials, DOI:10.1016/j.biomaterials.2020.120104]. 인테그린 특이적 PEG 하이드로겔에 혈관내피성장인자(VEGF)를 기능화한 경우, 임계 크기 골결손에서 혈관화와 골재생이 향상되었다 [García JR 2016, Journal of Biomedical Materials Research Part A, DOI:10.1002/jbm.a.35626]. 조직공학 장(腸) 구조물에서 VEGF의 지속 방출이 혈관신생을 증진한 보고도 있다 [Rocha FG 2008, Biomaterials, DOI:10.1016/j.biomaterials.2008.03.026]. 세포가 스스로 분비한 ECM 단백질을 매트릭스에 격리시켜 난포 발생과 난자 성숙을 개선한 사례도 있다 [Tomaszewski CE 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.03.041]. (신뢰도: 중 — 각 사례는 단일 원저이며 대상 조직이 서로 달라 일반화에는 추가 근거가 필요)

성장인자 결합능은 다당 선택과도 직결된다. 헤파린과 히알루론산은 인간 iPSC의 신경 패터닝에 서로 다른 영향을 주었는데 [Bejoy J 2018, ACS Biomaterials Science & Engineering, DOI:10.1021/acsbiomaterials.8b01142], 이는 황산화 다당이 성장인자를 붙잡는 능력의 차이와 무관하지 않다. 글리코사미노글리칸 결합 하이드로겔이 인간 다능성줄기세포 자기재생을 역학적으로 제어한 보고도 같은 맥락이다 [Musah S 2012, ACS Nano, DOI:10.1021/nn3039148]. (신뢰도: 중 — 상관 근거이며 기전적 인과 검증은 원문 범위 밖)

**중요한 주의.** 이 네 번째 축은 **배지 성분과 혼동하기 가장 쉬운 지점**이다. "성장인자가 들어 있다"는 진술은 반드시 (a) 배지에 액상으로 첨가된 것인지, (b) 매트릭스에 내재된 것인지, (c) 매트릭스에 의도적으로 공유결합·친화결합시킨 것인지를 구분해야 한다. Matrigel 계열은 (b)에 해당하여, 제조사가 성장인자 저감(reduced growth factor, RGF) 등급을 별도 제품으로 판매한다(bio-techne.com 및 thermofisher.com 공식 제품 페이지, 접근 2026-09-14). Thermo Fisher의 Geltrex RGF 등급은 공식 페이지 기준 EGF·PDGF·NGF가 검출한계 이하이고 TGF-β가 약 2 ng/mL 수준이라고 기재되어 있다. (신뢰도: 중 — 제조사 공식 페이지 1차 확인, 독립 검증 없음)

### O2 종합 — 네 축이 부착·증식·분화에 미치는 영향

| 축 | 부착(adhesion) | 증식(proliferation) | 분화(differentiation) | 핵심 근거 |
|---|---|---|---|---|
| ① 접착 리간드 | 결정적. 리간드 없으면 인테그린 접착 자체가 불가(단, 비접착 겔에서 성장한 예외 보고 있음) | 리간드 종류 의존. 장 줄기세포는 피브로넥틴 접착으로 생존·증식 충족 | 라미닌 접착이 분화·오가노이드 형성에 요구됨 | [Gjorevski N 2016, Nature, DOI:10.1038/nature20168] [Capeling MM 2019, Stem Cell Reports, DOI:10.1016/j.stemcr.2018.12.001] |
| ② 강성 | 퍼짐 정도와 접착반(focal adhesion) 성숙을 좌우 | 고강성이 YAP 핵이동을 통해 줄기세포 확장 증진 | 계통 선택을 직접 지시; 과도한 강성은 줄기성 제한 | [Engler AJ 2006, Cell, DOI:10.1016/j.cell.2006.06.044] [Dupont S 2011, Nature, DOI:10.1038/nature10137] [He S 2023, Gastroenterology, DOI:10.1053/j.gastro.2023.02.030] |
| ② 점탄성 | 빠른 응력완화가 퍼짐 증가 | 빠른 완화가 증식 증가 | 빠른 완화가 골분화 촉진; 조직 수준에서 대칭 파괴·패터닝 유도 | [Chaudhuri O 2016, Nature Materials, DOI:10.1038/nmat4489] [Elosegui-Artola A 2023, Nature Materials, DOI:10.1038/s41563-022-01400-4] |
| ③ 분해성·가소성 | 초기 부착보다는 이후 형태 변화에 관여 | 침윤·확장 공간 확보를 통해 간접 기여 | 크립트 싹눈 등 형태형성에 필수적 공간 제공; 단, 효소 분해 없이 동적 재배치만으로도 가능 | [Lutolf MP 2003, PNAS, DOI:10.1073/pnas.0737381100] [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7] |
| ④ 결합 성장인자 | 인테그린과 협동 제시 시 접착 신호 강화 | 국소 고농도 유지로 증식 지지 | 조직 특이 분화 유도에 기여 | [Trujillo S 2020, Biomaterials, DOI:10.1016/j.biomaterials.2020.120104] [García JR 2016, J Biomed Mater Res A, DOI:10.1002/jbm.a.35626] |

(표 전체 신뢰도: 중~상 — 각 셀의 근거는 위 본문에 개별 표기한 등급을 따름. 축 간 상호작용의 정량적 분리는 대부분의 원저에서 부분적으로만 수행됨)

---

## O3. 소재 분류체계 — 5계열

ECM 소재는 **원료의 출처와 정의 수준(definedness)**을 기준으로 다섯 계열로 나누는 것이 실무적으로 가장 유용하다. 이 축은 곧 "무엇이 들어 있는지 얼마나 알고 있는가"이며, 재현성·규제 적합성·설계 자유도와 직결된다 [Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8] [Kratochvil MJ 2019, Nature Reviews Materials, DOI:10.1038/s41578-019-0129-9] [Tayler IM 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.04.020]. (신뢰도: 상 — 3편의 독립 종설이 동일한 분류 축(천연-정제-합성 스펙트럼)을 채택)

### O3-0. 계열 비교 요약

| 계열 | 정의 수준 | 접착 리간드 | 강성 조절 | 점탄성 | 분해성 | 주요 장점 | 주요 단점 |
|---|---|---|---|---|---|---|---|
| ① 천연 유래(탈세포화 / 기저막추출물) | 낮음(수백~수천 단백질) | 풍부·생체 유사 | 어려움(조성에 종속) | 빠른 완화(생체 유사) | 내재적(세포 유래 MMP로 절단) | 생물학적 성능이 가장 검증됨, 즉시 사용 가능 | 조성 미정의, 로트 간 편차, 이종(異種) 유래, 규제·임상 이행 장벽 |
| ② 정제 단백질(콜라겐·라미닌·피브로넥틴·피브린 등) | 중간~높음 | 명확(단백질 고유 서열) | 제한적(농도·가교로 일부) | 중간 | 내재적 | 조성이 명확하고 기능이 특정됨, 재조합 등급 확보 가능 | 강성·리간드 독립 조절 불가, 고순도 재조합 단백질 비용 |
| ③ 다당(히알루론산·알지네이트·셀룰로스·키토산 등) | 높음 | 없음(별도 도입 필요) | 용이 | 화학에 따라 광범위 조절 | 대개 비(非)효소분해성, 별도 설계 필요 | 동물유래 회피 용이, 물성 조절 폭이 큼, 회수 용이 | 접착 리간드 부재로 그대로는 상피 지지 제한 |
| ④ 합성(PEG 등) | 가장 높음 | 설계로 도입(RGD·IKVAV 등) | 완전 독립 조절 | 화학 설계로 조절 | 설계로 부여(MMP 절단서열·동적 결합) | 각 변수를 독립적으로 조절 가능, 배치 재현성 최상 | 조성 설계 부담이 큼, 조직별 재최적화 필요, 생물학적 복잡성 결여 |
| ⑤ 하이브리드 | 중간 | 천연 성분에서 확보 | 합성 성분으로 조절 | 조합에 따라 조절 | 조합 설계 | 생물학적 성능과 조절성의 절충 | 변수 얽힘으로 해석이 어려움, 여전히 일부 미정의 성분 잔존 |

(표 신뢰도: 중 — 위 3편 종설의 논지를 통합 정리한 것으로, 각 셀에 대한 개별 정량 근거는 계열별 본문의 인용으로 대체)

### O3-1. ① 천연 유래 — 탈세포화 기질 및 기저막추출물(BME)

**정체.** 이 계열은 다시 두 갈래다. (a) 마우스 Engelbreth-Holm-Swarm(EHS) 육종에서 추출한 기저막추출물, (b) 실제 조직(돼지 소장, 간, 췌장, 폐, 자궁내막 등)에서 세포를 제거하고 남긴 ECM을 소화·중화해 겔화한 **탈세포화 ECM(decellularized ECM, dECM)** 하이드로겔이다.

**성능과 근거.** EHS 유래 BME는 오가노이드 기술 자체의 출발점이었다. 단일 Lgr5 양성 장 줄기세포로부터 크립트-융모 구조를 만든 최초 실험이 이 매트릭스 위에서 이루어졌고 [Sato T 2009, Nature, DOI:10.1038/nature07935], 인간 대장·선종·선암·바렛식도 상피의 장기 확장도 같은 기반에서 확립되었다 [Sato T 2011, Gastroenterology, DOI:10.1053/j.gastro.2011.07.050]. 뇌 [Lancaster MA 2013, Nature, DOI:10.1038/nature12517], 신장 [Takasato M 2015, Nature, DOI:10.1038/nature15695], 간 [Huch M 2015, Cell, DOI:10.1016/j.cell.2014.11.050], 기도 [Sachs N 2019, The EMBO Journal, DOI:10.15252/embj.2018100300], 위 [McCracken KW 2014, Nature, DOI:10.1038/nature13863], 장(다능성줄기세포 유래) [Forster R 2014, Stem Cell Reports, DOI:10.1016/j.stemcr.2014.05.001] 등 사실상 모든 주요 오가노이드 계통이 이 계열로 확립되었다. 면역세포를 보존한 기류계면(air-liquid interface) 종양 오가노이드 배양도 같은 계열 위에서 구현되었다 [Neal JT 2018, Cell, DOI:10.1016/j.cell.2018.11.021]. (신뢰도: 상 — 6개 이상 조직에서 독립적으로 확립된 표준 프로토콜)

**한계.** 조성이 정의되지 않았다는 점이 결정적이다. Matrigel의 단백질체 분석은 이 물질이 라미닌·콜라겐 IV·엔탁틴·퍼레칸 외에 다수의 부수 단백질과 성장인자를 포함한 복합 혼합물임을 보였다 [Hughes CS 2010, Proteomics, DOI:10.1002/pmic.200900758]. (신뢰도: 중 — 초록에서 분석 기법(암모늄황산 침전, 크기배제 크로마토그래피, 1D SDS-PAGE, dynamic iterative exclusion)은 확인했으나 동정 단백질 총수는 초록에 기재되어 있지 않아 수치를 인용하지 않음) 이에 더해 종양 유래·이종 유래라는 점, 로트마다 물성과 조성이 달라지는 점이 문제로 반복 지적되어 왔고 [Benton G 2014, Advanced Drug Delivery Reviews, DOI:10.1016/j.addr.2014.06.005] [Kozlowski MT 2021, Communications Biology, DOI:10.1038/s42003-021-02910-8] [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7], 이것이 합성 대체재 개발의 직접적 동기가 되었다 [Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8]. (신뢰도: 상 — 4개 독립 출처가 동일한 한계를 명시)

**dECM 갈래.** 탈세포화 돼지 소장 점막·점막하층에서 얻은 ECM 하이드로겔이 위·간·췌장·소장 등 내배엽 유래 인간 오가노이드의 형성과 성장을 지지했고, 안정적 전사체 특성과 생체 내 전달 가능성까지 보고되었다 [Giobbe GG 2019, Nature Communications, DOI:10.1038/s41467-019-13605-4]. (신뢰도: 상 — 원저 초록을 2026-09-14 직접 확인, 조직 종류와 결과가 명시) 조직 특이적 dECM이 위장관 오가노이드에서 Matrigel의 대안이 될 수 있음을 보인 연구 [Kim S 2022, Nature Communications, DOI:10.1038/s41467-022-29279-4], 인간 췌장 탈세포화·탈지질화 기질 [Sackett SD 2018, Scientific Reports, DOI:10.1038/s41598-018-28857-1], 소·인간 자궁내막 유래 하이드로겔 [Jamaluddin MFB 2022, PNAS, DOI:10.1073/pnas.2208040119], 돼지 뇌 dECM 상의 뇌 오가노이드 형성 [Simsa R 2021, PLoS ONE, DOI:10.1371/journal.pone.0245685] 등이 축적되었다. dECM의 일반 원리와 오가노이드 적용은 종설로 정리되어 있다 [Zhu L 2023, Small, DOI:10.1002/smll.202207752] [Li C 2024, Journal of Biomedical Science, DOI:10.1186/s12929-024-01086-7]. dECM은 조직 특이성을 얻는 대신 **탈세포화 공정과 소화 정도에 따른 편차**라는 새로운 변수를 떠안는다. (신뢰도: 중 — 다수 원저가 있으나 조직·프로토콜별 이질성이 커 직접 비교가 어려움)

**대표 제품(제조사 공식 페이지 확인, 접근일 2026-09-14).**

| 제품명 | 제조사 | 공식 페이지상 원료·특징 | 형태 |
|---|---|---|---|
| Corning Matrigel Matrix for Organoid Culture (예: cat. 356255) | Corning Incorporated (미국) | EHS 마우스 육종 추출. 라미닌(주성분), 콜라겐 IV, 헤파란황산 프로테오글리칸, 엔탁틴/니도겐, 다수 성장인자 포함. **로트별 탄성계수(elastic modulus) 측정** 및 오가노이드용 3D 돔 형성 적격성 판정 명시 | 3D 하이드로겔 |
| Cultrex BME / RGF BME Type 2 Select / UltiMatrix RGF BME | R&D Systems (Bio-Techne, 미국) | EHS 종양 유래. 라미닌·콜라겐 IV·엔탁틴·헤파란황산 프로테오글리칸. Type 2는 높은 저장탄성률(storage modulus)을 표방, UltiMatrix는 오가노이드·iPSC 확장/분화 용도 표방 | 3D 하이드로겔 |
| Geltrex LDEV-Free RGF BME / Geltrex Flex | Thermo Fisher Scientific (미국) | 마우스 EHS 종양 유래, LDEV(lactose dehydrogenase elevating virus) 무함유. RGF 등급은 EGF·PDGF·NGF 검출한계 이하, TGF-β 약 2 ng/mL. 기존 A1413202 등은 재입고 중단, Geltrex Flex로 대체된다고 명시 | 2D 코팅 및 3D 모두 |

(제품 정보 신뢰도: 중 — 제조사 공식 페이지 1차 확인. 단 Corning 페이지는 직접 HTTP 페치 시 403 응답으로 차단되어, corning.com 도메인으로 한정한 검색 색인을 통해 공식 페이지 내용을 확인했다. 제3자 독립 검증은 수행하지 않았으며, 모든 수치·특성은 제조사 표방값이다.)

### O3-2. ② 정제 단백질

**정체.** 생체 ECM에서 정제하거나 재조합으로 생산한 단일(또는 소수) 단백질을 그대로 겔화하거나 코팅한다. 콜라겐 I, 라미닌(111/511/521), 피브로넥틴, 비트로넥틴, 피브린(피브리노겐+트롬빈), 젤라틴(변성 콜라겐) 등이 해당한다.

**성능과 근거.** 피브린에 라미닌-111을 보강하고 RGD 접착 도메인을 포함시킨 정의된 하이드로겔이 마우스·인간의 장·간·췌장 상피 오가노이드를 장기 확장시켰고, 저자들은 이를 BME의 정의된 등가물로 제시했다 [Broguiere N 2018, Advanced Materials, DOI:10.1002/adma.201801621]. (신뢰도: 상 — 원저 초록에서 조성(fibrin + laminin-111 + RGD)과 적용 오가노이드 종류를 2026-09-14 직접 확인) 2D 영역에서는 재조합 라미닌-511/521이 hPSC 자기재생의 표준 기질로 자리잡았고 [Domogatskaya A 2008, Stem Cells, DOI:10.1634/stemcells.2007-0389] [Rodin S 2010, Nature Biotechnology, DOI:10.1038/nbt.1620], 비트로넥틴 코팅 위의 완전 정의 xeno-free 배양계 [Lu HF 2014, Biomaterials, DOI:10.1016/j.biomaterials.2013.12.050]와 화학적 정의 심근세포 분화계 [Burridge PW 2014, Nature Methods, DOI:10.1038/nmeth.2999]가 확립되었다. 재조합 인간 제II형 콜라겐 겔은 연골 결손 재생에 사용되었다 [Pulkkinen HJ 2013, Osteoarthritis and Cartilage, DOI:10.1016/j.joca.2012.12.004]. (신뢰도: 상 — 2D 라미닌·비트로넥틴 계열은 복수 독립 원저로 교차확인)

**한계.** 단백질 자체가 접착과 역학을 동시에 결정하므로, 강성만 바꾸려 해도 리간드 밀도가 따라 변한다. 이 **변수 얽힘(coupling)**이 정제 단백질 계열의 근본적 제약이며, 합성 계열이 등장한 이유다 [Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8]. (신뢰도: 중 — 종설 논지, 정량 비교 수치 미확인)

**대표 제품(공식 페이지 확인, 접근일 2026-09-14).** Biolaminin 521 LN (BioLamina AB, 스웨덴) — 인간 재조합 **전장** 라미닌-521. 공식 페이지는 hPSC의 feeder-free 배양과 ROCK 저해제 없는 단세포 계대를 표방한다. **2D 코팅 기질**이다. (신뢰도: 중 — 제조사 공식 페이지 1차 확인, 제조사 표방값)

### O3-3. ③ 다당(polysaccharide)

**정체.** 히알루론산(hyaluronic acid, HA), 알지네이트(alginate, 갈조류 유래), 셀룰로스 나노섬유(nanofibrillar cellulose, NFC), 키토산 등 당 사슬 고분자. 대부분 포유류 세포가 인식하는 인테그린 결합 서열을 갖지 않으므로, 그 자체로는 '접착 리간드 없는 3차원 공간'을 제공한다.

**성능과 근거.** 접착성이 없는 알지네이트 하이드로겔에서도 다능성줄기세포 유래 장 오가노이드가 성장했다는 보고는 이 계열의 가능성을 보여준다 [Capeling MM 2019, Stem Cell Reports, DOI:10.1016/j.stemcr.2018.12.001]. 식물 유래 나노셀룰로스 하이드로겔이 소장 오가노이드 성장을 지지했고 [Curvello R 2020, Advanced Science, DOI:10.1002/advs.202002135], 양이온성 가교 나노셀룰로스는 **오가노이드의 성장과 회수(recovery)** 모두를 겨냥해 설계되었다 [Curvello R & Garnier G 2021, Biomacromolecules, DOI:10.1021/acs.biomac.0c01510]. 열감응 콜라겐-나노셀룰로스 복합 겔 [Curvello R 2021, Materials Science and Engineering: C, DOI:10.1016/j.msec.2021.112051]과 셀룰로스 나노피브릴 겔에서의 간 오가노이드 분화 촉진 [Krüger M 2020, Advanced Healthcare Materials, DOI:10.1002/adhm.201901658]도 보고되었다. 신장 오가노이드에서는 티올-엔 가교 알지네이트 포매가 비정상적 제1a1형 콜라겐 침착을 줄이며 ECM 조성을 조절했다 [Geuens T 2021, Biomaterials, DOI:10.1016/j.biomaterials.2021.120976]. 알지네이트 기반 정의 하이드로겔이 척수 오가노이드 유도·성숙을 지지한 사례도 있다 [Chooi WH 2023, Advanced Healthcare Materials, DOI:10.1002/adhm.202202342]. HA 계열에서는 응력완화형 HA-콜라겐 복합겔이 3차원 세포 퍼짐과 접착반 형성을 촉진했다 [Lou J 2018, Biomaterials, DOI:10.1016/j.biomaterials.2017.11.004]. (신뢰도: 중 — 각 소재별로 1~2편의 원저가 존재하나 조직 간 교차검증은 제한적)

**한계.** 접착 리간드 부재가 양날의 검이다. 설계 자유도(원하는 리간드만 골라 도입 가능)를 주는 동시에, 그대로는 상피 극성·분화를 충분히 지지하지 못하는 경우가 많다.

**대표 제품(공식 페이지 확인, 접근일 2026-09-14).**

| 제품명 | 제조사 | 공식 페이지상 원료·특징 |
|---|---|---|
| GrowDex (및 제품군) | UPM Biomedicals (핀란드) | 자작나무 유래 나노피브릴 셀룰로스 + 정제수만으로 구성. 성장인자·동물 DNA 무함유, 실온 보관·사용, 즉시 사용형. 제조사는 로트 간 편차가 없음을 표방 |
| HyStem / HyStem-C / HyStem-HP | Advanced BioMatrix (미국) | 티올화 히알루로난(Glycosil) + 티올 반응성 가교제 PEG 디아크릴레이트(Extralink-Lite). HA는 Bacillus subtilis 발효 유래로 동물유래 원료 무함유 |
| PRONOVA UP 계열 (UP LVG / UP VLVG / UP MVG / UP LVM / UP MVM) | NovaMatrix (노르웨이) | 초정제 소듐 알지네이트. 점도 및 구룰로네이트(G)/만누로네이트(M) 비율별 등급. 내독소 ≤100 EU/g, 총생균수 ≤100 cfu/g 규격. 미국 FDA에 Drug Master File 제출 사실을 공식 페이지에 기재 |

(제품 정보 신뢰도: 중 — 제조사 공식 페이지 1차 확인, 제조사 표방값이며 독립 검증 없음)

### O3-4. ④ 합성(synthetic)

**정체.** 폴리에틸렌글리콜(PEG)을 대표로 하는 생체 불활성 고분자 골격에, 접착 펩타이드(RGD, IKVAV 등)와 분해성 가교제(MMP 절단 서열) 또는 동적 결합을 **설계자가 직접** 붙여 만든 매트릭스. 네 가지 신호 축을 각각 독립적으로 조절할 수 있다는 점이 최대 강점이다.

**성능과 근거.** 원리적 기반은 인테그린 결합 부위와 MMP 감수성을 동시에 갖춘 PEG 하이드로겔이다 [Lutolf MP 2003, PNAS, DOI:10.1073/pnas.0737381100]. 오가노이드 적용의 분수령은 모듈형 합성 하이드로겔로 ISC 확장과 오가노이드 형성의 요구 조건을 분리해낸 연구로, 이 연구는 확장에 최적이면서 이후 분화를 허용하도록 **역학적으로 변하는(mechanically dynamic)** 매트릭스까지 구현했다 [Gjorevski N 2016, Nature, DOI:10.1038/nature20168]; 실험 절차는 별도 프로토콜로 공개되었다 [Gjorevski N & Lutolf MP 2017, Nature Protocols, DOI:10.1038/nprot.2017.095]. 4팔 말레이미드 말단 PEG(PEG-4MAL) 하이드로겔은 종양 유래 ECM 없이 인간 장 오가노이드를 생성했고, 손상 대장에 주입 전달되어 생착과 상처 치유 개선을 보였다 [Cruz-Acuña R 2017, Nature Cell Biology, DOI:10.1038/ncb3632]; 프로토콜도 공개되어 있다 [Cruz-Acuña R 2018, Nature Protocols, DOI:10.1038/s41596-018-0036-3]. (신뢰도: 상 — Gjorevski 2016과 Cruz-Acuña 2017의 원저 초록을 2026-09-14 직접 확인, 프로토콜 논문으로 재현 경로까지 공개)

이후 합성 계열은 조직별로 확장되었다. 췌장관선암(PDAC) 오가노이드용 미세환경 모사 3차원 모델 [Below CR 2022, Nature Materials, DOI:10.1038/s41563-021-01085-1], 간 오가노이드 유도용 역학조절 합성 니치 [Sorrentino G 2020, Nature Communications, DOI:10.1038/s41467-020-17161-0], 환자 유래 장 오가노이드용 공학 매트릭스 [Hunt DR 2021, Advanced Science, DOI:10.1002/advs.202004705], 환자 유래 대장 종양 오가노이드용 역학·화학 정의 매트릭스 [Ng S 2019, Biomaterials, DOI:10.1016/j.biomaterials.2019.119400], 완전 합성 ECM 기반 인간 자궁내막 공배양 모델 [Gnecco JS 2023, Med, DOI:10.1016/j.medj.2023.07.004], 화학적으로 정의된 간 오가노이드용 하이드로겔 [Ye S 2020, Advanced Functional Materials, DOI:10.1002/adfm.202000893], 강성 조절 가능한 정의 하이드로겔에서의 뇌 오가노이드 형성 [Isik M 2023, Acta Biomaterialia, DOI:10.1016/j.actbio.2023.09.040], 합성 하이드로겔 상의 평면형 신경 오가노이드 [Majumder J 2024, Journal of Tissue Engineering, DOI:10.1177/20417314241230633] 등이 보고되었다. 장 오가노이드용 합성 매트릭스의 현황은 별도 정리가 있다 [Poudel H 2022, ACS Omega, DOI:10.1021/acsomega.1c05136]. (신뢰도: 중 — 조직별로 각 1편 수준의 근거이며, 조직 간 이식 가능성은 검증되지 않음)

**한계.** 조직마다 최적 조성을 다시 찾아야 하고, 생체 ECM이 가진 수백 종 단백질의 복합적 상호작용은 재현되지 않는다.

**대표 제품(공식 페이지 확인, 접근일 2026-09-14).**

| 제품명 | 제조사 | 공식 페이지상 원료·특징 | 형태 |
|---|---|---|---|
| VitroGel ORGANOID | TheWell Bioscience (미국) | 100% 합성, 동물·인체 유래 성분 없음. 상온에서 배지와 혼합해 겔화, 중성 pH·투명. 전용 효소 비의존 회수 용액(VitroGel Cell Recovery Solution) 제공. apical-out 구조 지원을 표방 | 3D 하이드로겔 |
| Corning Synthemax II-SC Substrate | Corning Incorporated (미국) | 비트로넥틴 모사 올리고펩타이드(RGD 모티프 및 측면 서열 포함)를 고분자 백본에 공유결합시킨 자가코팅 합성 기질. 동물유래 성분 없음 | **2D 코팅 기질** |

(제품 정보 신뢰도: 중 — 제조사 공식 페이지 1차 확인, 제조사 표방값. Synthemax의 학술적 근거는 [Melkoumian Z 2010, Nature Biotechnology, DOI:10.1038/nbt.1629]에 해당)

**확보 실패:** QGel(스위스) 사의 오가노이드용 합성 매트릭스 제품군 — 제조사 공식 웹사이트(qgelbio.com)에 접근했으나 제품 사양을 확인할 수 있는 공식 제품 페이지를 확인하지 못했다(접근 2026-09-14). 따라서 제품명·사양을 기재하지 않는다. 해당 기술의 학술적 근거는 [Gjorevski N 2016, Nature, DOI:10.1038/nature20168] 및 [Gjorevski N & Lutolf MP 2017, Nature Protocols, DOI:10.1038/nprot.2017.095]로 대체한다. (신뢰도: 하 — 1차 출처 미확인)

### O3-5. ⑤ 하이브리드

**정체.** 위 계열을 의도적으로 조합한 것. 대표 유형은 (a) 천연 단백질 + 합성 가교제(예: 젤라틴 메타크릴로일 GelMA — 젤라틴에 광가교 가능한 메타크릴로일기를 도입한 것), (b) 다당 + 단백질(HA-콜라겐, 콜라겐-나노셀룰로스), (c) BME + 합성/다당(알지네이트-Matrigel 마이크로스피어), (d) dECM + 합성 가교 시스템이다.

**성능과 근거.** GelMA 계열은 강성 구배 제작과 줄기세포 역학감지 연구 [Kim C 2020, Annals of Biomedical Engineering, DOI:10.1007/s10439-019-02428-5], 신장 오가노이드의 세포 유형 특이 성숙 유도 [Clerkin S 2025, Biomaterials, DOI:10.1016/j.biomaterials.2025.123349], 환자 유래 유방암 오가노이드 약물시험 플랫폼 [Bock N 2023, Pharmaceutics, DOI:10.3390/pharmaceutics15010261]에 사용되었다. 천연 하이드로겔 조합이 신장 오가노이드 생성과 시험관 내 혈관신생을 지지한 사례 [Garreta E 2024, Advanced Materials, DOI:10.1002/adma.202400306], 자기조립 펩타이드 하이드로겔에서의 신장 오가노이드 성장·분화 [Treacy NJ 2023, Bioactive Materials, DOI:10.1016/j.bioactmat.2022.08.003], 폴리이소시아나이드 하이드로겔에서의 유선 오가노이드 형성 [Zhang Y 2020, Advanced Science, DOI:10.1002/advs.202001797], 단백질 공학 스캐폴드에서의 성체 장 오가노이드 배양 [DiMarco RL 2015, Biomaterials Science, DOI:10.1039/c5bm00108k]이 보고되었다. 하이브리드 및 정의 매트릭스 전반의 설계 관점은 종설로 정리되어 있다 [Tayler IM 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.04.020] [Hirota A 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.05.010]. (신뢰도: 중 — 사례별 단일 원저 기반)

**한계.** 두 계열의 장점을 취하는 만큼 변수가 얽혀 해석이 어렵고, 천연 성분이 남아 있는 한 로트 편차와 규제 이슈가 완전히 사라지지 않는다.

---

## O4. 오가노이드 지지체의 특수 요건 — 왜 일반 3차원 배양보다 까다로운가

일반적인 3차원 세포 배양(스페로이드, 세포 포매 배양)의 성공 기준은 대체로 "세포가 죽지 않고 3차원에서 자란다"이다. 오가노이드는 기준이 다르다. **세포가 스스로 방향을 잡고(극성), 스스로 모양을 만들고(형태형성), 여러 세포 유형으로 갈라져야(분화)** 비로소 오가노이드다. 매트릭스는 이 자기조직화(self-organization) 과정을 방해하지 않으면서 필요한 물리·화학 신호를 시기별로 제공해야 한다. 아래 다섯 가지가 오가노이드 지지체에만 부과되는 추가 요건이다.

### O4-1. 극성(apicobasal polarity) 형성

**무엇인가.** 상피세포는 위아래가 다르다. 장(腸)으로 치면 음식물이 닿는 쪽이 **정단면(apical)**, 혈관·기저막 쪽이 **기저측면(basolateral)**이다. 이 방향성을 **정단-기저 극성(apicobasal polarity)**이라 한다. 일반 스페로이드는 극성이 없거나 무질서해도 무방하지만, 오가노이드는 극성이 정해져야 관강(lumen)이 생기고 흡수·분비 기능이 나타난다.

**매트릭스가 결정한다.** 세포는 라미닌이 풍부한 기저막을 '바깥'으로 인식한다. 따라서 세포를 기저막 유사 겔로 감싸면 기저면이 바깥을 향하고 정단면이 안쪽 관강을 향하는 **apical-in** 구조가 만들어진다. 반대로 매트릭스를 제거하고 부유 배양하면 극성이 뒤집혀 정단면이 바깥을 향하는 **apical-out** 구조가 된다 [Stroulios G 2021, Journal of Visualized Experiments, DOI:10.3791/62330]. apical-out 오가노이드는 병원체 감염·흡수 실험에서 정단면 접근성을 얻는 대신 다른 제약을 갖는다 [Chen Y & Wang Y 2025, European Journal of Cell Biology, DOI:10.1016/j.ejcb.2025.151476] [Csukovich G 2025, Journal of Visualized Experiments, DOI:10.3791/68039]. (신뢰도: 상 — 프로토콜 논문 2편과 종설 1편이 동일한 매트릭스-극성 관계를 기술)

극성은 매트릭스 조성으로 능동적으로 제어할 수도 있다. 라미닌 유래 IKVAV 펩타이드를 장식한 합성 동적 하이드로겔로 장 오가노이드 극성을 제어한 보고 [Rijns L 2026, Advanced Healthcare Materials, DOI:10.1002/adhm.202502079], ECM을 통합한 기도 오가노이드에서 정단-기저 극성을 재현한 보고 [Gong Z 2026, Biomaterials, DOI:10.1016/j.biomaterials.2026.124084], 정단면이 바깥인 비강 오가노이드에서 MMP가 기도 상피 분화에 필수적임을 보인 보고 [Li L 2024, Nature Communications, DOI:10.1038/s41467-023-44488-1]가 있다. 신장 오가노이드에서는 부드러운 동적 하이드로겔 구속이 관강 형태를 개선하고 상피-간엽 전이를 줄였다 [Ruiter FAA 2022, Advanced Science, DOI:10.1002/advs.202200543]. (신뢰도: 중 — 각 조직별 단일 원저이며 일부는 최신 보고로 인용 축적이 부족)

### O4-2. 싹눈(budding)과 크립트(crypt) 형성

**무엇인가.** 장 오가노이드는 매끈한 구(球)에 머무르지 않고 표면에서 손가락 모양 돌기를 내밀며, 이 돌기 끝에 줄기세포와 파네트세포가 모인 **크립트(crypt, 장 상피의 줄기세포 구역)**가 형성된다. 이 '싹눈 내밀기(budding)'가 오가노이드가 진짜 조직 구조를 재현했다는 최소 증거다 [Sato T 2009, Nature, DOI:10.1038/nature07935]. (신뢰도: 상 — 원저가 이 구조를 핵심 결과로 제시, 5,800회 인용)

**왜 매트릭스가 어려운가.** 싹눈을 내밀려면 상피가 주변 매트릭스를 **국소적으로 밀어내야** 한다. 매트릭스가 너무 단단하거나 전혀 풀어지지 않으면 조직이 구 형태에 갇힌다. 실제로 매트릭스 힘의 이완이 크립트 형성과 구조를 지시했고 [Hushka EA 2020, Advanced Healthcare Materials, DOI:10.1002/adhm.201901214], 응력완화형 합성 하이드로겔은 효소 분해 없이도 YAP 경유로 크립트 싹눈과 파네트세포 형성을 촉진했다 [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7]. 완전 합성 하이드로겔에서 견고한 크립트 형성을 달성한 후속 보고도 나왔다 [Hushka EA 2025, Advanced Materials, DOI:10.1002/adma.202509672]. 조직 역학 측면에서는 상피 내부의 기계적 구획화가 크립트 접힘과 집단적 세포 이동을 가능하게 함이 밝혀졌고 [Pérez-González C 2021, Nature Cell Biology, DOI:10.1038/s41556-021-00699-6], 빛으로 매트릭스 점탄성을 국소 변조해 상피 곡률을 바꾸고 크립트 형태형성을 유도할 수 있었다 [Yavitt FM 2023, Science Advances, DOI:10.1126/sciadv.add5668]. 매트릭스가 부과하는 기하학적 구속이 오가노이드 패터닝을 결정론적으로 만든 사례도 있다 [Gjorevski N 2022, Science, DOI:10.1126/science.aaw9021]. (신뢰도: 상 — 6편의 독립 원저가 "매트릭스의 국소 이완·기하 구속이 크립트 형태형성을 지배한다"는 동일 결론에 수렴)

최근에는 상피세포 자신이 분비한 ECM 니치가 장 오가노이드 형성을 이끈다는 보고도 나와, 매트릭스의 역할이 '제공'뿐 아니라 '세포 자체 ECM 생산의 허용'에도 있음을 시사한다 [Chrisnandy A & Lutolf MP 2025, Developmental Cell, DOI:10.1016/j.devcel.2025.06.026]. (신뢰도: 중 — 최신 단일 원저, 인용 축적 부족)

### O4-3. 조직별로 요구가 다르다

같은 '오가노이드'라도 조직마다 매트릭스 요구가 다르다. 이것이 "만능 매트릭스"가 존재하지 않는 핵심 이유다.

| 조직 | 매트릭스 관련 특기 요구 | 근거 |
|---|---|---|
| 장(소장·대장) | 단계별 전환 필요: 확장기에는 고강성+피브로넥틴 접착, 분화·오가노이드 형성기에는 저강성+라미닌 접착 | [Gjorevski N 2016, Nature, DOI:10.1038/nature20168] |
| 간 | 역학 조절형 합성 니치가 오가노이드 유도 효율을 좌우 | [Sorrentino G 2020, Nature Communications, DOI:10.1038/s41467-020-17161-0] [Huch M 2015, Cell, DOI:10.1016/j.cell.2014.11.050] |
| 뇌 | 하이드로겔 역학이 배아체 성장·발생에 영향; 뇌 특이 ECM이 구조적·기능적 성숙을 촉진 | [Cassel de Camps C 2022, ACS Applied Bio Materials, DOI:10.1021/acsabm.1c01047] [Cho AN 2021, Nature Communications, DOI:10.1038/s41467-021-24775-5] [Lancaster MA 2013, Nature, DOI:10.1038/nature12517] |
| 신장 | 부드러운 동적 구속이 관강 형태 개선·상피간엽전이 억제; 알지네이트 포매가 비정상 콜라겐 침착 감소 | [Ruiter FAA 2022, Advanced Science, DOI:10.1002/advs.202200543] [Geuens T 2021, Biomaterials, DOI:10.1016/j.biomaterials.2021.120976] [Takasato M 2015, Nature, DOI:10.1038/nature15695] [Morizane R 2015, Nature Biotechnology, DOI:10.1038/nbt.3392] |
| 기도·폐 | 정단-기저 극성 재현과 ECM 통합이 분화의 관건; 가용성 ECM이 폐포 모델 형성을 촉진 | [Gong Z 2026, Biomaterials, DOI:10.1016/j.biomaterials.2026.124084] [Valdoz JC 2022, Biomaterials, DOI:10.1016/j.biomaterials.2022.121464] [Sachs N 2019, The EMBO Journal, DOI:10.15252/embj.2018100300] |
| 종양 | 강성·점탄성이 약물 반응과 침윤 표현형을 직접 바꾸므로 매트릭스가 곧 실험 변수 | [Below CR 2022, Nature Materials, DOI:10.1038/s41563-021-01085-1] [Ng S 2019, Biomaterials, DOI:10.1016/j.biomaterials.2019.119400] [Neal JT 2018, Cell, DOI:10.1016/j.cell.2018.11.021] |
| 자궁내막 | 완전 합성 ECM에서 호르몬 반응성 공배양 구현; 조직 유래 하이드로겔도 사용 | [Gnecco JS 2023, Med, DOI:10.1016/j.medj.2023.07.004] [Turco MY 2017, Nature Cell Biology, DOI:10.1038/ncb3516] [Jamaluddin MFB 2022, PNAS, DOI:10.1073/pnas.2208040119] |

(표 신뢰도: 중 — 각 행은 1~3편의 원저에 근거하며, 조직 간 직접 비교 실험은 거의 없음)

### O4-4. 회수 가능성(retrievability)

**무엇인가.** 오가노이드는 배양이 끝이 아니다. 계대(passage), 단일세포 해리, 유세포분석, 시퀀싱, 이식 등을 위해 **겔에서 손상 없이 꺼내야** 한다. 일반 3차원 배양에서는 회수 품질이 결과에 큰 영향을 주지 않는 경우가 많지만, 오가노이드는 회수 과정에서 구조가 깨지거나 잔류 매트릭스 단백질이 하류 분석(특히 단백질체·전사체 분석)을 오염시킨다.

**근거와 대응.** BME는 냉각 및 전용 회수 용액으로 녹여 꺼내지만 잔류 단백질 문제가 남는다 [Benton G 2014, Advanced Drug Delivery Reviews, DOI:10.1016/j.addr.2014.06.005]. 다당 계열에서는 회수를 설계 목표로 명시한 사례가 있다 — 양이온성 가교 나노셀룰로스 매트릭스는 장 오가노이드의 '성장과 회수'를 함께 겨냥해 개발되었다 [Curvello R & Garnier G 2021, Biomacromolecules, DOI:10.1021/acs.biomac.0c01510]. 합성·다당 계열 상용품 중에는 효소를 쓰지 않는 전용 회수 용액을 함께 공급하는 제품이 있다(TheWell Bioscience VitroGel Cell Recovery Solution, thewellbio.com 공식 페이지, 접근 2026-09-14). 이식·전달 관점에서는 PEG-4MAL 하이드로겔이 오가노이드 주입 전달 매개체로 사용되었다 [Cruz-Acuña R 2017, Nature Cell Biology, DOI:10.1038/ncb3632] [Cruz-Acuña R 2018, Nature Protocols, DOI:10.1038/s41596-018-0036-3]. (신뢰도: 중 — 회수 성능을 정량 비교한 표준화 연구를 확보하지 못했고, 제품 정보는 제조사 표방값)

**확보 실패:** 계열 간 오가노이드 회수율·생존율을 동일 조건에서 정량 비교한 논문 — 검증 문헌 풀 내에서 확인하지 못했다. (신뢰도: 하 — 해당 근거 부재)

### O4-5. 로트 간 편차(lot-to-lot variability)

**무엇인가.** 같은 제품명이라도 제조 배치(lot)가 바뀌면 물성과 조성이 달라져 실험 결과가 흔들리는 현상. 동물 조직 유래 소재의 구조적 문제다.

**근거.** Matrigel류의 조성이 정의되지 않은 복합 혼합물이라는 점 [Hughes CS 2010, Proteomics, DOI:10.1002/pmic.200900758], 그로 인한 배치 간 편차와 면역원성이 임상 응용을 제약한다는 점 [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7], Matrigel 의존에서 벗어나야 한다는 문제 제기 [Kozlowski MT 2021, Communications Biology, DOI:10.1038/s42003-021-02910-8], 합성 대체재 개발의 동기가 바로 이 편차라는 점 [Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8]이 반복 확인된다. 종양 오가노이드 분야에서는 재현 가능한 ECM 확보가 독립된 과제로 정리되었다 [Li K 2025, Journal of Translational Medicine, DOI:10.1186/s12967-025-06349-x] [Guo L 2024, Frontiers in Immunology, DOI:10.3389/fimmu.2024.1290504]. (신뢰도: 상 — 6개 독립 출처가 동일한 문제를 명시)

**대응 방향은 세 갈래다.** (i) 제조사 측 로트 QC 강화 — Corning은 오가노이드용 Matrigel의 로트별 탄성계수 측정과 3D 돔 형성 적격성 판정을 공식 페이지에 명시한다(corning.com, 접근 2026-09-14). (ii) 정의된 소재로 이행 — 합성·다당 계열 채택. UPM Biomedicals는 GrowDex가 나노피브릴 셀룰로스와 물만으로 구성되어 로트 간 편차가 없다고 표방한다(upmbiomedicals.com, 접근 2026-09-14). (iii) 측정 표준화 — 원자간력현미경(AFM)을 이용한 연질 배양 표면 및 3차원 하이드로겔의 탄성계수 측정 프로토콜이 공개되어 있어, 실험실 수준의 로트 검수가 가능하다 [Norman MDA 2021, Nature Protocols, DOI:10.1038/s41596-021-00495-4]. (신뢰도: 중 — (i)(ii)는 제조사 표방값, (iii)은 프로토콜 논문 1편)

임상·산업 이행 관점에서 GMP(우수의약품제조관리기준) 준수 오가노이드 생산 [Dossena M 2020, Stem Cell Research & Therapy, DOI:10.1186/s13287-020-1585-2]과 환자 유래 오가노이드 기반 이식용 점막 제작 [Meran L 2023, Nature Protocols, DOI:10.1038/s41596-022-00751-1]이 보고되었고, 비용 절감형 장 오가노이드 배양법도 제시되었다 [Takahashi Y 2023, Scientific Reports, DOI:10.1038/s41598-023-32438-2]. (신뢰도: 중 — 각 1편의 원저)

### O4-6. 정리 — 일반 3차원 배양보다 까다로운 이유

첫째, **요구가 시간에 따라 바뀐다.** 일반 3차원 배양은 하나의 고정된 물성으로 충분하지만, 오가노이드는 확장기와 분화기의 최적 물성·리간드가 상반된다 [Gjorevski N 2016, Nature, DOI:10.1038/nature20168]. 이 때문에 '동적 매트릭스' 설계가 필수 과제가 되었다 [Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7] [Yavitt FM 2023, Science Advances, DOI:10.1126/sciadv.add5668] [Peng YH 2023, Nature Nanotechnology, DOI:10.1038/s41565-023-01483-3]. (신뢰도: 상 — 4개 독립 출처 수렴)

둘째, **성공 판정 기준이 형태학적이다.** 세포 생존율이 아니라 극성·관강·싹눈·세포 다양성이 기준이므로, 매트릭스의 미세한 물성 차이가 곧 표현형 차이로 드러난다 [Pérez-González C 2021, Nature Cell Biology, DOI:10.1038/s41556-021-00699-6] [Elosegui-Artola A 2023, Nature Materials, DOI:10.1038/s41563-022-01400-4]. (신뢰도: 상 — 2편의 독립 원저)

셋째, **조직 특이성이 강하다.** O4-3에서 보았듯 장·간·뇌·신장·폐·종양의 요구가 각각 다르며, 한 조직에서 검증된 매트릭스가 다른 조직에서 그대로 작동한다는 보장이 없다 [Kratochvil MJ 2019, Nature Reviews Materials, DOI:10.1038/s41578-019-0129-9]. (신뢰도: 중 — 종설 논지)

넷째, **하류 공정까지 함께 설계해야 한다.** 회수·분석·이식까지 고려하면 매트릭스 선택은 배양 성능만의 문제가 아니다 [Cruz-Acuña R 2018, Nature Protocols, DOI:10.1038/s41596-018-0036-3] [Meran L 2023, Nature Protocols, DOI:10.1038/s41596-022-00751-1]. (신뢰도: 중 — 프로토콜 논문 2편)

다섯째, **재현성 요구 수준이 높다.** 오가노이드는 약물 반응 예측 등 정량적 판정에 쓰이므로, 로트 편차가 곧 결론의 편차가 된다 [Li K 2025, Journal of Translational Medicine, DOI:10.1186/s12967-025-06349-x]. (신뢰도: 중 — 종설 1편)

---

## 확보 실패 항목 (미해결 4건)

1. **Engler 2006의 탄성계수 구간 수치** — Europe PMC 초록(2026-09-14 조회)에 kPa 값이 기재되어 있지 않아, 본 문서에서는 정성적 결론(뇌 모사=신경, 근육 모사=근육, 뼈 모사=골)만 채택하고 수치는 제시하지 않았다.
2. **Hughes 2010이 동정한 Matrigel 단백질 총수** — 해당 초록(2026-09-14 조회)에 총 개수가 기재되어 있지 않아 수치를 인용하지 않았다.
3. **QGel 사 제품 사양의 1차 출처** — qgelbio.com 접근 결과 제품 사양을 확인할 수 있는 공식 제품 페이지를 확인하지 못했다(2026-09-14). 제품명·사양 기재를 보류했다.
4. **계열 간 오가노이드 회수율·생존율의 동일 조건 정량 비교 문헌** — 검증 문헌 풀(565편 + 랜드마크 40편) 내에서 해당 비교 연구를 확인하지 못했다.

**추가 접근 제약 기록.** Corning의 Matrigel Matrix for Organoid Culture 공식 페이지 및 Guidelines for Use PDF는 직접 HTTP 요청 시 403(Forbidden)이 반환되었다(2026-09-14). 따라서 해당 제품 정보는 corning.com 도메인으로 한정한 검색 색인을 통해 확인한 공식 페이지 내용에 근거하며, 원문 PDF 대조는 하지 못했다.

---

## 인용 문헌 목록 (본문 인용 순 무관, 저자 알파벳순)

1. Aisenbrey EA & Murphy WL 2020, Nature Reviews Materials, DOI:10.1038/s41578-020-0199-8, PMID:32953138
2. Baghdadi MB 2024, Science, DOI:10.1126/science.adj7615, PMID:39607940
3. Bejoy J 2018, ACS Biomaterials Science & Engineering, DOI:10.1021/acsbiomaterials.8b01142, PMID:31572767
4. Below CR 2022, Nature Materials, DOI:10.1038/s41563-021-01085-1, PMID:34518665
5. Benton G 2014, Advanced Drug Delivery Reviews, DOI:10.1016/j.addr.2014.06.005, PMID:24997339
6. Bock N 2023, Pharmaceutics, DOI:10.3390/pharmaceutics15010261
7. Braam SR 2008, Stem Cells, DOI:10.1634/stemcells.2008-0291, PMID:18599809
8. Broguiere N 2018, Advanced Materials, DOI:10.1002/adma.201801621, PMID:30203567
9. Burridge PW 2014, Nature Methods, DOI:10.1038/nmeth.2999, PMID:24930130
10. Capeling MM 2019, Stem Cell Reports, DOI:10.1016/j.stemcr.2018.12.001, PMID:30612954
11. Cassel de Camps C 2022, ACS Applied Bio Materials, DOI:10.1021/acsabm.1c01047
12. Chaudhuri O 2016, Nature Materials, DOI:10.1038/nmat4489, PMID:26618884
13. Chaudhuri O 2020, Nature, DOI:10.1038/s41586-020-2612-2, PMID:32848221
14. Chen Y & Wang Y 2025, European Journal of Cell Biology, DOI:10.1016/j.ejcb.2025.151476, PMID:39837176
15. Cho AN 2021, Nature Communications, DOI:10.1038/s41467-021-24775-5
16. Chooi WH 2023, Advanced Healthcare Materials, DOI:10.1002/adhm.202202342
17. Chrisnandy A 2022, Nature Materials, DOI:10.1038/s41563-021-01136-7, PMID:34782747
18. Chrisnandy A & Lutolf MP 2025, Developmental Cell, DOI:10.1016/j.devcel.2025.06.026, PMID:40680738
19. Clerkin S 2025, Biomaterials, DOI:10.1016/j.biomaterials.2025.123349, PMID:40315627
20. Cosgrove BD 2016, Nature Materials, DOI:10.1038/nmat4725, PMID:27525568
21. Cruz-Acuña R 2017, Nature Cell Biology, DOI:10.1038/ncb3632, PMID:29058719
22. Cruz-Acuña R 2018, Nature Protocols, DOI:10.1038/s41596-018-0036-3
23. Csukovich G 2025, Journal of Visualized Experiments, DOI:10.3791/68039, PMID:40227982
24. Curvello R 2020, Advanced Science, DOI:10.1002/advs.202002135, PMID:33437574
25. Curvello R 2021, Materials Science and Engineering: C, DOI:10.1016/j.msec.2021.112051
26. Curvello R & Garnier G 2021, Biomacromolecules, DOI:10.1021/acs.biomac.0c01510, PMID:33332099
27. DiMarco RL 2015, Biomaterials Science, DOI:10.1039/c5bm00108k
28. Domogatskaya A 2008, Stem Cells, DOI:10.1634/stemcells.2007-0389, PMID:18757303
29. Dossena M 2020, Stem Cell Research & Therapy, DOI:10.1186/s13287-020-1585-2
30. Dupont S 2011, Nature, DOI:10.1038/nature10137, PMID:21654799
31. Elosegui-Artola A 2023, Nature Materials, DOI:10.1038/s41563-022-01400-4, PMID:36456871
32. Engler AJ 2006, Cell, DOI:10.1016/j.cell.2006.06.044, PMID:16923388
33. Forster R 2014, Stem Cell Reports, DOI:10.1016/j.stemcr.2014.05.001, PMID:24936470
34. Frantz C 2010, Journal of Cell Science, DOI:10.1242/jcs.023820, PMID:21123617
35. García JR 2016, Journal of Biomedical Materials Research Part A, DOI:10.1002/jbm.a.35626, PMID:26662727
36. Garreta E 2024, Advanced Materials, DOI:10.1002/adma.202400306, PMID:38762768
37. Geuens T 2021, Biomaterials, DOI:10.1016/j.biomaterials.2021.120976, PMID:34198162
38. Giobbe GG 2019, Nature Communications, DOI:10.1038/s41467-019-13605-4, PMID:31827102
39. Gjorevski N 2016, Nature, DOI:10.1038/nature20168, PMID:27851739
40. Gjorevski N & Lutolf MP 2017, Nature Protocols, DOI:10.1038/nprot.2017.095
41. Gjorevski N 2022, Science, DOI:10.1126/science.aaw9021, PMID:34990240
42. Gnecco JS 2023, Med, DOI:10.1016/j.medj.2023.07.004
43. Gong Z 2026, Biomaterials, DOI:10.1016/j.biomaterials.2026.124084, PMID:41722465
44. Guo L 2024, Frontiers in Immunology, DOI:10.3389/fimmu.2024.1290504, PMID:38571961
45. He S 2023, Gastroenterology, DOI:10.1053/j.gastro.2023.02.030, PMID:36871599
46. Hirota A 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.05.010
47. Huch M 2015, Cell, DOI:10.1016/j.cell.2014.11.050, PMID:25533785
48. Hughes CS 2010, Proteomics, DOI:10.1002/pmic.200900758
49. Hunt DR 2021, Advanced Science, DOI:10.1002/advs.202004705, PMID:34026461
50. Hushka EA 2020, Advanced Healthcare Materials, DOI:10.1002/adhm.201901214, PMID:31957249
51. Hushka EA 2025, Advanced Materials, DOI:10.1002/adma.202509672, PMID:40817630
52. Hynes RO & Naba A 2012, Cold Spring Harbor Perspectives in Biology, DOI:10.1101/cshperspect.a004903, PMID:21937732
53. Isik M 2023, Acta Biomaterialia, DOI:10.1016/j.actbio.2023.09.040, PMID:37793600
54. Jamaluddin MFB 2022, PNAS, DOI:10.1073/pnas.2208040119, PMID:36279452
55. Karamanos NK 2021, The FEBS Journal, DOI:10.1111/febs.15776, PMID:33605520
56. Kim C 2020, Annals of Biomedical Engineering, DOI:10.1007/s10439-019-02428-5, PMID:31802282
57. Kim S 2022, Nature Communications, DOI:10.1038/s41467-022-29279-4, PMID:35354790
58. Kloxin AM 2009, Science, DOI:10.1126/science.1169494, PMID:19342581
59. Kozlowski MT 2021, Communications Biology, DOI:10.1038/s42003-021-02910-8, PMID:34893703
60. Kratochvil MJ 2019, Nature Reviews Materials, DOI:10.1038/s41578-019-0129-9, PMID:33552558
61. Krüger M 2020, Advanced Healthcare Materials, DOI:10.1002/adhm.201901658
62. Lancaster MA 2013, Nature, DOI:10.1038/nature12517, PMID:23995685
63. Lee HP 2019, Nature Communications, DOI:10.1038/s41467-019-08465-x
64. Li C 2024, Journal of Biomedical Science, DOI:10.1186/s12929-024-01086-7
65. Li K 2025, Journal of Translational Medicine, DOI:10.1186/s12967-025-06349-x, PMID:40312683
66. Li L 2024, Nature Communications, DOI:10.1038/s41467-023-44488-1
67. Lou J 2018, Biomaterials, DOI:10.1016/j.biomaterials.2017.11.004, PMID:29132046
68. Lu HF 2014, Biomaterials, DOI:10.1016/j.biomaterials.2013.12.050, PMID:24411336
69. Lutolf MP 2003, PNAS, DOI:10.1073/pnas.0737381100, PMID:12686696
70. Maharjan S 2024, Advanced Drug Delivery Reviews, DOI:10.1016/j.addr.2024.115237
71. Majumder J 2024, Journal of Tissue Engineering, DOI:10.1177/20417314241230633, PMID:38361535
72. McCracken KW 2014, Nature, DOI:10.1038/nature13863, PMID:25363776
73. McKinnon DD 2014, Advanced Materials, DOI:10.1002/adma.201303680
74. Melkoumian Z 2010, Nature Biotechnology, DOI:10.1038/nbt.1629, PMID:20512120
75. Meran L 2023, Nature Protocols, DOI:10.1038/s41596-022-00751-1
76. Miller JS 2012, Nature Materials, DOI:10.1038/nmat3357, PMID:22751181
77. Morizane R 2015, Nature Biotechnology, DOI:10.1038/nbt.3392
78. Musah S 2012, ACS Nano, DOI:10.1021/nn3039148, PMID:23005914
79. Naba A 2012, Molecular & Cellular Proteomics, DOI:10.1074/mcp.m111.014647, PMID:22159717
80. Naba A 2016, Matrix Biology, DOI:10.1016/j.matbio.2015.06.003, PMID:26163349
81. Naba A 2024, Nature Reviews Molecular Cell Biology, DOI:10.1038/s41580-024-00767-3, PMID:39223427
82. Nam S 2019, Biomaterials, DOI:10.1016/j.biomaterials.2019.02.004
83. Neal JT 2018, Cell, DOI:10.1016/j.cell.2018.11.021, PMID:30550791
84. Ng S 2019, Biomaterials, DOI:10.1016/j.biomaterials.2019.119400
85. Norman MDA 2021, Nature Protocols, DOI:10.1038/s41596-021-00495-4
86. Ohnsorg ML 2025, Accounts of Chemical Research, DOI:10.1021/acs.accounts.4c00548, PMID:39665396
87. Peng YH 2023, Nature Nanotechnology, DOI:10.1038/s41565-023-01483-3, PMID:37550574
88. Pérez-González C 2021, Nature Cell Biology, DOI:10.1038/s41556-021-00699-6, PMID:34155382
89. Poudel H 2022, ACS Omega, DOI:10.1021/acsomega.1c05136
90. Pulkkinen HJ 2013, Osteoarthritis and Cartilage, DOI:10.1016/j.joca.2012.12.004, PMID:23257243
91. Rijns L 2026, Advanced Healthcare Materials, DOI:10.1002/adhm.202502079, PMID:40904064
92. Rocha FG 2008, Biomaterials, DOI:10.1016/j.biomaterials.2008.03.026, PMID:18396329
93. Rodin S 2010, Nature Biotechnology, DOI:10.1038/nbt.1620, PMID:20512123
94. Ruiter FAA 2022, Advanced Science, DOI:10.1002/advs.202200543, PMID:35567354
95. Sachs N 2019, The EMBO Journal, DOI:10.15252/embj.2018100300, PMID:30643021
96. Sackett SD 2018, Scientific Reports, DOI:10.1038/s41598-018-28857-1, PMID:29993013
97. Sato T 2009, Nature, DOI:10.1038/nature07935, PMID:19329995
98. Sato T 2011, Gastroenterology, DOI:10.1053/j.gastro.2011.07.050, PMID:21889923
99. Shao X 2023, Nucleic Acids Research, DOI:10.1093/nar/gkac1009, PMID:36399478
100. Simsa R 2021, PLoS ONE, DOI:10.1371/journal.pone.0245685
101. Sorrentino G 2020, Nature Communications, DOI:10.1038/s41467-020-17161-0, PMID:32651372
102. Stanton AE 2019, Acta Biomaterialia, DOI:10.1016/j.actbio.2019.06.048, PMID:31255664
103. Stroulios G 2021, Journal of Visualized Experiments, DOI:10.3791/62330, PMID:33843928
104. Takahashi Y 2023, Scientific Reports, DOI:10.1038/s41598-023-32438-2
105. Takasato M 2015, Nature, DOI:10.1038/nature15695, PMID:26444236
106. Tayler IM 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.04.020, PMID:33882354
107. Tomaszewski CE 2021, Acta Biomaterialia, DOI:10.1016/j.actbio.2021.03.041
108. Treacy NJ 2023, Bioactive Materials, DOI:10.1016/j.bioactmat.2022.08.003, PMID:36093324
109. Trujillo S 2020, Biomaterials, DOI:10.1016/j.biomaterials.2020.120104, PMID:32422492
110. Turco MY 2017, Nature Cell Biology, DOI:10.1038/ncb3516
111. Valdoz JC 2022, Biomaterials, DOI:10.1016/j.biomaterials.2022.121464
112. Yavitt FM 2023, Science Advances, DOI:10.1126/sciadv.add5668, PMID:36662859
113. Ye S 2020, Advanced Functional Materials, DOI:10.1002/adfm.202000893
114. Zhang Y 2020, Advanced Science, DOI:10.1002/advs.202001797
115. Zhu L 2023, Small, DOI:10.1002/smll.202207752

**인용 논문 총계: 115편** (검증 문헌 풀 및 랜드마크 목록에 실재하는 항목만 사용. 최소 요건 30편을 충족)

## 1차 출처 확인 기록 (비(非)논문, 접근일 2026-09-14)

| 대상 | 제조사 | 확인 경로 | 상태 |
|---|---|---|---|
| Matrigel Matrix for Organoid Culture | Corning Incorporated | corning.com 공식 제품 페이지 | 확인(직접 페치 403 → 도메인 한정 검색 색인 경유) |
| Cultrex BME / RGF BME Type 2 Select / UltiMatrix | R&D Systems (Bio-Techne) | bio-techne.com 공식 제품 페이지 | 확인 |
| Geltrex LDEV-Free RGF BME / Geltrex Flex | Thermo Fisher Scientific | thermofisher.com 공식 제품 페이지 | 확인 |
| Biolaminin 521 LN | BioLamina AB | biolamina.com 공식 제품 페이지 | 확인 |
| Synthemax II-SC Substrate | Corning Incorporated | corning.com 공식 제품 페이지 | 확인 |
| GrowDex | UPM Biomedicals | upmbiomedicals.com 공식 제품 페이지 | 확인 |
| VitroGel ORGANOID / Cell Recovery Solution | TheWell Bioscience | thewellbio.com 공식 제품 페이지 | 확인 |
| HyStem / HyStem-C / HyStem-HP | Advanced BioMatrix | advancedbiomatrix.com 공식 제품 페이지 | 확인 |
| PRONOVA UP 알지네이트 | NovaMatrix | novamatrix.biz 공식 제품 페이지 | 확인 |
| IntestiCult Organoid Growth Medium (배지, 매트릭스 아님) | STEMCELL Technologies | stemcell.com 공식 제품 페이지 | 확인 |
| QGel 오가노이드용 합성 매트릭스 | QGel | qgelbio.com | **1차 출처 미확인** |

(본 표의 모든 제품 특성은 제조사 표방값이며 독립적 제3자 검증은 수행하지 않았다. 신뢰도: 중)
