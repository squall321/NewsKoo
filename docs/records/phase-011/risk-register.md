# Phase 011 — Risk Register & Guardrail Tracker

Phase 011에서 도출된 Guardrail/리스크 요구사항은 KPI 증빙 신뢰와 Exec 선공개 실험을 동시에 보호해야 하므로 전용 백로그(ISS-311~319)에 즉시 반영했다.

## Impact / Likelihood Scale
| 점수 | 영향도 정의 | 발생도 정의 |
| --- | --- | --- |
| 5 | KPI/수익 손실 또는 North Star 붕괴 | 페이즈 범위 내 반복 가능 |
| 4 | 출시 지연·비용 초과 | 페이즈 중 1회 이상 가능 |
| 3 | 국지적 기능 지연 | 조건부 발생 |
| 2 | 단일 작업 영향 | 낮음 |
| 1 | 미미 | 매우 낮음 |

## Risk Inventory
| ID | 카테고리 | 설명 | 영향 | 발생 | 점수 | 요구사항/대응 | 상태 | 백로그/소유 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSK-044 | 고객 신뢰/템플릿 | Exec 선공개 템플릿과 무료 사용자 카피가 분리되면 CTA/출처가 불일치해 NPS가 하락. | 4 | 3 | 12 | FR-041, FR-044, NFR-027을 통해 단일 템플릿 엔진·QA 체크리스트를 강제. | 완화 중 | Issue `#ISS-311`(스토리), `#ISS-314`(서브태스크). 소유: Product + Platform |
| RSK-045 | 증빙 거버넌스 | KPI 증빙 패널이 QA/태깅과 분리되면 스폰서 번들 신뢰(재구매율 40%)가 붕괴. | 5 | 3 | 15 | FR-042, FR-043, NFR-026으로 KPI 카탈로그와 UI를 동기화하고 QA 체크리스트를 자동화. | 계획 중 | Issue `#ISS-312`(Story), `#ISS-313`(연계). 소유: Product Ops + Data |
| RSK-046 | 비용/가드레일 | GPU Telemetry·캐시가 없으면 translation guardrails 비용 상한을 초과하거나 폴백이 동작하지 않음. | 4 | 4 | 16 | FR-045, NFR-025, NFR-028을 통해 Telemetry 훅과 캐시 폴백을 구현하고 위반 시 배포 차단. | 계획 중 | Issue `#ISS-315`~`#ISS-319`. 소유: Infra + Platform |

## Guardrail Actions
- GPU/비용 로그를 Phase 018 보고서와 Steering Committee 주간 리포트에 첨부(DEC-046).
- 템플릿 변경 시 QA 체크리스트 결과를 `docs/strategy/translation-guardrails.md` 첨부 양식으로 기록.
- KPI 증빙 패널 QA 실패 시 24h 내 Revenue/Product 공동 RCA 세션을 소집해 Issue Tracker에 기록.
