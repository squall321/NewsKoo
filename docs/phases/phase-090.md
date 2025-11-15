# Phase 090 - 백엔드 API 및 데이터 계층

## Objective
콘텐츠·번역·검수 데이터를 관리하는 Flask 기반 백엔드와 DB 스키마를 완성한다. 이번 페이즈는 **테스트 커버리지 구현**에 중점을 둔다.

## Tasks
1. 테스트 커버리지를 위한 API 명세를 세부 설계하고 테스트 코드를 작성한다.
2. ORM 모델과 마이그레이션을 추가한다.
3. 관찰 가능한 로깅/메트릭 포인트를 노출한다.

## Deliverables
- OpenAPI 스펙 업데이트
- 데이터베이스 마이그레이션 스크립트

## Success Metrics
- 엔드포인트 응답시간 p95 300ms 이하
- 테스트 커버리지 관련 테스트 커버리지 85% 이상

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-090/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

