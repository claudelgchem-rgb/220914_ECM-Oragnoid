---
agent: E
status: complete
date_checked: 2026-09-14
items_count: 30
evidence_count: {papers: 51, patents: 0}
unresolved: 9
---

> **[병합 고지 — 2026-09-14, V 감사 반려-004 반영]** 내부 감사에서 `E-L8-005`(염화칼슘),
> `E-L8-007`(염화바륨), `E-L8-008`(글루코노델타락톤)이 L6의 가교제 항목과 **같은 물질로 중복
> 등재**된 것이 확인되어, 통합 인벤토리에서는 각각 `D-L6-025`, `D-L6-027`, `D-L6-026`으로
> 병합했다. 이들의 주 기능은 이온 가교이므로 대표 층위를 L6으로 확정했다. 본문의 L8 관점
> 서술(이온강도·완충·가교 속도 제어)은 그대로 유효하다. 그 결과 이 문서의 등재 항목은
> **30건**(L8 13건 · L9 17건)이다.



# 05. 규격·품질·규제 — L8 완충·이온·부형제 / L9 품질·안전 규격 / O8 규제·등급 체계

**작성 기준일: 2026-09-14 (모든 규제 문서 접근일 동일)**

본 문서는 오가노이드 배양용 세포외기질(ECM, extracellular matrix — 세포를 둘러싸고 물리적 지지와 신호를 동시에 제공하는 단백질·다당류 복합 그물망) 대체 지지체를 상업 제품으로 만들 때, 매트릭스 고분자 자체가 아니라 **그 주변을 규정하는 것들** — 완충·이온·부형제(L8)와 품질·안전 규격 항목(L9), 그리고 이 둘을 강제하는 규제 등급 체계(O8) — 을 다룬다. 등재 항목은 총 30건(L8 13건, L9 17건 — 중복 병합 후 최종값)이며 인벤토리는 `inv_spec.csv`에 있다. 규제·약전 정보는 모두 발행기관 원문 또는 공식 공지를 직접 확인했고, 확인하지 못한 항목은 본문에 "확보 실패"로 명시했다. **본 문서에서 인용한 논문의 DOI·PMID는 전부 검증된 문헌 풀(`landmarks.txt`, `E_spec.txt` 및 동일 수집 계열 파일)에 실재하는 서지값이며, 약전 모노그래프 번호나 가이던스 문서번호를 추정해 기재한 곳은 없다.**

문서 전반에서 두 가지 구분을 일관되게 유지한다. 첫째, **배지 성분과 매트릭스 성분의 구분**이다. 중탄산나트륨·항생제·DMSO는 배지 또는 동결보존액 성분이고, 염화칼슘·수산화나트륨은 매트릭스 겔화 공정의 성분이다. 규제 문서에서 전자는 제거 대상 공정 보조제로, 후자는 최종 제품 구성물로 취급되므로 CMC(Chemistry, Manufacturing and Controls — 원료·제조·관리 정보) 문서에서 자리가 완전히 다르다. 둘째, **체외 배양용(in vitro)과 체내 이식용(in vivo implantation)의 구분**이다. 감작성·자극성 시험, 잔류 가교제 한도, 무균시험 같은 항목은 체내 이식 경로에서만 필수이며, 체외 배양 전용 연구용 제품에 이를 일괄 부과하면 개발비만 과다 계상된다.

---

## ① L8 — 완충·이온·부형제

오가노이드 지지체 논문은 거의 언제나 고분자(콜라겐, 라미닌, 알지네이트, 폴리에틸렌글리콜)를 주인공으로 서술하지만, 실제 제조 현장에서 로트 간 재현성을 무너뜨리는 것은 대부분 이 절에 나오는 **보조 물질**이다. 이온강도가 몇 mM 다르면 콜라겐 섬유 직경이 달라지고, 가교욕의 칼슘 이온 공급 방식이 외부 확산이냐 내부 서방이냐에 따라 겔 내부의 가교밀도 분포가 완전히 달라진다. 완충계 선택은 pH만의 문제가 아니라 — 인산완충식염수(PBS)를 알지네이트 칼슘 가교 공정에 쓰면 인산이온이 Ca²⁺를 침전시켜 가교 자체가 실패한다 — 화학적 양립성의 문제다. 아래 13건은 이런 "보이지 않는 변수"를 규격화 가능한 항목으로 분해한 것이다.

### 1-1. 이온강도와 콜라겐 섬유화

**염화나트륨(NaCl)** 은 중성 pH에서 진행되는 콜라겐 자가조립(fibrillogenesis — 산성 용액에 단분자로 녹아 있던 콜라겐이 중성·37 °C에서 스스로 섬유 다발을 이루는 과정)의 핵형성 속도와 최종 섬유 직경을 결정한다. 겔화 완충액의 최종 Na⁺ 농도는 **140–160 mM**, 삼투압은 **285 ± 15 mOsm/kg**(빙점강하 삼투압측정법)을 공정 목표로 삼는다. 이온강도가 과다하면 섬유가 굵어지면서 동일 단백질 농도에서도 저장탄성률 G′(진동 전단에서 재료가 탄성적으로 저장하는 에너지 성분, 단위 Pa)이 크게 흔들리고, 과소하면 겔화가 지연되거나 불완전 겔로 끝난다. 탈세포 조직 유래 ECM 하이드로겔의 겔화 거동을 다룬 연구들이 이 민감성을 반복해서 보여준다(Giobbe 2019, DOI:10.1038/s41467-019-13605-4, PMID:31827102; Kim S 2022, DOI:10.1038/s41467-022-29279-4, PMID:35354790).

**수산화나트륨(NaOH)** 은 pH 2–4의 산성 콜라겐 원액을 **pH 7.2 ± 0.2**(전위차 pH측정법, 4 °C 조작)로 중화해 섬유화를 개시시키는 필수 공정 시약이다. 국소적으로 pH 8을 넘기면 콜라겐이 변성·응집해 G′ 재현성이 붕괴하고, 조작 온도가 4 °C를 벗어나면 중화 도중 조기 겔화가 일어난다. 중화 후 37 °C 겔화시간은 레오미터 시간掃引(1 Hz, 변형 1%)에서 G′–G″ 교차점으로 판정하며 **20–40분**이 표준 범위다.

**확보 실패:** 이온강도가 콜라겐 섬유 직경에 미치는 영향을 직접 정량한(예: NaCl 농도별 섬유 직경 nm 값) 논문이 검증된 문헌 풀 내에 존재하지 않는다. 따라서 위 수치는 dECM·콜라겐 겔 제조 프로토콜에서 통용되는 공정 목표값으로 기재했으며, 1차 정량 논문 근거는 붙이지 않았다.

### 1-2. 완충계

| 항목 | 사용 범위 | 핵심 규격 | 주의점 |
|---|---|---|---|
| 인산완충식염수(PBS/DPBS) | 세척·희석·평형화 | pH 7.2 ± 0.2, 270–300 mOsm/kg, 무균(USP \<71\>), 내독소 ≤ 0.5 EU/mL(USP \<85\>/\<86\>) | Ca²⁺와 불용성 인산칼슘 형성 → **알지네이트 이온가교 공정에 사용 금지** |
| HEPES | CO₂ 비의존 pH 완충(겔 캐스팅·이미징·수송) | 10–25 mM, pKa 7.48(25 °C) 기준 pH 7.2–7.6 유지 | 광조사 시 과산화수소 생성; 25 mM 초과 시 세포독성 영역 |
| 중탄산나트륨(NaHCO₃) | **배지 성분**(매트릭스 성분 아님) | 14–44 mM, 5% CO₂ 평형 후 pH 7.2–7.4 | CO₂ 분압 이탈 시 배지 알칼리화(pH > 7.8)로 생존율 급락 |

HEPES(4-(2-하이드록시에틸)-1-피페라진에탄설폰산 — CO₂ 분압에 의존하지 않고 생리적 pH를 유지하는 합성 양쪽성 이온 완충제)는 인큐베이터 밖에서 겔을 다루는 모든 구간에 필요하며, 화학 정의형 하이드로겔 오가노이드 배양 프로토콜에서 반복 사용된다(Broguiere 2018, DOI:10.1002/adma.201801621, PMID:30203567; Ye S 2020, DOI:10.1002/adfm.202000893, PMID:34658689; Turco 2017, DOI:10.1038/ncb3516, PMID:28394884).

### 1-3. 이온 가교제 — 알지네이트계

알지네이트(갈조류 유래 선형 다당으로, 구루론산 G-블록이 2가 양이온과 "에그박스(egg-box)" 구조를 이루며 가교되는 고분자)는 화학 정의형·무동물유래 지지체의 대표 후보이며, 장/척수 오가노이드 배양에서 실제로 작동한다(Capeling 2019, DOI:10.1016/j.stemcr.2018.12.001, PMID:30612954; Chooi 2023, DOI:10.1002/adhm.202202342, PMID:36502337). 가교제 선택이 곧 겔 균질성 규격이 된다.

- **염화칼슘(CaCl₂)** — 외부 가교. 가교욕 **50–100 mM**, 접촉 **5–10분**. 용해도가 높아 표면에서 급속히 가교가 진행되므로 겔 두께 방향으로 가교밀도 구배가 생긴다. 이것이 로트 간 G′ 편차의 주요 원인이다. 세척 후 배지 내 Ca²⁺는 1.8 mM 이하로 복귀시킨다.
- **황산칼슘(CaSO₄)** — 내부 가교. 저용해도 슬러리로 Ca²⁺를 서방 공급해 최종 **5–20 mM Ca²⁺** 상당, 실온 30–60분에 균일 겔화. 겔화 완료는 G′ > G″ 교차점으로 판정한다.
- **글루코노델타락톤(GDL)** — CaCO₃와 **1:2 몰비**로 조합해 가수분해 산성화로 Ca²⁺를 방출시키는 완서 가교계. 겔화 중 pH 강하폭을 **pH 7.4 → 7.0 이내**로 제한해야 오가노이드 생존율이 유지된다. 트랜스글루타미나제 병용 가교 연구가 CaCl₂ 대비 팽윤 거동 차이를 보여준다(Pilipenko 2019, DOI:10.1016/j.carbpol.2019.115035, PMID:31426956).
- **염화바륨(BaCl₂)** — Ba²⁺가 G-블록 친화도가 높아 장기 안정성이 우수하지만, Ba²⁺는 K⁺ 채널을 차단하는 전신 독성 물질이다. 가교욕 **20 mM 이하**로 제한하고 잔류 Ba²⁺는 유도결합플라스마 질량분석(ICP-MS)으로 정량해 검출한계 미만을 목표로 한다. **체내 이식용 경로에서는 잔류 규격과 독성학적 정당화 없이는 수용되기 어렵다.** 확보 실패: Ba²⁺ 잔류 허용치를 규정한 약전·ISO 수치 기준을 1차 출처에서 확인하지 못했다.

