# Phase 007 — Content Category Architecture

## Executive Summary
시장/경쟁/지표 정렬 결과를 바탕으로 6개의 핵심 콘텐츠 카테고리를 정의했다. 각 카테고리는 직무 세그먼트, 가치 제안, KPI와 연결되어 생산 캘린더·알림 전략을 동시에 설계할 수 있도록 구성했다.

## Category Framework
| 카테고리 | 대상 세그먼트 | 톤/형식 | 주기 | KPI 연결 |
| --- | --- | --- | --- | --- |
| **Ops Laugh Lab** | 운영/지원 | 체크리스트형 밈 | 주 5회 | 큐레이터 배치 처리량, 출처 배지 |
| **Product Panic Room** | PM/PO | 스토리 카드 | 주 5회 | MAJR, 체류 시간 |
| **Marketing Meme Board** | 마케터/광고 | 슬라이드 카드 | 주 4회 | 공유율, 파트너 리포트 |
| **Dev Standup Satires** | 개발자 | 코드 스니펫 + punchline | 주 3회 | 직무 재방문, 버그 리포트 CTA |
| **Exec Trend Roast** | 경영/광고주 | 인포그래픽형 | 주 2회 | 파트너 리포트, Revenue |
| **All-hands Catch-up** | 전체 | 주간 요약 | 주 1회 | 온보딩 완료율, 푸시 CTR |

## Editorial Guardrails
1. 모든 카테고리는 원문 링크/출처를 포함하고 3단 구조(상황→업계 맥락→한국식 punchline)를 따른다.
2. 재작성 템플릿은 Phase 004 결정(6개 업계)과 동일하게 유지.
3. 카드 컬러/아이콘 시스템을 정의해 직관적으로 구분.
4. KPI 연결을 명시해 콘텐츠 성과가 바로 측정되도록 태깅.
5. 알림/공유 CTA는 각 카테고리에 맞춘 기본값을 제공.

## Requirement Updates
### Functional
1. **FR-031: 카테고리 메타데이터 스키마** — 톤, 주기, KPI 태그를 포함하는 YAML/JSON 정의.
2. **FR-032: 카테고리별 생산 캘린더** — 큐레이터가 주당 슬롯을 예약.
3. **FR-033: KPI 태깅 자동화** — 게시 시 카테고리별 KPI가 자동 연결.
4. **FR-034: 알림/공유 기본값 설정** — 카테고리마다 Push/CTA 템플릿을 자동 로드.
5. **FR-035: 카테고리 성과 대시보드** — 카테고리 단위로 Leading/Lagging 지표를 시각화.

### Non-functional
- **NFR-020 카테고리 SLA**: 정의된 주기 준수율 95% 이상.
- **NFR-021 일관성**: 카테고리별 템플릿 재사용률 80% 이상.
- **NFR-022 데이터 연결성**: KPI 태깅 정확도 98% 이상.

## Dependencies
- FR-031~FR-035는 Phase 011/012 UI·API와 Phase 018 데이터 파이프라인에 모두 의존.
- 카테고리별 주기 준수는 Phase 019 워크플로 설계와 Phase 021 콘텐츠 Ops 툴킷에서 지원.
- Exec Trend Roast 카테고리는 Phase 024 파트너 세션에서 베타 공유.

## Guardrails & Approvals
- 카테고리 예시는 모두 재작성하여 `translation-guardrails.md`의 저작권/출처 규칙을 준수했다.
- 워크숍 참석자 20명 중 19명 찬성, 반대 1건은 Dev 카테고리 주기를 늘리라는 의견으로 Phase 008에서 재검토 예정이다.
