# Phase 102 - 프론트엔드 인프라 및 디자인 시스템

## Objective
React+Vite 기반 코드베이스와 공용 UI 패턴을 구축하여 일관된 UX를 제공한다. 이번 페이즈는 **라우팅 정비**에 중점을 둔다.

## Tasks
1. 라우팅을 반영한 보일러플레이트를 작성한다.
2. 스토리북/디자인 토큰을 연결한다.
3. CI에서의 빌드 및 린트 파이프라인을 보강한다.

## Deliverables
- 프론트엔드 컨벤션 가이드
- 컴포넌트 카탈로그

## Success Metrics
- 번들 사이즈 베이스라인 수립
- 라우팅 관련 회귀 버그 0건 유지

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-102/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

