# Phase 121 - 콘텐츠 편집 및 검수 UX

## Objective
검수자가 자동 번역본을 빠르게 확인·수정·게시할 수 있는 워크스페이스를 설계한다. 이번 페이즈는 **리스트 필터 설계**에 중점을 둔다.

## Tasks
1. 리스트 필터 시나리오를 와이어프레임과 사용자 흐름으로 표현한다.
2. 프로토타입을 제작해 내부 유저 테스트를 진행한다.
3. 피드백을 정리해 디자인 시스템에 반영한다.

## Deliverables
- UX 스펙 문서
- 프로토타입 링크 및 테스트 결과

## Success Metrics
- 검수 단계별 클릭 수 20% 감소
- 리스트 필터 과업 만족도 4/5 이상

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-121/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

