# Phase 215 - QA 및 품질 보증

## Objective
자동화 테스트, 수동 검증, 품질 지표를 체계화하여 회귀와 결함을 최소화한다. 이번 페이즈는 **접근성 테스트 강화**에 중점을 둔다.

## Tasks
1. 접근성 테스트를 위한 테스트 케이스를 설계하고 자동화한다.
2. 품질 리포트를 생성하여 추세를 추적한다.
3. 결함 관리 프로세스를 정립한다.

## Deliverables
- 테스트 플레이북
- 품질 지표 대시보드

## Success Metrics
- 테스트 커버리지 90%
- 접근성 테스트 관련 결함의 평균 해결시간 3일 이내

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-215/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

