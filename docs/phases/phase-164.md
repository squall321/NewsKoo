# Phase 164 - 수익화 및 분석

## Objective
광고 수익과 사용자 행동 분석을 위한 도구와 실험 프레임워크를 구축한다. 이번 페이즈는 **A/B 실험 구축**에 중점을 둔다.

## Tasks
1. A/B 실험을 구성하고 추적 태그를 검증한다.
2. 지표 정의서를 작성해 이해관계자와 공유한다.
3. 수익화 실험의 가설과 롤아웃 계획을 수립한다.

## Deliverables
- 애널리틱스 대시보드
- 수익화 실험 계획서

## Success Metrics
- 핵심 이벤트 추적 정확도 98%
- A/B 실험 도입 후 CPM 향상 목표 대비 80% 이상

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-164/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

