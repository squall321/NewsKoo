# Phase 011 — Vision & Requirements Alignment

## Executive Summary
Phase 011은 Phase 003 시장 통찰, Phase 006 KPI 트리, Phase 007 카테고리 전략, Phase 008 수익 가설, Phase 009 리스크 대응 방안을 통합해 **직무 기반 가치 제안과 투명성·가드레일 요구사항**을 하나의 실행 스펙으로 묶는 것을 목표로 한다. 워크숍에서는 "월간 활성 직무 독자" North Star(DEC-026)와 스폰서 번들 KPI(Phase 008 HYP-008A/B/C)를 동시에 만족하기 위해 **알림·템플릿, KPI 증빙 패널, Guardrail Telemetry**를 핵심축으로 삼았다.

## KPI & Upstream Inputs
| 출처 | 핵심 시사점 | Phase 011 영향 |
| --- | --- | --- |
| Phase 003 리서치 합성 | 모바일 68%·직무 세그먼트 중심, 출처 투명성 35% 영향 | 카드형 CTA·원문 매크로·출처 패널 요구.|
| Phase 006 KPI 트리/DEC-026 | North Star = 월간 활성 직무 독자, KPI 카탈로그 YAML 관리 | 온보딩/템플릿에서 직무 필수 수집 및 KPI 태깅 자동화.|
| Phase 007 카테고리 전략/DEC-031~035 | 6개 카테고리, Ops/Product 우선, KPI 태깅 자동화 | 템플릿/리포트에 KPI ID 노출, 태그 누락 모니터링.|
| Phase 008 수익 가설(HYP-008A/B/C)/DEC-037 | 스폰서 번들에 KPI 보고서 번들 포함, Exec 선공개 실험 | KPI 증빙 패널과 Exec Push 템플릿을 동일 설계.|
| Phase 009 리스크(RSK-041~043)/DEC-040~042 | GPU 비용/가드레일, 고객 신뢰 유지, 증빙 로그 QA | 템플릿 캐싱·Guardrail Telemetry·QA 체크리스트 필수화.|

## Requirement Breakdown
### Functional Requirements
| ID | 설명 | KPI 정렬 | 우선순위 | 선행/의존성 | 담당 조직 |
| --- | --- | --- | --- | --- | --- |
| **FR-041: 직무 기반 알림·CTA 템플릿 엔진** | 카테고리·직무·가설(EX-008-03) 별로 Push/Email 템플릿을 구성하고 Exec 선공개·무료 사용자 텍스트를 동시 관리. | Push CTR, Exec ARPU(Phase 008), North Star 활성 독자(Phase 006). | Must | Phase 007 템플릿 가이드, Phase 090 알림 실행, Issue `#ISS-311` 스토리. | Product(소유) + Platform(구현) |
| **FR-042: 스폰서 KPI 증빙 패널** | Ops/Product 번들 KPI를 큐레이션 UI와 리포트에 동시 노출, QA 체크리스트·카테고리 태그 자동 연결. | 스폰서 재구매율/CPM (HYP-008A/B), KPI 태깅 정확도(NFR-022). | Must | Phase 018 로그 스키마, Phase 019 워크플로, Issue `#ISS-312`. | Product Ops(소유) + Data(구현) |
| **FR-043: 직무 온보딩 계측 & KPI 태깅 브리지** | 온보딩 단계에 직무·세그먼트 수집을 강제하고 KPI 카탈로그(YAML)와 자동 동기화. | North Star 활성 독자, KPI Tree 정확도(NFR-017). | Must | Phase 006 KPI 카탈로그, Phase 021 마케팅, Issue `#ISS-313`. | Growth(소유) + Product Ops(지원) |
| **FR-044: 투명성 배지·원문 CTA 매크로** | Exec/무료 구독 모두에 출처 배지, 원문 링크, 재작성 이유 매크로를 강제하고 로그에 전파. | 출처 누락률 ≤0.5%(DEC-028), 고객 신뢰(NPS). | Should | Phase 012 NPS 리서치, translation guardrails, Issue `#ISS-314`. | Translation Guardrails Guild |
| **FR-045: Guardrail Telemetry 대시보드 훅** | GPU 스케줄·번역 캐시·비용 메트릭을 템플릿 스펙과 연동해 위반 시 알람. | Guardrail 비용(translation guardrails), KPI 증빙 신뢰. | Should | Phase 018 데이터 파이프라인, Infra GPU 스케줄러, Issue `#ISS-315`. | Infra(소유) + SRE(알람) |

