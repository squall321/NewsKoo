# Phase 043 - 데이터 수집 및 크롤링 기초

## Objective
신뢰성 있는 크롤링 인프라와 데이터 파이프라인을 준비하여 지속적인 컨텐츠 공급을 가능케 한다. 이번 페이즈는 **우회 전략 설계**에 중점을 둔다.

## Tasks
1. 우회 전략을(를) 문서화하고 구현 가이드를 만든다.
2. 테스트 크롤을 실행해 수집 품질을 평가한다.
3. 법적/윤리적 가이드를 다시 검토하고 체크리스트를 갱신한다.

## Deliverables
- 크롤링 전략 문서
- 샘플 데이터셋과 품질 보고서

## Success Metrics
- 수집 성공률 95% 이상
- 우회 전략 관련 이슈 대응 SLA 1일 이내

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-043/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