### 1-4. 당류·동결보호제·기타 부형제

**수크로스**(2–10% w/v)와 **트레할로스**(5–10% w/v)는 동결건조 보호제 겸 부피형성제로, 잔류수분 ≤ 3%(칼피셔 수분측정법)를 규격으로 삼는다. 트레할로스는 비환원당이라 마이야르 반응으로 단백질 순도를 떨어뜨리지 않는 것이 수크로스 대비 명확한 이점이다. **만니톨**(3–5% w/v)은 이온강도를 바꾸지 않고 삼투압만 **280–320 mOsm/kg**으로 맞춰야 할 때 쓰는 비이온성 삼투질이다.

**DMSO(디메틸설폭사이드)** 는 동결보존액 중 **5–10%(v/v)** 로 쓰이는 세포내 동결보호제이며, **배지·동결보존액 성분이지 매트릭스 성분이 아니다.** 규제상으로는 잔류 용매로 관리된다 — ICH Q3C(R9) 원문(2026-09-14 열람)의 TABLE 3에 DMSO가 **3급(Class 3) 용매**로 등재되어 있고, 3급의 정의는 "인체에 대한 독성 잠재력이 낮아 건강 기반 노출 한도가 필요 없는 용매로, PDE(permitted daily exposure, 1일 허용노출량)가 50 mg/일 이상"이다. 옵션1 기준 잔류 한도는 **5000 ppm(0.5%)**, 정량은 헤드스페이스 기체크로마토그래피(HS-GC)로 한다.

**글리세롤**은 DMSO 대체 동결보호제(10% v/v)이자 건조 매트릭스 가소제다. 중요한 확인 사항이 하나 있다 — **ICH Q3C(R9)의 TABLE 1~3 어디에도 글리세롤은 등재되어 있지 않다**(원문 직접 확인). 따라서 잔류 용매 체계가 아니라 약전 순도 규격과 ISO 10993-17:2023 독성학적 위해평가로 관리한다. 다만 **우지(tallow) 유래 글리세롤은 반추동물 유래 원료**이므로 아래 ③절의 TSE 규제를 그대로 받는다. 식물유 또는 합성 유래임을 원료 출처 증명서로 확보해야 한다.

**메틸셀룰로스** 등 점도 조절제는 바이오프린팅·미세액적 캡슐화에서 액적 안정성과 세포 침강을 제어하며, 전구용액 겉보기 점도 **0.1–2 Pa·s**(회전레오미터, 전단속도 1–100 s⁻¹, 25 °C)와 전단담화 지수 n < 1을 공정 목표로 삼는다.

### 1-5. 항생제 — 배지 성분인가 매트릭스 성분인가

**페니실린-스트렙토마이신(100 U/mL + 100 µg/mL)** 은 **배지 첨가제이며 지지체 구성 성분이 아니다.** 이 구분은 학술적 취향이 아니라 규제 요건이다. EudraLex Volume 4 Part IV(첨단치료의약품 전용 GMP 지침, 유럽위원회 2017-11-22 채택, 2018-05-22 시행) 7.11항 원문은 다음과 같이 규정한다.

> "…it is stressed that the use of antimicrobials does not replace the requirement for aseptic manufacturing. When antimicrobials are used, they should be removed as soon as possible, unless the presence thereof in the finished product is specifically foreseen in the marketing authorisation/clinical trial authorisation (**e.g. antibiotics that are part of the matrix of the finished product**). Additionally, it is important to ensure that antibiotics or antimicrobials do not interfere with the sterility testing, and that they are not present in the finished product…"
> — EudraLex Vol.4 Part IV, §7.11 (2026-09-14 원문 열람)

즉 규제 문헌 자체가 "매트릭스의 일부인 항생제"와 "공정 중 사용 후 제거되어야 하는 항생제"를 명시적으로 구분하며, 후자가 오가노이드 배양의 페니실린-스트렙토마이신에 해당한다. 무균시험 간섭 방지를 위해 Ph. Eur. 2.6.1의 중화물질 사용이 요구되는 것도 같은 조항의 각주(각주 13)에 명시되어 있다. 실무상 더 중요한 함의는, **항생제 상재 사용이 저수준 오염을 은폐해 무균시험 위음성을 만든다**는 점이며, 이는 GMP 등급 전환 시 항생제 무첨가 폐쇄계 제조로 옮겨가야 하는 직접적 이유가 된다(Dossena 2020, DOI:10.1186/s13287-020-1585-2, PMID:32127043; Mizutani 2016, DOI:10.1016/j.reth.2016.06.004, PMID:31245497).

> **해석.** L8은 "싸고 흔한 시약"이라는 인상 때문에 규격 관리에서 가장 늦게 손대는 층이지만, 실제로는 겔의 G′ 산포, 가교 균질성, 무균시험 신뢰도를 직접 결정한다. 특히 PBS–칼슘 비양립성, GDL의 pH 강하폭, 항생제의 규제상 지위 세 가지는 문헌에 잘 드러나지 않으면서 스케일업 단계에서 반드시 문제가 되는 항목이다. 이 층을 규격화해 두면 상위 매트릭스 층의 변수 탐색이 비로소 해석 가능해진다.

---

## ② L9 — 품질·안전 규격 항목

L9는 물질이 아니라 **시험 항목과 판정 기준**의 집합이다. 여기서 가장 흔한 실수는 두 가지다. 하나는 약전·ISO가 정한 법정 기준과 업계 관행 수치를 구분하지 않고 섞어 쓰는 것이고, 다른 하나는 체외 배양용 제품에 체내 이식용 시험을 통째로 부과하거나 반대로 이식용 제품에서 필수 시험을 누락하는 것이다. 아래에서는 **① 법정 근거가 있는 항목은 문서번호·발행일과 함께**, **② 법정 기준이 없는 항목은 그 사실을 명시하고 위해평가 경로를 제시**하는 방식으로 17건을 정리한다. 모든 수치에는 단위와 시험법을 붙였다.

### 2-1. 미생물학적 안전성

**내독소(endotoxin, 그람음성균 세포외막의 지질다당류(LPS)로 미량으로도 TLR4 경로를 통해 세포 반응을 교란하는 발열성 물질)** 는 지지체 원자재의 1차 안전 지표다. 규격은 **≤ 0.5 EU/mL 또는 ≤ 1.0 EU/mg**, 시험법은 **USP \<85\> 세균내독소시험(LAL 겔화법·비탁법·발색법)** 또는 **USP \<86\> 재조합 시약 이용 세균내독소시험**이다. USP \<86\>은 재조합 C인자(rFC)와 재조합 캐스케이드 시약(rCR)을 쓰는 비동물성 시험법으로 **2025-05-01 공식 발효**했다(USP 공지, 2024-11 조기채택 승인). 한도 산출식은 **L = K/M**이며, FDA의 Inspection Technical Guide "Bacterial Endotoxins/Pyrogens" 원문(2026-09-14 열람)은 다음과 같이 규정한다.

> "K is 5.0 EU/kilogram (kg.), which represents the approximate threshold pyrogen dose for humans and rabbits… If a product is labeled for intrathecal injection, then K is 0.2 EU/kg."

생체재료가 내독소에 취약하다는 점은 오래된 문제로, 생체재료 분야에서 내독소가 체계적으로 과소관리되어 왔음을 지적한 종설(Gorbet & Sefton 2005, DOI:10.1016/j.biomaterials.2005.04.063, PMID:16019062)과 키토산 지지체 생체적합성 평가(VandeVord 2002, DOI:10.1002/jbm.1270, PMID:11774317)가 근거를 제공한다.

**생균수(bioburden)** 는 멸균 전 제품에 존재하는 생존 미생물 총수로, 멸균선량 설정의 입력값이다. 시험법은 **ISO 11737-1:2018**(제품 상 미생물 집단 수 측정)이며 회수효율 검증이 필수다. 방사선 멸균에서 **VDmax25**(25 kGy 사용 타당성 입증법)를 적용하려면 평균 생균수를 제품당 100 CFU 이하로 유지하는 것이 일반적 전제이며, 선량 설정 자체는 **ISO 11137-2:2013**이 **무균보증수준(SAL, sterility assurance level) 10⁻⁶** 달성을 위한 25 kGy 또는 15 kGy 사용 타당성 입증 방법을 규정한다.

**무균시험(sterility)** 은 **USP \<71\>** 또는 **Ph. Eur. 2.6.1**에 따라 멤브레인 여과법을 우선 적용하고 14일 배양해 성장 없음을 확인한다. 점성 하이드로겔은 멤브레인 여과가 불가능하거나 필터가 폐색되어 직접접종법에 의존하게 되는데, 이때 검출민감도가 떨어지는 것이 구조적 한계다.

**마이코플라스마(Mycoplasma)** 는 세포벽이 없어 0.22 µm 필터를 통과하고 광학현미경으로 보이지 않는 세균으로, 배양계 만성 오염의 주범이다. 규격은 불검출이며, EudraLex Vol.4 Part IV 7.16항은 "마이코플라스마 오염 위험이 있는 원자재는, 공급자가 해당 원자재가 시험되어 마이코플라스마 음성임을 인증하지 않는 한, 사용 전 여과해야 한다"고 요구한다(원문 열람).

**바이러스 안전성**은 인체·동물 유래 원자재 경로에서 필수다. 일본 **生物由来原料基準**(厚生労働省告示 第210号, 2003-05-20 제정; 令和5年8月30日 厚生労働省告示 第257号 최종개정, 2023-09-01 적용) 제3·제4는 인체/동물 유래 원료에 대해 적절한 단계의 바이러스 시험과 제조공정 중 불활화·제거 처리를 의무화하고, 외래성 바이러스가 검출되면 원칙적으로 사용을 금지한다(원문 열람). FDA 초안 가이던스(2024-04)는 돼지 유래 원료에 대해 돼지써코바이러스(PCV) 1·2형 및 돼지파보바이러스 시험을 추가로 권고한다.

### 2-2. 동물유래성분과 TSE/BSE

