# Phase 036 - 아키텍처 및 기술 스택 설계

## Objective
프론트엔드, 백엔드, 크롤러, 번역 파이프라인을 아우르는 일관된 기술 구조를 정의한다. 이번 페이즈는 **스토리지 옵션 심화**에 중점을 둔다.

## Tasks
1. 스토리지 옵션를 반영한 다이어그램을 그리고 근거를 설명한다.
2. 성능, 비용, 운영성을 비교하여 기술 선택을 명시한다.
3. PoC 항목을 정의하고 성공 기준을 기록한다.

## Deliverables
- 아키텍처 데크와 다이어그램
- 기술 의사결정 레코드(ADR)

## Success Metrics
- ADR 승인 리드타임 3일 이내
- 핵심 스토리지 옵션 리스크가 모두 대응 전략을 가진다

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-036/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

