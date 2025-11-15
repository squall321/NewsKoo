# Phase 006 — Success Metrics Blueprint

## Executive Summary
가치 제안을 측정할 KPI 트리를 정의하고, 각 지표별 소스·도구·책임자를 지정했다. Leading 지표(콘텐츠 생산/검수 속도, 세그먼트 온보딩)와 Lagging 지표(재방문, 파트너 매출)를 연결해 이후 실험이 어떤 지표를 움직이는지 추적 가능하도록 했다.

## KPI Tree
| 레벨 | 지표 | 유형 | 목표 | 데이터 소스 | 비고 |
| --- | --- | --- | --- | --- | --- |
| North Star | 월간 활성 직무 독자(MAJR) | Lagging | 50k (12M) | 웹/앱 이벤트 | 직무 선택 완료 기준 |
| Growth Driver | 세그먼트 온보딩 완료율 | Leading | 80% | 온보딩 이벤트 | Phase 005 영향 |
| Content Driver | 큐레이터 배치당 승인 카드 수 | Leading | 10건 | 검수 로그 | 모델 캐시 지표 연동 |
| Quality Driver | 출처 배지 노출률 | Leading | 99.5% | 퍼블리싱 로그 | 투명성 배지 의무 |
| Engagement Driver | 카드당 평균 체류 시간 | Lagging | 45초 | 웹/앱 분석 | 모바일 우선 기준 |
| Revenue Driver | 파트너 증빙 리포트 발송 수 | Lagging | 월 30건 | 로그 Export | 광고 파이프라인 |

## Measurement Framework
1. **데이터 계층** — Snowflake 대체로 DuckDB+S3 조합을 사용, Airbyte 무료 커넥터로 이벤트 수집.
2. **모니터링 주기** — Leading 지표는 주간, Lagging 지표는 월간 리뷰.
3. **책임 체계** — Product Ops가 KPI 대시보드 오너, Data 팀은 검증.
4. **실험 연계** — Phase 050 실험 플랫폼에 KPI 태그를 연결해 Impact를 자동 기록.
5. **법무/비용 가드레일** — 로그 데이터에서 PII 제거, 로컬 저장 우선.

## Requirements Updates
### Functional
1. **FR-026: KPI 카탈로그** — 지표 정의/소스/쿼리를 YAML로 관리하고 UI에 노출.
2. **FR-027: 검수 로그 스트림** — 큐레이터 배치 성과를 실시간 집계.
3. **FR-028: 세그먼트 온보딩 이벤트 스키마** — 직무/숙련도 선택 데이터를 익명화하여 저장.
4. **FR-029: 출처 배지 품질 경보** — 배지 누락 시 슬랙/메일 알림.
5. **FR-030: 리포트 전송 추적기** — 파트너 리포트 발송 현황을 KPI 대시보드와 연동.

### Non-functional
- **NFR-017 데이터 정확도**: KPI 산출값 오차 ±2% 이내.
- **NFR-018 지표 최신성**: Leading 지표 2시간, Lagging 지표 24시간 내 업데이트.
- **NFR-019 보안**: KPI 데이터는 로컬 저장 후 익명 처리, 외부 공유 시 승인 필요.

## Dependencies
- FR-026~FR-030은 Phase 018 로그 파이프라인과 Phase 040 Growth Analytics에 기술 의존.
- KPI 대시보드는 Phase 065 품질/성장 리뷰와 연동, Phase 090 알림 전략 지표로 확장.
- 이벤트 스키마는 Phase 011/012 개발에 전달하여 구현 동시 진행.

## Guardrails & Approvals
- 지표 정의 과정에서 `translation-guardrails.md`의 데이터 보존/비용 원칙을 준수했고, 상용 API 미사용을 재확인했다.
- 워크숍에서 10/11 찬성, 반대 1건은 콘텐츠 카테고리 지표 상세 요청으로 Phase 007에 반영한다.