**TSE(전달성해면상뇌증, transmissible spongiform encephalopathy — 프리온 단백질에 의해 전파되며 열·방사선·화학적 멸균에 극히 저항성인 신경퇴행성 질환군)** 위험 관리는 동물유래 원자재를 쓰는 순간 자동으로 발생하는 규제 부담이다. 세 개 관할의 요구가 서로 다르며, 다국가 개발에서는 최엄격 기준을 채택해야 한다.

**유럽:** EudraLex Vol.4 Part IV 7.16항은 "Note for Guidance on Minimising the Risk of Transmitting Animal Spongiform Encephalopathy (TSE) Agents via Human and Veterinary Medicinal Products"의 **최신판 준수를 요구**하며, 각주에서 문서번호를 **EMA/410/01 rev.3**으로 명시한다(EudraLex 원문 각주 14, 2026-09-14 열람). 이 지침은 EU 관보 **OJ C 73/1(2011-03-05)** 에 2011/C 73/01로 게재되었고 **적용일은 2011-07-01**이다.

**일본:** 生物由来原料基準 제4-1 **반추동물유래원료기준**은 사용 금지 부위를 조문에 열거한다(원문 열람) — 하수체, 흉선, 경막, 삼차신경절, 송과체, 척수, 척주골(생후 30개월 이하 소 제외), 태반(소 제외), 두개골(생후 30개월 이하 소 제외), 장, 뇌, 뇌척수액, 배근신경절, 비장(소 제외), 부신, 편도, 안구, 림프절. 원산국은 세계동물보건기구(국제수역사무국)가 BSE 병원체 전파 위험을 무시할 수 있다고 판정한 국가 및 조문에 열거된 9개국으로 한정된다. **다만 수모·유·뼈(척주골·두개골 제외) 및 피부 유래 젤라틴(콜라겐 포함)은 "저위험원료"로 분류되어 원산국 제한의 예외**다. 이 조항은 실무적으로 매우 중요한데, **소 진피 유래 I형 콜라겐이 일본 규제상 저위험원료에 해당**한다는 뜻이기 때문이다.

**미국:** FDA 초안 가이던스 "Considerations for the Use of Human- and Animal-Derived Materials in the Manufacture of Cellular and Gene Therapy and Tissue-Engineered Medical Products"(CBER, 2024년 4월; 연방관보 공고 2024-04-30)는 다음과 같이 요구한다(원문 열람).

> "…for bovine-derived materials, including those with indirect contact, you should provide documentation reflecting freedom from adventitious agents and bovine spongiform encephalopathy (BSE) (e.g., documentation that the herds are born, raised, and slaughtered in a country with negligible BSE risk)."

**국제표준:** ISO 22442-1:2020(위험관리 적용), ISO 22442-2:2020(조달·채취·취급 관리), ISO 22442-3:2007(바이러스·TSE 인자 제거/불활화 밸리데이션)이 의료기기 경로의 동물조직 사용을 규율한다.

동물유래 회피 경로는 재조합 인체 콜라겐(RHC), 재조합 라미닌, 식물 유래 나노셀룰로스, 전합성 PEG 매트릭스다. 재조합 콜라겐의 미생물·식물 생산 체계와 조직공학 적용은 문헌적으로 확립되어 있고(Báez 2005, DOI:10.1007/s00253-005-0180-x, PMID:16240115; Yang C 2004, DOI:10.2165/00063030-200418020-00004, PMID:15046526; Davison-Kotler 2019, DOI:10.3390/bioengineering6030056, PMID:31261996), 재조합 인체 콜라겐 각막 이식체는 이미 4년 추적 임상 결과가 보고되어 있다(Fagerholm 2014, DOI:10.1016/j.biomaterials.2013.11.079, PMID:24374070; Islam 2018, DOI:10.1038/s41536-017-0038-8, PMID:29423280).

### 2-3. 화학적 잔류물

**잔류 가교제.** 글루타르알데하이드·카보디이미드(EDC/NHS)·제니핀 등 공유가교제의 잔류량에 대해 **약전 또는 ISO가 정한 단일 법정 수치 한도는 존재하지 않는다.** 관리 경로는 **ISO 10993-17:2023**(의료기기 구성물질의 독성학적 위해평가)으로 허용한계(AL)를 산출하고 **ISO 10993-18**의 화학적 특성 분석으로 추출물 중 잔류량을 정량(HPLC 또는 GC-MS)하는 방식이다. 글루타르알데하이드는 유도체화 후 HPLC-UV로 정량해 검출한계 미만 또는 산출된 AL 미만을 규격으로 설정한다. EDC/NHS계는 반응 후 수용성 요소 유도체로 전환되어 투석으로 제거 가능하며, 세척 종말점은 전도도와 자외부 흡광(A₂₆₀)으로 관리한다.

여기서 잔류량보다 더 근본적인 문제가 있다. **카보디이미드 가교는 콜라겐의 인테그린 결합 부위(GFOGER 모티프 등)를 화학적으로 소실시켜 세포 인식능 자체를 훼손한다**(Bax 2017, DOI:10.1016/j.actbio.2016.11.059, PMID:27915017). 가교제 종류에 따른 조직 고정 특성 비교(Sung 2003, DOI:10.1002/jbm.a.10346, PMID:12579556)와 입체장애가 큰 카보디이미드 대 일반 카보디이미드의 각막 이식체 성능 비교(Ahn 2013, DOI:10.1016/j.actbio.2013.04.014, PMID:23619290)가 이 트레이드오프를 정량적으로 보여준다. 즉 잔류 가교제는 "씻어내면 되는 문제"가 아니라 **가교 방식 선택 자체를 규격 설계 단계에서 재검토해야 하는 문제**다.

**잔류 용매.** ICH Q3C(R9) Step 4(2024-01-24; EU 시행 문서 EMA/CHMP/ICH/82260/2006 Step 5, 2024-04-29 발효) 원문에서 직접 확인한 2급 용매 옵션1 농도한도(1일 10 g 투여 가정)는 다음과 같다.

| 용매 | PDE (mg/일) | 농도한도 (ppm) |
|---|---|---|
| 아세토니트릴 | 4.1 | 410 |
| N,N-디메틸포름아미드(DMF) | 8.8 | 880 |
| 디클로로메탄 | 6.0 | 600 |
| 메탄올 | 30.0 | 3000 |
| N-메틸피롤리돈(NMP) | 5.3 | 530 |
| 1,4-다이옥산 | 3.8 | 380 |
| 톨루엔 | 8.9 | 890 |

3급 용매(DMSO·에탄올·아세톤 등)는 PDE ≥ 50 mg/일, 옵션1 기준 **5000 ppm(0.5%)**. 정량은 HS-GC-FID/MS. PEG 매크로머 합성과 펩타이드 고상합성을 거치는 합성 하이드로겔은 DMF·NMP·DCM 잔류가 실질적 쟁점이며, 다공성 하이드로겔은 용매 회수 정량이 까다롭다.

### 2-4. 생물학적 안전성 시험(체내 이식용 경로)

| 시험 | 규격 | 판정 기준 | 적용 범위 |
|---|---|---|---|
| 세포독성 | ISO 10993-5:2009(제3판, 2022 재확인) | 세포 생존율 ≥ 70%(30% 초과 감소를 세포독성으로 판정) | 이식용 필수, 연구용도 권장 |
| 감작성 | ISO 10993-10:2021 | 감작성 음성(GPMT 또는 LLNA) | 체내 이식용 한정 |
| 자극성 | ISO 10993-23:2021 (+ DAmd1 제정 중, 2024) | 자극성 음성(화학특성분석 → in vitro RhE → in vivo 단계적 접근) | 체내 이식용 한정 |
| 독성학적 위해평가 | ISO 10993-17:2023 | 구성물질별 허용한계(AL) 산출 | 잔류물 관리 근거 |

**확보 실패:** ISO 규격 전문은 유료 문서로 원문을 열람하지 못했다. 위 표의 판번호·표제·현행 여부·개정 구조는 ISO 공식 목록에서 1차 확인했으나, 생존율 70% 기준을 포함한 세부 판정 수치는 규격 본문을 직접 확인하지 못한 통용 기준임을 명시한다.

ECM 기반 생체재료에 ISO 10993-5 표준시험을 그대로 적용하는 것의 한계(L929 마우스 섬유아세포 기반 대사 분석이 실제 거동을 왜곡할 수 있다는 점)는 2026년에도 여전히 논의 대상이다. 한편 오가노이드 자체를 세포독성 평가 플랫폼으로 쓰는 접근은 비용 절감 전략과 함께 실증되었다(Takahashi Y 2023, DOI:10.1038/s41598-023-32438-2, PMID:37012293).

### 2-5. 무균화 방식이 단백질 활성에 미치는 영향

멸균 방식 선택은 무균성과 물성 보존 사이의 직접적 교환이다.

- **감마선·전자선(방사선)**: ISO 11137-1:2025 + ISO 11137-2:2013, SAL 10⁻⁶ 기준 **25 kGy 또는 15 kGy** 사용 타당성 입증. 라디칼 생성으로 사슬 절단과 가교가 동시에 일어나 **G′과 효소분해 거동이 함께 변한다.** 따라서 멸균 전후 G′ 비교 데이터가 규격서에 반드시 포함되어야 한다.
- **에틸렌옥사이드(EO)**: ISO 11135:2014/Amd 1:2018 공정 밸리데이션 + **ISO 10993-7:2026**(제3판, 2026-04 발행) 잔류물 한도. 에틸렌클로로하이드린(ECH)은 **제한노출(24시간 이내) 기준 24시간 내 4 mg 이하**, **영구접촉 기준 1일 평균 0.1 mg 이하이면서 최초 24시간 내 4 mg 이하**. 저온 처리가 가능한 것이 장점이나, 수분을 함유한 하이드로겔에는 가스 침투가 제약된다.
- **여과멸균(0.22 µm)**: 단백질 활성 보존에 가장 유리하며 필터 무결성시험(버블포인트)으로 검증한다. 단 점성 전구용액에서는 필터 폐색과 수율 손실이 발생한다.

**확보 실패:** 검증된 문헌 풀(`landmarks.txt`, `E_spec.txt` 및 동일 수집 계열 파일)에 감마선 조사가 콜라겐 겔의 저장탄성률에 미치는 영향을 정량한 논문이 존재하지 않는다. 따라서 본 항은 규격 문서(ISO 11137-2:2013, ISO 10993-7:2026)를 근거로만 기술했고, 문헌 인용을 붙이지 않았다.

### 2-6. 물성·순도·식별·안정성