### Non-functional Requirements
| ID | 설명 | KPI/제약 | 우선순위 | 선행/의존성 | 담당 조직 |
| --- | --- | --- | --- | --- | --- |
| **NFR-025: Guardrail 성능 한도** | Exec 선공개 템플릿은 RTX 5070 Ti 16GB 환경에서 배치 추론 6초 이내, GPU 비용은 guardrail 문서 상한 준수. | RSK-041, translation guardrails 비용. | Must | Infra GPU 스케줄링, Issue `#ISS-316` 모니터링. | Infra + Platform |
| **NFR-026: KPI 데이터 거버넌스** | KPI 로그 익명화·30일 원문/365일 재작성 보존 정책을 템플릿 및 리포트 모듈에 적용. | Phase 003 데이터 보존, RSK-030. | Must | Data Platform, Legal, Issue `#ISS-317`. | Data Platform + Legal |
| **NFR-027: 템플릿 일관성 QA** | 알림/리포트 템플릿은 경 시 QA 체크리스트(Phase 009 DEC-040) 통과 및 2인 승인. | KPI 증빙 신뢰, 고객 신뢰. | Should | Product Ops, QA, Issue `#ISS-318`. | Product Ops + QA |
| **NFR-028: 세그먼트 캐시 안정성** | 직무/카테고리 캐시 미스는 1% 이하, 실패 시 폴백 템플릿 제공. | Push CTR, Exec ARPU. | Could | Platform Team, Issue `#ISS-319`. | Platform |

## Risk & Guardrail Traceability
| 요구사항 | 연결된 리스크 | 대응 전략/백로그 |
| --- | --- | --- |
| FR-041, FR-044, NFR-027 | RSK-044 | 템플릿 엔진을 단일화하고 QA 체크리스트를 translation guardrails 체크인에 첨부. Issue `#ISS-311`, `#ISS-314`, `#ISS-318`. |
| FR-042, FR-043, NFR-026 | RSK-045 | KPI 카탈로그 싱크·QA 자동화를 Phase 018/019 파이프라인에 통합. Issue `#ISS-312`, `#ISS-313`, `#ISS-317`. |
| FR-045, NFR-025, NFR-028 | RSK-046 | GPU Telemetry, 캐시 폴백, 비용 알람을 Infra 모니터링에 추가. Issue `#ISS-315`, `#ISS-316`, `#ISS-319`. |

- 모든 guardrail 관련 요구사항은 translation guardrails 문서와 GPU/비용 로그를 주간 리포트에 첨부하도록 정의했다.

### Sprint Story Export
- `FR-041`~`FR-045`는 Product/Infra 합동 백로그에 `#ISS-311`~`#ISS-315`로 등록되어 Phase 012, 018, 090 스프린트 계획에 배정.
- `NFR-025`~`NFR-028`은 데이터 거버넌스 및 모니터링 태스크로 `#ISS-316`~`#ISS-319`에 반영되어, 각 담당 조직이 주차별 책임자를 지정했다.

## Approval Workshop Outcomes
- **참석자**: Product(4), Data(2), Infra(2), Marketing(1), Sales Enablement(1) — 총 10명.
- **합의율**: 9/10 (90%). 반대 1건은 Exec 선공개 범위 축소 요청으로 Phase 012 실험 설계에 추가 검토 Action Item 생성.
- **미해결 항목**:
  1. Exec 선공개 컨텐츠 범위 축소 여부 (Phase 012 실험 결과 대기, Owner: Marketing).
  2. KPI 증빙 패널에서 파트너별 커스텀 위젯 제공 필요성 (Phase 018 데이터 모델 영향 분석, Owner: Product Ops).

## Next Steps & Traceability
1. Issue Tracker `#ISS-311`~`#ISS-319`로 스토리/태스크를 생성해 Phase 012~019 스프린트 백로그에 등록.
2. Decision/Dependency 및 Risk Register 문서를 본 문서와 연결해 Steering Committee에 공유.
3. translation guardrails 체크리스트를 Phase 011 산출물 패키지에 첨부하고 비용·GPU 로그를 주 단위 보고.
