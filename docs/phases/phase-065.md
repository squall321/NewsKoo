# Phase 065 - 번역 자동화 파이프라인

## Objective
다국어 원문을 자동으로 수집·정제·번역하는 데 필요한 서비스와 알고리즘을 완성한다. 이번 페이즈는 **후편집 기준 고도화**에 중점을 둔다.

## Tasks
1. 후편집 기준을 실험하고 결과를 수치화한다.
2. 번역 큐와 워커 구성을 문서화한다.
3. 검수자 피드백 루프를 시스템에 통합한다.

## Deliverables
- 번역 파이프라인 다이어그램
- 품질 및 비용 리포트

## Success Metrics
- 자동 번역 정확도 85% 이상
- 후편집 기준 적용 후 검수 시간 20% 단축

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-065/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