**로트 간 저장탄성률(G′) 편차**는 오가노이드 지지체 재현성의 최대 단일 인자다. 시험법은 진동 전단 레오미터로 진폭掃引에서 선형점탄성 영역을 확인한 뒤 주파수掃引(**1 Hz, 변형 1%, 37 °C**)에서 G′·G″를 측정하고, 국소 탄성계수는 원자간력현미경(AFM) 나노압입으로 보완한다(Norman 2021, DOI:10.1038/s41596-021-00495-4, PMID:33854255). 출하규격으로는 **로트 간 G′ 상대표준편차(RSD) ≤ 15%** 를 권고하나, 이것은 법정 기준이 아니라 내부 공정능력 기반 목표값이다. 여기에 더해 **응력이완 시간 τ₁/₂**(초기 응력의 50%가 이완되는 시간)를 병기해야 점탄성 재현성이 비로소 규정된다 — 동일 G′라도 응력이완 거동이 다르면 줄기세포 운명이 달라지기 때문이다(Chaudhuri 2016, DOI:10.1038/nmat4489, PMID:26618884). 정의형 매트릭스에서 탄성계수를 좁은 범위로 제어했을 때 장 오가노이드 형성 효율이 결정된다는 사실이 이 항목의 실질적 근거다(Gjorevski 2016, DOI:10.1038/nature20168, PMID:27851739). 합성·반합성 매트릭스가 배치 간 일관성에서 우위를 갖는다는 점은 GelMA(젤라틴 메타크릴로일) 제조 제어 연구에서 정량적으로 제시되었다(Zhu M 2019, DOI:10.1038/s41598-019-42186-x, PMID:31053756).

**단백질 농도·순도**는 표시량 대비 **90–110%**(BCA 또는 Lowry 비색법, A₂₈₀ 병용), 순도 **≥ 95%**(환원·비환원 SDS-PAGE 밀도측정 또는 크기배제 HPLC 면적백분율)를 규격으로 한다. 콜라겐은 α1/α2 사슬 비 2:1 확인과 하이드록시프롤린 정량을 추가한다. 다만 **동물 조직 추출 기저막 매트릭스는 1,000종 이상의 단백질을 함유하므로 '순도' 규격 자체가 성립하지 않는다**(Hughes 2010, DOI:10.1002/pmic.200900758, PMID:20162561; Benton 2014, DOI:10.1016/j.addr.2014.06.005, PMID:24997339). 이 한 가지 사실이 재조합 단일 단백질 또는 전합성 매트릭스로의 전환 압력을 만드는 가장 직접적인 규격상 근거다.

**비내독소 발열성물질**은 그람양성균 리포테이코산·진균 성분 등 LAL/rFC로 검출되지 않는 발열원을 대상으로 하며, **단구활성화시험(MAT)** 에서 인체 단구가 분비하는 IL-1β·IL-6·TNF-α를 ELISA로 정량한다. 내독소 등가 환산 한도는 L = K/M(K = 5.0 EU/kg)을 준용한다. FDA 기술지침 원문은 토끼 발열성물질시험이 척수강내 제품의 내독소 검출에 감도가 불충분하다고 명시한다.

**식별시험**은 단백질계는 SDS-PAGE 이동도 + 웨스턴블롯 또는 LC-MS/MS 펩타이드 맵핑, 다당류계(알지네이트·히알루론산)는 ¹H-NMR로 M/G 비 또는 이당 단위를 확인하고 FT-IR을 병용한다. USP \<1043\>이 정한 부자재 자격부여 프로그램의 5요소 — 식별(identification), 용도 적합성 및 선정(selection and suitability for use), 특성분석(characterization), 공급자 자격부여(vendor qualification), 품질보증/품질관리 — 중 첫 번째가 바로 이 항목이다.

**안정성·유효기간**은 실시간 안정성시험으로 **0·3·6·12·24개월** 시점에 단백질 농도(90–110%), 순도(≥ 95%), 겔화시간(G′–G″ 교차점), **G′(초기값 대비 ±20% 이내)**, 무균(USP \<71\>), 내독소(≤ 0.5 EU/mL), 외관·pH를 측정해 설정한다. 동결융해 반복 횟수 상한(통상 1회 사용 후 폐기)을 라벨에 명시해야 하며, 콜드체인 이탈이 최종 사용자 단계에서 추적되지 않는 것이 실무상 가장 큰 허점이다.

> **해석.** L9 17건 중 법정 수치 기준이 명확한 것은 내독소·잔류용매·EO 잔류물·방사선 선량 네 가지뿐이고, 나머지는 시험법만 표준화되어 있거나(세포독성·감작성·자극성·식별) 아예 법정 기준이 없다(잔류 가교제, 로트 간 G′ 편차, 안정성). 이 비대칭이 오가노이드 지지체 규격 설계의 본질적 어려움이다 — 제품 성능을 실제로 좌우하는 항목(G′ 산포, 순도)일수록 기댈 법정 기준이 없고, 따라서 **자체 규격을 세우고 그 근거를 문서화하는 능력 자체가 경쟁력**이 된다. 동물 조직 추출물이 '순도' 규격을 원리적으로 세울 수 없다는 점은 기술 선택을 규격 논리로 되밀어 올리는 가장 강한 지점이다.

---

## ③ O8 — 규제·등급 체계

여기서 다루는 질문은 세 가지다. 첫째, 연구용(RUO) 등급과 의약품 제조 등급(GMP grade), 그리고 세포치료제 부자재(ancillary material) 경로가 어떻게 다르고 무엇이 전환 요건인가. 둘째, 동물유래 원료 규제가 미국·유럽·한국·일본에서 어떻게 갈라지는가. 셋째, **오가노이드 지지체는 의약품인가 의료기기인가 부자재인가** — 그리고 이 분류가 개발 경로에 무엇을 강제하는가. 아래 내용은 모두 발행기관 원문 또는 공식 공지를 직접 확인한 것이며, 확인하지 못한 부분은 그렇게 표기했다.

### 3-1. RUO / GMP 등급 / 부자재 — 세 경로의 차이

**연구용(Research Use Only, RUO)** 은 미국에서 체외진단용 제품 라벨링 규제의 맥락에서 정의된 개념으로, FDA 가이던스 "Distribution of In Vitro Diagnostic Products Labeled for Research Use Only or Investigational Use Only"(2013-11-25 연방관보 공고)가 RUO 라벨을 붙인 제품이 임상 진단 목적으로 유통될 때의 문제를 다룬다. 실무적으로 RUO 등급 지지체는 **품질관리 항목이 공급자 재량**이며, 무균시험·바이러스 안전성·안정성 데이터가 없는 경우가 많고 **로트 간 물성 편차가 문서화되지 않는다.**

**GMP 등급(의약품 제조 등급)** 은 최종 제품이 아니라 **원자재 자체가 GMP 체계 하에서 제조**되었음을 뜻한다. 다만 EudraLex Vol.4 Part IV 7.13항 원문은 현실을 이렇게 인정한다.

> "While raw materials should be of pharmaceutical grade, it is acknowledged that, in some cases, only materials of research grade are available. The risks of using research grade materials should be understood (including the risks to the continuity of supply when larger amounts of product are manufactured). Additionally, the suitability of such raw materials for the intended use should be ensured, including where appropriate by means of testing (e.g. functional test, safety test)."
> — EudraLex Vol.4 Part IV, §7.13 (2026-09-14 원문 열람)

**즉 유럽 ATMP GMP는 연구용 등급 원자재의 사용을 전면 금지하지 않는다.** 대신 (a) 위험을 이해할 것, (b) **대량 생산 시 공급 연속성 위험을 포함해** 평가할 것, (c) 기능시험·안전시험으로 용도 적합성을 입증할 것을 요구한다. 같은 조항은 Ph. Eur. 5.2.12를 고려하도록 지시하며, 7.15항은 "EU에서 의약품으로 허가된 원자재(예: 사이토카인, 인혈청알부민, 재조합 단백질)에 대해서는 공급자의 시험성적서가 요구되지 않는다"고 규정해 **허가 의약품을 원자재로 쓰는 것을 명시적으로 장려**한다.

**부자재(ancillary material) 경로**의 표준 문서는 두 개다.

- **USP \<1043\> Ancillary Materials for Cell, Gene, and Tissue-Engineered Products** (DOI: 10.31003/USPNF_M620_02_01). 부자재의 정의는 **"최종 제품에 존재하도록 의도되지 않은 물질"** 이며, 위험도에 따라 4단계 티어로 분류한다(아래는 USP 공식 판본 원문 표현).
  - **Tier 1** — "Low-risk, highly qualified materials that are well-suited for use in manufacturing. The AM is either a licensed biologic, an approved drug, an approved or cleared medical device, or it is intended for use as an implantable biomaterial."
  - **Tier 2** — "Low-risk, well-characterized material that are well-suited for use in manufacturing. Their intended use is for drug, biologic, or medical device manufacture."
  - **Tier 3** — "Moderate risk material that will require a higher level of qualification than previous tier materials. Frequently, these materials are produced for in vitro diagnostic use."
  - **Tier 4** — "The highest risk level for AMs. Extensive qualification is necessary prior to use in manufacturing. The material is not produced in compliance with cGMPs."
  
  자격부여 프로그램은 식별, 선정 및 용도 적합성, 특성분석, 공급자 자격부여, 품질보증/품질관리의 5요소로 구성된다.
- **Ph. Eur. 5.2.12 Raw materials of biological origin for the production of cell-based and gene therapy medicinal products** — 유럽약전위원회가 **2015년 11월 17–18일 스트라스부르 회기에서 채택**했다(EDQM 공지). 생물유래 원자재의 위험평가와 추적성 요건을 규정하며, EudraLex ATMP GMP 7.13항이 이를 참조하도록 지시한다.

**현재 시판되는 오가노이드용 기저막 매트릭스는 USP \<1043\> 기준 Tier 4(cGMP 하에서 제조되지 않은 최고위험 부자재)에 해당하며, 이것이 임상 전환의 병목이다.** 원자재 관리의 위험 기반 접근과 상업화 전환 요건은 문헌적으로도 체계화되어 있다(Scott 2020, DOI:10.1016/j.jcyt.2020.06.011, PMID:32713719; Solomon 2025, DOI:10.1007/978-3-031-97297-3_8, PMID:41136834; Atouf 2016, DOI:10.1208/s12248-016-9935-9, PMID:27233803). 유럽에서는 ATMP 원자재 자격부여를 위한 인증제도 도입의 타당성 조사까지 진행되었다(Le Maux 2023, PMID:37711032, DOI 없음).

