# Phase 009 — Decision & Dependency Log

Phase 009 워크숍에서는 수익 가설(HYP-008A/B/C) 실행을 위한 증빙/비용/고객 신뢰 리스크 완화 전략에 합의했다.

| ID | 날짜 | 결정 내용 | 근거 | 영향/의존성 |
| --- | --- | --- | --- | --- |
| DEC-040 | 2024-06-25 | 스폰서 KPI 증빙을 위해 Phase 018 로그 스키마에 "번들 KPI 매핑"과 QA 체크리스트를 추가하고 Sales Enablement 미리보기 리포트를 함께 제공한다. | HYP-008A/B 워크숍 노트, RSK-040·042 시나리오 영향 분석 | [Phase 018] 데이터 파이프라인, [Phase 019] 큐레이션 워크플로, [Phase 024] 세일즈 킷 |
| DEC-041 | 2024-06-25 | Exec 선공개 + 증빙 PDF 자동화는 `translation-guardrails.md` 비용 한도를 기준으로 GPU 스케줄/모델을 선정하고, 초과 시 로컬 4bit 모델로 폴백한다. | Guardrail 문서 비용 제약, RSK-041 매트릭스 위치(4×4) | [Phase 011] 알림/콘텐츠 템플릿, [Phase 018] GPU 스케줄러, `docs/strategy/translation-guardrails.md` |
| DEC-042 | 2024-06-25 | 프리미엄 구독에서도 원문 CTA·저자 표기를 유지하고 NPS 조사(Phase 012)로 무료 사용자의 체감 품질을 모니터링한다. | RSK-043 영향분석, Phase 008 워크숍 피드백 | [Phase 011] 템플릿, [Phase 012] NPS 리서치, Issue Tracker `#ISS-233` |

## 대응 전략 & Phase 태그
- **[Phase 018] 증빙 거버넌스**: KPI 매핑 필드와 로그 QA 체크리스트를 데이터 스키마 문서에 반영하고, GPU/Guardrail 지표를 주 단위 보고서에 포함한다.
- **[Phase 019] 세일즈 실행 핸드오버**: 큐레이터 태깅 워크플로에 KPI ID를 노출하고, Sales Enablement 검증을 위한 샘플 리포트를 동기화한다.
- **[Phase 024] 파트너 커뮤니케이션**: 미리보기 리포트와 증빙 패키지를 파트너 온보딩 플로우에 추가하여 딜 중단 리스크(RSK-042)를 완화한다.
- **[Phase 011]/[Phase 012] 고객 신뢰 가드레일**: 알림 템플릿과 NPS 조사 설계를 통해 무료 사용자 영향도를 상시 측정하고 Issue Tracker `#ISS-233`과 연동한다.
