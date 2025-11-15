# Phase 008 — Stakeholder Workshop Minutes

## Session Details
- **일시**: 2024-06-18 10:00-12:00 KST
- **참석**: Product Lead, Revenue Lead, Content Lead, Data Lead, Legal Advisor, 2명 큐레이터 대표
- **목적**: Phase 007 카테고리 전략과 시장 리서치(Phase 003) 기반 수익 가설 정렬
- **준수 기준**: 모든 모델/콘텐츠 결정은 `docs/strategy/translation-guardrails.md`의 로컬 모델 우선·출처 투명성 규정을 재확인했다.

## Agenda & Notes
1. **카테고리별 수익 연계성 검토**
   - Ops/Product 카테고리 주당 슬롯을 스폰서 번들로 묶는 안을 재확인.
   - KPI 태깅 자동화 상태(Phase 007 DEC-034)와 연동해 보고서를 자동 생성해야 한다는 의견 제시.
2. **투명성 증빙 패키지 설계**
   - 광고 파트너 콜 인사이트(Phase 003) 공유.
   - Legal Advisor는 상용 API 사용 시 `translation-guardrails.md`상 사전 승인 필요를 재차 강조.
   - 데이터 팀은 로컬 LLaMA-3-8B 캐시를 활용하면 로그 생성 비용이 월 5만원 내로 유지된다고 보고.
3. **Exec 프리미엄 구독 모델**
   - Exec Trend Roast/All-hands Catch-up 선공개 실험 아이디어 수집.
   - Push/알림 템플릿은 Phase 090 설계와 호환되어야 하므로 CTA 변수 정의를 Issue Tracker `#ISS-233`에 기록하기로 함.
4. **리스크 및 의존성 식별**
   - 큐레이터 대표는 스폰서 슬롯 증가가 검수 시간을 늘려 SLA를 위협할 수 있다고 우려.
   - 데이터 팀은 증빙 패키지 자동화가 실패하면 수동 PDF 생성으로 전환해야 한다고 경고.

## Consensus Outcomes
| 항목 | 합의 내용 | 후속 조치 |
| --- | --- | --- |
| Revenue Hypotheses | HYP-008A/B/C를 Phase 008 공식 가설로 승인 | Decision Log에 기록, Issue Tracker `#ISS-188/#ISS-205/#ISS-219` 연결 |
| 모델/가드레일 | 로컬 7B~8B 번역 모델 유지, 상용 API는 예외 승인 시에만 사용 | Guardrail 체크리스트를 Phase 018 로그 파이프라인에 추가 |
| 보고서 자동화 | KPI 태깅 + Transparency 로그를 YAML 설정으로 통합 | Phase 018 작업 항목을 Issue Tracker `#ISS-241`로 생성 |
| Exec 구독 실험 | 선공개 콘텐츠 접근 제어와 Push 템플릿을 2주 내 설계 | Phase 011/090 담당자가 실험 브리프 초안 작성 |
| 큐레이터 용량 | 스폰서 검수 추가 시간(콘텐츠당 +6분)을 워크플로 슬롯에 반영 | Phase 019 용량 계획에 반영, 위험 항목은 Risk Register RSK-037로 추적 |

## Action Items
1. Revenue Lead: 스폰서 번들 가격표 초안(Ops/Product) 작성 — 6/20까지.
2. Data Lead: 증빙 로그 자동화를 위한 YAML 스키마 제안 — 6/21까지.
3. Content Lead: Exec 선공개 템플릿 샘플 제작 — 6/24까지.
4. Product Lead: Issue Tracker `#ISS-241`/`#ISS-233`에 의존성 태그와 일정 기입.