### 3-2. 국가별 차이

| 관할 | 핵심 문서 | 확인된 내용 | 접근일 |
|---|---|---|---|
| **미국** | FDA 초안 가이던스 "Considerations for the Use of Human- and Animal-Derived Materials in the Manufacture of Cellular and Gene Therapy and Tissue-Engineered Medical Products" (CBER, 2024-04; 연방관보 2024-04-30) | 소 유래 원료는 간접 접촉 포함 BSE 위험 무시 가능국 출생·사육·도축 문서 요구; 돼지 유래는 PCV 1·2형·파보바이러스 시험; TEMP의 지지체 분류 조항(3-3절) | 2026-09-14 |
| | FDA "Content and Review of CMC Information for Human Somatic Cell Therapy INDs" (2008-04) | 세포치료제 IND의 CMC 정보 구성 — 부자재/시약 항목 포함 | 2026-09-14 |
| | USP \<1043\>, \<85\>, \<86\>, \<71\> | 부자재 티어 체계 및 시험법 | 2026-09-14 |
| **유럽** | EudraLex Vol.4 Part IV ATMP GMP (EC 채택 2017-11-22, 시행 2018-05-22) | §7.10–7.24 원자재·출발물질 요건(원문 열람) | 2026-09-14 |
| | Ph. Eur. 5.2.12 (2015-11 채택) | 생물유래 원자재 위험평가·추적성 | 2026-09-14 |
| | EMA/410/01 rev.3 TSE 지침 (OJ C 73/1, 2011-03-05; 적용 2011-07-01) | 반추동물 유래 원료 TSE 위험 최소화 | 2026-09-14 |
| | EMA "Guideline on human cell-based medicinal products" (EMEA/CHMP/410869/2006; 공개 2008-05-21, 발효 2008-09-01) | 세포기반의약품의 품질·비임상·임상 개발 요건 | 2026-09-14 |
| **한국** | 첨단재생의료 및 첨단바이오의약품 안전 및 지원에 관한 법률(첨단재생바이오법), **법률 제20331호, 공포 2024-02-20, 시행 2025-02-21** | 첨단바이오의약품 규제의 근거 법률 — 세포치료제·유전자치료제·조직공학제제를 별도 범주로 규율 | 2026-09-14 |
| | MFDS **세포치료제 품질관리 시험항목 설정 가이드라인**(민원인 안내서 **안내서-0306-03**, 등록 **2023-06-23**) | 세포치료제 품질관리 시험항목 설정 지침 | 2026-09-14 |
| | 대한민국약전 제13개정 전부개정 고시 (**2026-06-29 고시**) — PDG·ICH 최신 가이드라인 반영, 28개 품목 규격 개선, 흡입제 전달량 균일성시험법 및 핵산기반기법 신설 | 국내 약전 시험법의 국제조화 강화 | 2026-09-14 |
| **일본** | **生物由来原料基準**(厚生労働省告示 第210号, 제정 2003-05-20; 최종개정 令和5年8月30日 厚生労働省告示 第257号, 적용 2023-09-01) | 제1 통칙 — 의약품·의약부외품·화장품·의료기기·**재생의료등제품**에 사용되는 인체 및 동물(식물 제외) 유래 원료(첨가제·배지 등 제조공정 사용물 포함)에 적용; 제4-1 반추동물유래원료기준 — 금지 부위 18개 열거, 원산국 제한, **수모·유·뼈·피부 유래 젤라틴(콜라겐 포함)은 저위험원료로 예외** | 2026-09-14 |
| **국제** | ISO 22442-1:2020 / -2:2020 / -3:2007, ISO 10993 시리즈, ISO 11137·11135·11737 | 의료기기 경로의 동물조직·생물학적 안전성·멸균 | 2026-09-14 |
| | AATB **Standards for Tissue Banking 제15판**(2024년 발표, **2025년 1월 시행**; Revision 2, 2025-08-11 시행). 발행기관 현행 명칭은 Association for Advancing Tissue and Biologics | 인체 조직은행 표준 — 인체 유래 ECM 원료 조달 경로에 적용 | 2026-09-14 |

**한국·일본의 구조적 차이 한 가지:** 일본의 生物由来原料基準은 제1 통칙에서 "**添加剤、培地等として製造工程において使用されるもの**"(첨가제·배지 등으로 제조공정에서 사용되는 것)을 명시적으로 적용 범위에 포함시킨다. 즉 최종 제품에 남지 않는 배지 성분·부자재까지 고시의 직접 규율 대상이다. 이는 미국의 부자재 개념(최종 제품에 존재하도록 의도되지 않은 물질 — USP \<1043\>)이 별도 티어 체계로 관리되는 구조와 접근이 다르며, **일본 시장 진입 시 배지·완충액 수준까지 원산지 문서를 요구받을 수 있다**는 뜻이다. 일본 내 자가세포 제조 시설의 오염 경험 사례는 이 규제 강도의 배경을 보여준다(Mizutani 2016, DOI:10.1016/j.reth.2016.06.004, PMID:31245497).

한국은 오가노이드 **시험법** 쪽에서 선도적 움직임이 있다. 식약처 식품의약품안전평가원은 2025-06-16 보도자료로 **오가노이드 시험법 국제표준화 추진위원회** 발족을 공고했고(담당: 독성연구과), ISO·OECD를 통한 국제표준 개발을 목표로 한다. **확보 실패:** 이 추진위원회가 목표로 하는 ISO/OECD 표준의 구체적 문서번호는 아직 부여되지 않았거나 공개 확인이 불가능해 기재하지 않는다.

### 3-3. 오가노이드 지지체는 의약품인가, 의료기기인가, 부자재인가

이것이 O8의 핵심 질문이며, 답은 **"지지체가 최종 제품에 남는가"** 하나로 갈린다.

**(가) 지지체가 최종 제품에 남지 않는 경우 — 부자재.** 오가노이드를 배양·확장한 뒤 지지체를 효소·킬레이트 처리로 제거하고 세포만 투여한다면, 지지체는 USP \<1043\>의 부자재 정의("최종 제품에 존재하도록 의도되지 않은 물질")에 정확히 부합한다. 이 경우 지지체는 독립된 허가 대상이 아니라 **세포치료제 CMC 문서의 한 항목**으로 평가되며, 티어 분류에 따른 자격부여와 잔류량 관리가 요구된다. **체외 배양 전용 연구용 제품도 실질적으로 이 경로**이며, 창약 스크리닝·독성평가용으로 팔리는 오가노이드 배양 매트릭스가 여기에 속한다.

**(나) 지지체가 최종 제품에 남는 경우 — 조합제품의 기기 구성요소.** FDA 초안 가이던스(2024-04) 제VIII장 "Tissue-Engineered Medical Products"는 이 상황을 직접 다룬다(원문 열람).

> "TEMPs commonly incorporate cells and scaffolds… **Unlike other types of materials used in product manufacturing, scaffolds may be an integral part of the final formulated TEMP that contributes to the intended therapeutic effect.** … In cases where TEMPs include a device constituent derived from animal sources (e.g., **an animal-derived scaffold used as a part of a cell-scaffold construct may be classified as a device constituent part in certain TEMPs**), we recommend that you follow the recommendations in the FDA guidance 'Medical Devices Containing Materials Derived from Animal Sources (Except for In Vitro Diagnostic Devices)…' dated March 2019"

같은 장은 ECM 지지체에 대해서도 명시한다.

> "Extracellular matrix scaffolds and proteins abundant in the extracellular matrix (e.g., collagen) derived from animals may also be used in TEMPs. As for all animal-derived materials, it is important to document the sourcing and testing of animal tissues and to document capabilities of the manufacturing and sterilization processes to eliminate animal pathogens."

탈세포 조직 매트릭스에 대해서는 세포물질(생존·비생존 모두) 부재 증명, 탈세포화 및 최종멸균 방법 문서화, 무균보증수준 문서화, 그리고 바이러스 불활화를 탈세포화·멸균에 의존하는 경우 **공정 단계별 log₁₀ 감소값의 총합(전체 바이러스 감소 계수)** 제출을 요구한다.

**(다) 분류 판정 경로.** 최종 제품이 세포와 지지체의 조합이면 미국에서는 21 CFR Part 3(Product Jurisdiction)의 조합제품 규율을 받으며, 분류가 불확실하면 지정요청(Request for Designation, RFD) 절차로 공식 판정을 받는다. 관련 가이던스는 "Classification of Products as Drugs and Devices & Additional Product Classification Issues"(2017-09-26 연방관보 공고)다. **확보 실패:** eCFR이 접근 차단(302 리다이렉트)되어 21 CFR 1271.10(a)의 HCT/P 4요건 원문과 21 CFR Part 3 조문을 직접 열람하지 못했다. 문서 표제와 존재만 확인했다.

**(라) 개발에 미치는 영향.** 분류가 갈리면 다음이 전부 달라진다.

1. **규격 항목 범위** — 부자재 경로는 잔류량 관리가 핵심이고 감작성·자극성 시험은 통상 불필요하다. 기기 구성요소 경로는 ISO 10993 시리즈 전체(세포독성·감작성·자극성·독성학적 위해평가)와 멸균 밸리데이션이 필수가 된다.
2. **동물유래 규제 강도** — 기기 구성요소가 되는 순간 ISO 22442 시리즈와 FDA 2019년 3월 동물유래 의료기기 가이던스가 추가로 적용된다.
3. **심사 주체와 기간** — 부자재는 세포치료제 IND/허가 심사에 흡수되지만, 기기 구성요소는 조합제품 관할 판정을 거쳐야 하고 RFD 절차 자체가 일정 변수다.
4. **공급자 계약 구조** — 부자재는 공급자 자격부여와 기술규격 합의(EudraLex 7.14 — "critical raw materials의 기술규격은 가능한 한 공급자와 합의해야 한다")로 충분하지만, 기기 구성요소는 설계이력파일(DHF)급 문서 접근이 필요해진다.

**따라서 실무적 권고는 명확하다: 제품 기획 단계에서 "지지체를 최종 제품에서 제거할 것인가"를 먼저 결정하고, 그 결정을 규격 설계의 최상위 분기점으로 삼아야 한다.** 이 결정을 미루면 두 경로의 요구사항을 모두 충족시키는 과잉 규격을 만들게 되고, 비용은 대략 두 배가 된다.

### 3-4. 오가노이드에 대한 미국 규제 동향 — 정확한 사실관계

