# Phase 150 - 모바일 웹·앱 경험

## Objective
모바일 최적화 UI와 향후 React 기반 앱 배포를 위한 기반을 마련한다. 이번 페이즈는 **스토어 자산 최적화**에 중점을 둔다.

## Tasks
1. 스토어 자산 요구사항을 프로토타입과 코드에 반영한다.
2. 실기기 테스트를 통해 레이아웃과 성능을 측정한다.
3. 앱 번들/패키징 전략을 문서화한다.

## Deliverables
- 모바일 스타일 가이드
- 빌드/배포 체크리스트

## Success Metrics
- Lighthouse 모바일 퍼포먼스 90+
- 스토어 자산 관련 이슈 해결 속도 2일 이하

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-150/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

