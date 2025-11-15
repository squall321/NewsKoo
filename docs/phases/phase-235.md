# Phase 235 - 현지화, 접근성, 규정 준수

## Objective
다양한 언어·문화·장애 환경에서도 사용 가능한 경험을 제공하고 규정을 준수한다. 이번 페이즈는 **키보드 내비게이션 강화**에 중점을 둔다.

## Tasks
1. 키보드 내비게이션 기준을 정의하고 테스트한다.
2. 전담 체크리스트를 만들어 배포 프로세스에 포함한다.
3. 법무·정책 팀과 리뷰를 진행한다.

## Deliverables
- 현지화/접근성 가이드
- 규정 준수 평가 보고

## Success Metrics
- 접근성 문제 해결률 100%
- 키보드 내비게이션 관련 사용자 신고 0건

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-235/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