여기서 흔히 유통되는 부정확한 서술을 바로잡을 필요가 있다. **"미국 식품의약국(FDA)이 오가노이드를 승인/허용했다"는 것은 사실이 아니다.** 확인된 사실관계는 다음과 같다.

**1) FDA Modernization Act 2.0 (2022-12-29 법률 성립).** 상원 법안 S.5002(제117대 의회)로 발의되어 2022-09-29 상원 만장일치 통과, 이후 **Consolidated Appropriations Act, 2023(Public Law 117-328)의 Division FF, Section 3209 "Animal Testing Alternatives"** 로 포함되어 2022-12-29 서명·성립했다. 개정 내용은 연방식품의약품화장품법(FD&C Act) 505(i)조의 **"preclinical tests (including tests on animals)"** 라는 문구를 **"nonclinical tests"** 로 대체하고, 이를 "in vitro, in silico, or in chemico, or a nonhuman in vivo test"로 정의한 것이다. 즉 **신약 임상시험계획(IND) 진입 요건에서 동물시험을 법적으로 의무화하던 조항이 삭제되고 대체 시험법 수용 경로가 열린 것**이며, 세포 기반 분석·오간칩·미세생리시스템·컴퓨터 모델링·바이오프린팅 등이 예시로 열거된다. **오가노이드는 그 대체법 목록 중 하나로 언급될 뿐이고, 개별 제품이 승인되거나 특정 방법이 의무화된 것이 아니다.**

**2) FDA 동물시험 단계적 폐지 계획 (2025-04-10).** FDA는 2025-04-10 보도자료 "FDA Announces Plan to Phase Out Animal Testing Requirement for Monoclonal Antibodies and Other Drugs"를 발표했다(원문 열람). 핵심 문언은 다음과 같다.

> "The FDA's animal testing requirement will be reduced, refined, or potentially replaced using a range of approaches, including AI-based computational models of toxicity and cell lines and organoid toxicity testing in a laboratory setting (so-called New Approach Methodologies or NAMs data). **Implementation of the regimen will begin immediately for investigational new drug (IND) applications, where inclusion of NAMs data is encouraged**, and is outlined in a roadmap also being released today."
>
> "**Human-Based Lab Models:** The FDA will promote the use of lab-grown human 'organoids' and organ-on-a-chip systems that mimic human organs – such as liver, heart, and immune organs – to test drug safety."
>
> "Over the coming year, the FDA aims to launch a pilot program allowing select monoclonal antibody developers to use a primarily non-animal-based testing strategy, under close FDA consultation. Findings from an accompanying pilot study will inform broader policy changes and **guidance updates expected to roll out in phases**."

같은 날 "Roadmap to Reducing Animal Testing in Preclinical Safety Studies"가 함께 공개되었다(보도자료가 "a roadmap also being released today"로 명시).

**3) 이것이 수요에 미치는 영향 — 점진적 증가이지 계단식 도약이 아니다.** 법문과 FDA 문언 어디에도 오가노이드 사용 의무나 시한이 없다. 2022년 법 개정은 동물시험을 **선택 가능**하게 만들었을 뿐이고, 2025년 로드맵은 IND에서 NAMs 데이터 포함을 **"권장(encouraged)"** 하며 정책·가이던스 변경은 **"단계적으로(in phases)"** 진행된다고 스스로 못박고 있다. 파일럿 프로그램도 단일클론항체 개발사 일부를 대상으로 한다. 따라서 오가노이드 배양 지지체 수요는 **규제 신호의 누적에 따라 점진적으로 증가하는 형태**로 보는 것이 문헌과 원문에 부합하며, 특정 시점의 계단식 수요 도약을 전제한 사업 계획은 근거가 없다. 한편 한국 식약처가 2025-06 오가노이드 시험법 국제표준화 추진위원회를 발족한 것(3-2절)은 같은 흐름의 아시아 측 신호다.

> **해석.** 규제 체계는 오가노이드 지지체를 독립된 제품 범주로 인정하지 않는다 — 그것은 언제나 상위 제품(세포치료제, 조직공학의료제품, 또는 연구용 시약)의 부속으로 규율된다. 이 구조가 의미하는 바는, 지지체 공급자가 확보해야 할 자산이 "허가"가 아니라 **고객의 CMC 문서에 그대로 붙일 수 있는 문서 패키지**(원산지 증명, 티어 분류 근거, 시험성적서, 안정성 데이터, 규제 지원 문서)라는 점이다. 규제가 제품이 아니라 문서를 요구할 때, 경쟁 우위도 제품이 아니라 문서에서 난다.

---

## ④ 등급 전환 시 실무 과제

RUO 등급으로 출발한 지지체를 GMP 등급 또는 부자재 경로로 옮기는 일은 "같은 물건에 서류를 붙이는 작업"이 아니다. 대부분의 경우 **원료 조달 경로, 제조 공정, 시험 체계, 문서 체계 네 가지가 동시에 바뀌어야 하며**, 어느 하나만 바꾸면 나머지에서 막힌다. 아래는 이 전환에서 실제로 병목이 되는 과제를 우선순위 순으로 정리한 것이다. 각 과제마다 근거 문서와 판단 기준을 함께 제시한다.

### 4-1. 원료 조달 — 동물유래 의존의 해소 또는 문서화

가장 먼저 결정해야 할 것은 동물유래 원료를 **문서화로 유지할 것인가, 재조합·합성으로 대체할 것인가**다.

- **유지 경로:** 원산국 증명(BSE 위험 무시 가능국 출생·사육·도축), 금지 부위 불사용 증명, 로트별 추적성 확보가 필요하다. 일본 기준의 금지 부위 목록이 가장 구체적이므로 이를 최엄격 기준으로 삼는 것이 효율적이다. **단, 소 피부 유래 콜라겐은 일본 기준상 저위험원료에 해당해 원산국 제한을 받지 않는다** — 이 예외 조항을 정확히 활용하면 조달 비용을 크게 줄일 수 있다.
- **대체 경로:** 재조합 인체 콜라겐(효모·CHO·식물 발현), 재조합 라미닌, 식물 유래 나노셀룰로스, 전합성 PEG 매트릭스. 기술적 실현 가능성은 문헌적으로 확립되어 있다(Báez 2005, PMID:16240115; Yang C 2004, PMID:15046526; Curvello 2020, DOI:10.1002/advs.202002135, PMID:33437574; Cruz-Acuña 2017, DOI:10.1038/ncb3632, PMID:29058719; Aisenbrey & Murphy 2020, DOI:10.1038/s41578-020-0199-8, PMID:32953138). 다만 **재조합 단백질 생산 자체가 배지·발효 원료를 통해 동물유래 성분을 재도입할 수 있으므로** 발효 공정까지 추적해야 한다. 이 함정은 인체 유래 단백질에 대해 FDA 초안 가이던스가 직접 경고한다 — 배지의 트랜스페린이나 인혈청알부민은 배지 시험성적서만 봐서는 존재가 드러나지 않으므로 제조사에 별도로 확인해야 한다는 취지다(원문 열람).
- 무혈청·이종유래 무첨가 배양계로의 이행은 합의 문서와 다수의 실증 연구가 뒷받침한다(Karnieli 2017, DOI:10.1016/j.jcyt.2016.11.011, PMID:28017599; Lu HF 2014, DOI:10.1016/j.biomaterials.2013.12.050, PMID:24411336; Shaikh 2026, DOI:10.1016/j.crmeth.2026.101538, PMID:42526442; Ong 2026, DOI:10.1088/2752-5724/ae4e4d, PMID:42089082). 인간 혈소판용해물의 병원체 저감 처리 같은 중간 해법도 검증되어 있다(Viau 2017, DOI:10.1371/journal.pone.0181406, PMID:28763452).

### 4-2. 로트 간 재현성 — 규격을 세울 수 있는 물질로의 이행

RUO→GMP 전환에서 기술적으로 가장 어려운 지점은 **"순도 규격을 세울 수 없는 물질로는 GMP 등급을 만들 수 없다"** 는 사실이다. 동물 조직 추출 기저막 매트릭스는 1,000종 이상의 단백질 혼합물이므로(Hughes 2010, PMID:20162561) 식별시험과 순도시험이 원리적으로 형식화될 수밖에 없고, 그 결과 로트 간 G′ 산포를 관리할 근거도 확보되지 않는다. 반면 화학 정의형 매트릭스는 처방과 공정 변수로 G′를 직접 설계할 수 있다(Gjorevski 2016, PMID:27851739; Chaudhuri 2016, PMID:26618884; Ng S 2019, DOI:10.1016/j.biomaterials.2019.119400, PMID:31398570; Ye S 2020, PMID:34658689; Liu J 2026, DOI:10.1002/adhm.71498, PMID:42568046). GelMA는 제조 제어를 통해 배치 간 일관성을 크게 높일 수 있음이 정량적으로 제시되었다(Zhu M 2019, PMID:31053756). 매트리겔 없는 오가노이드 배양의 현황과 한계를 정리한 종설도 이 전환의 실무 지도를 제공한다(Kozlowski 2021, DOI:10.1038/s42003-021-02910-8, PMID:34893703).

**실행 규칙:** 로트 간 G′ RSD ≤ 15%와 응력이완 시간 τ₁/₂ 병기를 출하규격에 넣을 수 있는지를 기술 선택의 판정 기준으로 삼는다. 넣을 수 없다면 그 물질로는 GMP 등급 전환이 성립하지 않는다.

### 4-3. 시험 체계의 확장

RUO 단계에서 통상 수행하지 않던 항목이 한꺼번에 추가된다. 항목별 신규 부담은 다음과 같다.

| 신규 항목 | 근거 | 리드타임·부담 |
|---|---|---|
| 무균시험 | USP \<71\> / Ph. Eur. 2.6.1 | 14일 배양 — 단기 유효기간 제품의 출하 일정에 직접 영향 |
| 마이코플라스마 | EudraLex 7.16 | 공급자 인증으로 갈음 가능(위험평가 문서화 전제) |
| 바이러스 안전성 | 生物由来原料基準 제3·제4, FDA 2024-04 초안 | 인체·동물 유래 원료 사용 시 공정 클리어런스 연구 필요 — 비용 부담 최대 |
| 비내독소 발열성물질(MAT) | 체내 이식용 경로 | 공여자 단구 로트 의존성으로 시험 간 변동 큼 |
| 안정성(실시간) | 유효기간 설정 | 24개월 데이터 확보에 최소 24개월 — **가장 긴 리드타임** |
| 잔류 용매 | ICH Q3C(R9) | HS-GC 밸리데이션 |
| 생물학적 안전성(ISO 10993 시리즈) | 체내 이식용 경로에 한정 | 체외 배양 전용 제품에는 불필요 — 범위 오판 시 비용 낭비 |

