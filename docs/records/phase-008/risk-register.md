# Phase 008 — Risk Register

| ID | 카테고리 | 설명 | 영향 | 대응 전략 | 상태 |
| --- | --- | --- | --- | --- | --- |
| RSK-036 | 수익 | Ops/Product 스폰서 번들이 KPI 향상을 입증하지 못할 수 있음 | CPM 인상 실패, 파이프라인 축소 | Phase 018 보고서에 전/후 지표 비교, Issue Tracker `#ISS-188` 실험 태깅 | 계획 중 |
| RSK-037 | 운영 | 스폰서 검수 추가 시간으로 큐레이터 SLA(95%)가 위협 | 일정 지연, 품질 저하 | Phase 019 워크플로 슬롯 재배치, 백업 큐레이터 예산 확보 | 모니터링 |
| RSK-038 | 기술 | Transparency 증빙 패키지 자동화가 실패하면 수동 PDF 생성 필요 | 리드타임 증가, 오류 가능 | 로컬 모델 로깅을 이중화, YAML 설정을 CI에서 검증 (`translation-guardrails.md` 준수) | 완화 중 |
| RSK-039 | 제품 | Exec 선공개 구독이 무료 사용자 경험을 훼손할 위험 | 이탈/불만 증가 | 콘텐츠 선공개 범위 명시, CTA에 원문 링크 유지, Issue Tracker `#ISS-233` 피드백 훅 추가 | 계획 중 |

## Escalation Notes
- KPI 미충족 시 Revenue/Product 공동 리뷰 후 가설 수정, 모든 변경은 `translation-guardrails.md` 체크리스트와 함께 재검증.
- 운영 SLA가 92% 이하로 떨어지면 Phase 019 용량 계획을 즉시 재조정한다.
