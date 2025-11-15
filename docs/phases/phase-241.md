# Phase 241 - 커뮤니티 및 참여도 성장

## Objective
콘텐츠 참여, 공유, 피드백 루프를 촉진하여 충성도 높은 커뮤니티를 구축한다. 이번 페이즈는 **댓글 시스템 확장**에 중점을 둔다.

## Tasks
1. 댓글 시스템 기능을 설계하고 MVP를 구현한다.
2. 사용자 테스트와 실험을 통해 반응을 측정한다.
3. 운영 정책과 모더레이션 도구를 마련한다.

## Deliverables
- 커뮤니티 기능 스펙
- 참여 지표 리포트

## Success Metrics
- DAU 대비 참여 액션 40%
- 댓글 시스템 기능 관련 유지율 +10%

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-241/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