여기에 더해, 지지체 선택은 **지지체 자체의 시험 항목을 넘어 최종 세포 제품의 시험 부담까지 바꾼다.** 일본 규제 체계에서 요구되는 잔존 미분화세포 검출(액적 디지털 PCR 기반 고감도 정량법이 확립되어 있다 — Kuroda 2015, DOI:10.1016/j.reth.2015.08.001, PMID:31245455)과 종양원성 평가(Yasuda & Sato 2015, DOI:10.1016/j.biologicals.2015.05.008, PMID:26071041)는 지지체가 세포 분화·증식 거동에 영향을 주는 만큼 매트릭스 변경 시 재수행 여부를 판단해야 하는 항목이다. 즉 매트릭스 변경은 지지체 규격서만의 문제가 아니라 하류 제품 시험 계획의 변경 관리 대상이다.

**리드타임 관점의 실행 규칙:** 실시간 안정성시험은 전환 결정과 동시에 착수해야 한다. 다른 모든 시험은 사후 보완이 가능하지만 24개월 안정성 데이터만은 시간을 압축할 수 없다.

### 4-4. 문서 체계와 공급자 관계

EudraLex Vol.4 Part IV 7.14–7.15항은 원자재 문서 체계에 대해 다음을 요구한다(원문 열람 요약).

- 중요 원자재(critical raw material)의 규격에는 용도 적합성 확보를 위한 품질 요건과 **판정 기준(acceptance criteria)** 을 포함해야 하며, 기술규격은 **가능한 한 공급자와 합의**해야 한다.
- 어떤 원자재가 중요한지의 판정은 제조자(또는 스폰서·허가권자)가 구체적 위험에 비추어 수행하고, **그 결정을 문서화**해야 한다.
- 감독과 추가 시험의 수준은 개별 원자재가 제기하는 위험에 **비례**해야 하며, 위험이 충분히 이해되고 완화 조치(예: 공급자 자격부여)가 갖춰져 있다면 **공급자 시험성적서에 의존하는 것도 수용 가능**하다.

이 세 문장이 지지체 공급자에게 주는 함의는 분명하다. **고객(세포치료제 개발사)이 위험 기반으로 "이 원자재는 중요하지 않다"고 판정할 수 있게 만들어 주는 문서를 제공하는 쪽이 채택된다.** 구체적으로는 USP \<1043\> 티어 분류 근거, 원산지·동물유래 성분 선언서, 로트별 시험성적서(내독소·무균·마이코플라스마·G′), 안정성 요약, 변경관리 통지 약정(change notification agreement)이 최소 구성이다. GMP 제조 전환의 조직적 요건과 세포치료 분야의 표준 개발 동향은 관련 문헌이 정리하고 있다(Jayaraman 2021, DOI:10.3389/fcell.2021.648472, PMID:33928083; Cao J 2021, DOI:10.1002/sct3.13035, PMID:34724717; Hayakawa 2015, DOI:10.1016/j.biologicals.2015.05.010, PMID:26272542; Torre 2015, DOI:10.1089/scd.2014.0299, PMID:25517941; Nozaki 2026, DOI:10.1016/j.jcyt.2026.102821, PMID:42462592).

### 4-5. 공급 연속성 — 규제가 명시적으로 요구하는 항목

EudraLex 7.13항이 연구용 등급 원자재의 위험에 **"including the risks to the continuity of supply when larger amounts of product are manufactured"** 를 명시한 것은 주목할 만하다. 즉 공급 연속성은 상업적 고려가 아니라 **GMP 지침이 직접 요구하는 위험평가 항목**이다. 실무적으로는 이중 공급원 확보, 안전재고 정책, 제조소 변경 시 동등성 입증 계획을 문서로 갖추는 것을 의미한다. 생물학적 변동성이 제조 계획에 미치는 영향은 메타분석 수준에서 정리되어 있다(Thurman-Newell 2015, DOI:10.1111/vox.12288, PMID:26174339).

### 4-6. 전환 의사결정 체크리스트

1. **지지체를 최종 제품에서 제거하는가?** → 아니오면 조합제품 기기 구성요소 경로(ISO 10993 전체 + ISO 22442 + 멸균 밸리데이션). 예면 부자재 경로(잔류량 관리 중심).
2. **동물유래 원료를 유지하는가?** → 유지면 3개 관할 최엄격 기준(일본 금지 부위 목록)으로 원산지 문서 체계 구축. 대체면 발효 원료까지 추적.
3. **로트 간 G′ RSD ≤ 15%를 출하규격으로 걸 수 있는가?** → 불가면 GMP 등급 전환 자체를 재검토.
4. **24개월 실시간 안정성시험을 지금 착수했는가?** → 미착수면 즉시 착수(압축 불가한 유일한 리드타임).
5. **멸균 방식을 확정했는가?** → 방사선 선택 시 멸균 전후 G′ 비교 데이터, EO 선택 시 ISO 10993-7:2026 잔류물 규격, 여과 선택 시 필터 폐색·수율 손실 평가를 각각 규격서에 편입.
6. **고객 CMC에 그대로 붙일 수 있는 문서 패키지가 있는가?** → 없으면 제품 성능과 무관하게 임상 개발사 채택에서 탈락.

> **해석.** 등급 전환에서 실제로 시간이 걸리는 것은 시험이 아니라 **되돌릴 수 없는 선택들** — 원료 조달 경로, 매트릭스 화학, 멸균 방식 — 이다. 이 셋은 한 번 정하면 안정성 데이터가 리셋되므로 뒤늦게 바꾸면 24개월을 다시 잃는다. 따라서 전환 계획은 시험 항목 나열이 아니라 **이 세 가지 선택을 언제 잠글 것인가의 일정표**로 작성되어야 한다. 규제 문서가 요구하는 것의 대부분은 기술이 아니라 결정의 근거이며, 결정을 미루는 것 자체가 가장 비싼 선택이다.

---

## 부록 A. 1차 출처를 직접 확인한 규제·표준 문서 (접근일 전부 2026-09-14)

**미국**
1. FDA. *Considerations for the Use of Human- and Animal-Derived Materials in the Manufacture of Cellular and Gene Therapy and Tissue-Engineered Medical Products — Draft Guidance for Industry*. CBER, 2024년 4월. 연방관보 공고 2024-04-30. (본문 원문 열람)
2. FDA. *Medical Devices Containing Materials Derived from Animal Sources (Except for In Vitro Diagnostic Devices); Guidance for Industry and FDA Staff*. 2019년 3월. (위 문서 Ref.14로 인용 확인)
3. FDA. *Distribution of In Vitro Diagnostic Products Labeled for Research Use Only or Investigational Use Only; Guidance for Industry and FDA Staff*. 2013-11-25 연방관보 공고.
4. FDA. *Classification of Products as Drugs and Devices & Additional Product Classification Issues*. 2017-09-26 연방관보 공고.
5. FDA. *Content and Review of CMC Information for Human Somatic Cell Therapy INDs — Guidance for FDA Reviewers and Sponsors*. 2008년 4월.
6. FDA. *Inspection Technical Guide: Bacterial Endotoxins/Pyrogens*. (K/M 산출식·K값 원문 열람)
7. FDA 보도자료. *FDA Announces Plan to Phase Out Animal Testing Requirement for Monoclonal Antibodies and Other Drugs*. 2025-04-10. (원문 열람)
8. FDA. *Roadmap to Reducing Animal Testing in Preclinical Safety Studies*. 2025-04-10. (표제·발행일 확인; 본문 PDF는 접근 제한)
9. FDA Modernization Act 2.0 — S.5002(제117대 의회) → Public Law 117-328, Division FF, §3209 "Animal Testing Alternatives", 2022-12-29 성립.
10. USP 〈1043〉 *Ancillary Materials for Cell, Gene, and Tissue-Engineered Products*. DOI: 10.31003/USPNF_M620_02_01. (현행판 존재 확인 + 공식 판본 원문에서 4티어 정의 축자 확인)
11. USP 〈86〉 *Bacterial Endotoxins Test Using Recombinant Reagents*. 공식 발효 2025-05-01(2024-11 조기채택 승인).
12. USP 〈85〉 *Bacterial Endotoxins Test*; USP 〈71〉 *Sterility Tests*.
13. ANSI/AAMI ST72:2019 *Bacterial endotoxins — Test methods, routine monitoring, and alternatives to batch testing*. (표제·판년 확인; 수치 한도 미열람)

**유럽**
14. EudraLex Volume 4, Part IV — *Guidelines on Good Manufacturing Practice specific to Advanced Therapy Medicinal Products*. 유럽위원회 채택 2017-11-22, 시행 2018-05-22. (§7.10–7.24 원문 열람)
15. Ph. Eur. 5.2.12 *Raw materials of biological origin for the production of cell-based and gene therapy medicinal products*. 유럽약전위원회 2015-11-17/18 회기 채택(EDQM 공지).
16. EMA/410/01 rev.3 — *Note for Guidance on Minimising the Risk of Transmitting Animal Spongiform Encephalopathy Agents via Human and Veterinary Medicinal Products*. OJ C 73/1, 2011-03-05(2011/C 73/01), 적용 2011-07-01.
17. EMA. *Guideline on human cell-based medicinal products*. EMEA/CHMP/410869/2006. 공개 2008-05-21, 발효 2008-09-01.
18. Ph. Eur. 2.6.1 *Sterility* (EudraLex 각주 13으로 확인).
19. ICH Q3C(R9) *Impurities: Guideline for Residual Solvents*. Current Step 4 version, 2024-01-24. (원문 PDF TABLE 2·TABLE 3 축자 확인)
20. EMA/CHMP/ICH/82260/2006 — ICH Q3C(R9) Step 5, EU 발효 2024-04-29.

**한국**
21. 첨단재생의료 및 첨단바이오의약품 안전 및 지원에 관한 법률. 법률 제20331호, 공포 2024-02-20, 시행 2025-02-21.
22. 식품의약품안전처. *세포치료제 품질관리 시험항목 설정 가이드라인*(민원인 안내서). 안내서-0306-03, 등록 2023-06-23.
23. 식품의약품안전처. 대한민국약전 제13개정 전부개정 고시. 2026-06-29. (고시번호·시행일은 미확인 — 부록 B 참조)
24. 식품의약품안전처 보도참고자료. *오가노이드 시험법 국제표준화를 위한 추진위원회 발족*. 2025-06-16, 독성연구과.

