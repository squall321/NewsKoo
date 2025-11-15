# Phase 006 — Decision & Dependency Log

| ID | 날짜 | 결정 내용 | 근거 | 영향/의존성 |
| --- | --- | --- | --- | --- |
| DEC-026 | 2024-06-04 | North Star를 "월간 활성 직무 독자"로 확정 | 세그먼트 온보딩 데이터를 활용해야 함 | Phase 011 UX, Phase 090 알림 전략 KPI 정렬 |
| DEC-027 | 2024-06-04 | 데이터 스택은 DuckDB+S3+Airbyte 조합으로 구성 | 비용 0~5만원/월, 로컬 실행 가능 | Phase 018 데이터 파이프라인 설계 반영 |
| DEC-028 | 2024-06-05 | 출처 배지 누락률 0.5% 이하를 품질 OKR로 설정 | 신뢰 지표 상위 | Phase 011 UI, Phase 065 품질 대시보드 필수 항목 |
| DEC-029 | 2024-06-06 | Leading 지표는 주간 리뷰, Lagging은 월간 리뷰 | 리소스 제약, 의사결정 리듬 정합 | Phase 050 실험 플래닝, 경영 리뷰 캘린더 반영 |
| DEC-030 | 2024-06-07 | KPI 카탈로그를 YAML/Repo 기반으로 관리 | 버전 관리, 협업 용이 | Phase 040 Analytics, DevOps 파이프라인 연동 |

## Alignment Notes
- 지표 정의는 `translation-guardrails.md`에서 규정한 데이터 보존/비용 한계를 준수한다.
- 콘텐츠 카테고리별 지표 분해는 Phase 007 Action Item으로 이관했다.