**일본**
25. 生物由来原料基準. 厚生労働省告示 第210号, 2003-05-20 제정. 최종개정 令和5年8月30日 厚生労働省告示 第257号, 2023-09-01 적용. (제1 통칙, 제3 ヒト由来原料総則, 제4 動物由来原料総則 원문 열람)

**국제표준**
26. ISO 10993-5:2009 (제3판, 2022 재확인) — 체외 세포독성 시험
27. ISO 10993-7:2026 (제3판, 2026-04) — 에틸렌옥사이드 멸균 잔류물
28. ISO 10993-10:2021 — 피부감작성 시험
29. ISO 10993-23:2021 (+ DAmd1:2024 제정 중) — 자극성 시험
30. ISO 10993-17:2023 — 의료기기 구성물질의 독성학적 위해평가
31. ISO 11137-1:2025 / ISO 11137-2:2013 — 방사선 멸균
32. ISO 11135:2014 / Amd 1:2018 (ISO/FDIS 11135 개정 진행 중) — EO 멸균
33. ISO 11737-1:2018 — 생균수 측정
34. ISO 22442-1:2020 / -2:2020 / -3:2007 — 동물조직 이용 의료기기

**조직은행 표준**
35. AATB. *Standards for Tissue Banking*, 제15판. 2024년 발표, 2025년 1월 시행; Revision 2 시행 2025-08-11. 발행기관 현행 명칭 Association for Advancing Tissue and Biologics.

---

## 부록 B. 확보 실패 항목 (9건)

1. **USP 〈1043〉 현행판 전문** — USP-NF 온라인 구독 필요. 티어 정의는 USP 공식 판본(USP32–NF27) 원문에서 축자 확보해 대체했으며, 현행판의 표제·식별자·DOI는 doi.usp.org에서 확인.
2. **Ph. Eur. 5.2.12 전문** — EDQM 유료 문서. 채택 경위·표제·채택 회기는 EDQM 공지로 확인, 조문 세부는 미열람.
3. **ISO 규격 전문(10993 시리즈, 11137, 11135, 11737, 22442)** — 전부 유료 문서. 표제·판번호·발행연도·현행 여부는 ISO 공식 목록으로 확인했으나, ISO 10993-5의 생존율 70% 판정 기준 등 세부 수치는 규격 본문 미열람 상태의 통용 기준임.
4. **ANSI/AAMI ST72:2019의 기기별 내독소 한도 수치** — 유료 규격으로 수치 미확인. 본문에서는 약전 K/M 산출식만 사용했으며 기기별 고정 한도값은 기재하지 않음.
5. **대한민국약전 제13개정의 고시번호 및 시행일** — 2026-06-29 고시 사실은 확인했으나 고시번호와 시행일을 1차 출처에서 확정하지 못함.
6. **21 CFR 1271.10(a) 및 21 CFR Part 3 조문 원문** — eCFR 접근이 302 리다이렉트로 차단됨. 문서 표제와 존재만 확인.
7. **감마선 조사가 콜라겐 겔 저장탄성률에 미치는 영향의 정량 논문** — 검증된 문헌 풀에 해당 논문 부재. 규격 문서 근거만으로 기술하고 논문 인용을 붙이지 않음.
8. **잔류 글루타르알데하이드의 법정 수치 한도** — 약전·ISO 어디에도 단일 수치 한도가 존재하지 않음을 확인 범위 내에서 파악. ISO 10993-17:2023 기반 허용한계 산출 경로로 대체 기술.
9. **오가노이드 지지체 전용 ISO/OECD 표준 문서번호** — 식약처 추진위원회(2025-06)가 목표로 하는 표준의 문서번호가 아직 부여되지 않았거나 공개 확인 불가.

---

## 부록 C. 인용 논문 목록 (51편, 전부 검증된 문헌 풀 수록 서지)

| # | 저자·연도 | 저널 | DOI | PMID |
|---|---|---|---|---|
| 1 | Gjorevski N et al. 2016 | Nature | 10.1038/nature20168 | 27851739 |
| 2 | Sato T et al. 2009 | Nature | 10.1038/nature07935 | 19329995 |
| 3 | Aisenbrey EA, Murphy WL 2020 | Nat Rev Mater | 10.1038/s41578-020-0199-8 | 32953138 |
| 4 | Hughes CS et al. 2010 | Proteomics | 10.1002/pmic.200900758 | 20162561 |
| 5 | Benton G et al. 2014 | Adv Drug Deliv Rev | 10.1016/j.addr.2014.06.005 | 24997339 |
| 6 | Kozlowski MT et al. 2021 | Commun Biol | 10.1038/s42003-021-02910-8 | 34893703 |
| 7 | Kim S et al. 2022 | Nat Commun | 10.1038/s41467-022-29279-4 | 35354790 |
| 8 | Giobbe GG et al. 2019 | Nat Commun | 10.1038/s41467-019-13605-4 | 31827102 |
| 9 | Capeling MM et al. 2019 | Stem Cell Reports | 10.1016/j.stemcr.2018.12.001 | 30612954 |
| 10 | Chooi WH et al. 2023 | Adv Healthc Mater | 10.1002/adhm.202202342 | 36502337 |
| 11 | Pilipenko N et al. 2019 | Carbohydr Polym | 10.1016/j.carbpol.2019.115035 | 31426956 |
| 12 | Curvello R et al. 2020 | Adv Sci | 10.1002/advs.202002135 | 33437574 |
| 13 | Cruz-Acuña R et al. 2017 | Nat Cell Biol | 10.1038/ncb3632 | 29058719 |
| 14 | Broguiere N et al. 2018 | Adv Mater | 10.1002/adma.201801621 | 30203567 |
| 15 | Chaudhuri O et al. 2016 | Nat Mater | 10.1038/nmat4489 | 26618884 |
| 16 | Norman MDA et al. 2021 | Nat Protoc | 10.1038/s41596-021-00495-4 | 33854255 |
| 17 | Zhu M et al. 2019 | Sci Rep | 10.1038/s41598-019-42186-x | 31053756 |
| 18 | Ye S et al. 2020 | Adv Funct Mater | 10.1002/adfm.202000893 | 34658689 |
| 19 | Ng S et al. 2019 | Biomaterials | 10.1016/j.biomaterials.2019.119400 | 31398570 |
| 20 | Turco MY et al. 2017 | Nat Cell Biol | 10.1038/ncb3516 | 28394884 |
| 21 | Lu HF et al. 2014 | Biomaterials | 10.1016/j.biomaterials.2013.12.050 | 24411336 |
| 22 | Shaikh N et al. 2026 | Cell Rep Methods | 10.1016/j.crmeth.2026.101538 | 42526442 |
| 23 | Ong J et al. 2026 | Materials Futures | 10.1088/2752-5724/ae4e4d | 42089082 |
| 24 | Gorbet MB, Sefton MV 2005 | Biomaterials | 10.1016/j.biomaterials.2005.04.063 | 16019062 |
| 25 | VandeVord PJ et al. 2002 | J Biomed Mater Res | 10.1002/jbm.1270 | 11774317 |
| 26 | Karnieli O et al. 2017 | Cytotherapy | 10.1016/j.jcyt.2016.11.011 | 28017599 |
| 27 | Torre ML et al. 2015 | Stem Cells Dev | 10.1089/scd.2014.0299 | 25517941 |
| 28 | Scott M et al. 2020 | Cytotherapy | 10.1016/j.jcyt.2020.06.011 | 32713719 |
| 29 | Atouf F 2016 | AAPS J | 10.1208/s12248-016-9935-9 | 27233803 |
| 30 | Solomon JN et al. 2025 | Adv Exp Med Biol | 10.1007/978-3-031-97297-3_8 | 41136834 |
| 31 | Nozaki Y et al. 2026 | Cytotherapy | 10.1016/j.jcyt.2026.102821 | 42462592 |
| 32 | Le Maux S et al. 2023 | Pharmeuropa Bio Sci Notes | (DOI 없음) | 37711032 |
| 33 | Jayaraman P et al. 2021 | Front Cell Dev Biol | 10.3389/fcell.2021.648472 | 33928083 |
| 34 | Hayakawa T 2015 | Biologicals | 10.1016/j.biologicals.2015.05.010 | 26272542 |
| 35 | Dossena M et al. 2020 | Stem Cell Res Ther | 10.1186/s13287-020-1585-2 | 32127043 |
| 36 | Mizutani M et al. 2016 | Regen Ther | 10.1016/j.reth.2016.06.004 | 31245497 |
| 37 | Viau S et al. 2017 | PLoS One | 10.1371/journal.pone.0181406 | 28763452 |
| 38 | Cao J et al. 2021 | Stem Cells Transl Med | 10.1002/sct3.13035 | 34724717 |
| 39 | Kuroda T et al. 2015 | Regen Ther | 10.1016/j.reth.2015.08.001 | 31245455 |
| 40 | Yasuda S, Sato Y 2015 | Biologicals | 10.1016/j.biologicals.2015.05.008 | 26071041 |
| 41 | Thurman-Newell JA et al. 2015 | Vox Sang | 10.1111/vox.12288 | 26174339 |
| 42 | Báez J et al. 2005 | Appl Microbiol Biotechnol | 10.1007/s00253-005-0180-x | 16240115 |
| 43 | Davison-Kotler E et al. 2019 | Bioengineering | 10.3390/bioengineering6030056 | 31261996 |
| 44 | Yang C et al. 2004 | BioDrugs | 10.2165/00063030-200418020-00004 | 15046526 |
| 45 | Fagerholm P et al. 2014 | Biomaterials | 10.1016/j.biomaterials.2013.11.079 | 24374070 |
| 46 | Islam MM et al. 2018 | NPJ Regen Med | 10.1038/s41536-017-0038-8 | 29423280 |
| 47 | Ahn JI et al. 2013 | Acta Biomater | 10.1016/j.actbio.2013.04.014 | 23619290 |
| 48 | Sung HW et al. 2003 | J Biomed Mater Res A | 10.1002/jbm.a.10346 | 12579556 |
| 49 | Bax DV et al. 2017 | Acta Biomater | 10.1016/j.actbio.2016.11.059 | 27915017 |
| 50 | Takahashi Y et al. 2023 | Sci Rep | 10.1038/s41598-023-32438-2 | 37012293 |
| 51 | Liu J et al. 2026 | Adv Healthc Mater | 10.1002/adhm.71498 | 42568046 |

특허 인용: 0건(본 에이전트 범위 외).

