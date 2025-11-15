# Phase 190 - DevOps 및 운영 자동화

## Objective
CI/CD, 인프라 프로비저닝, 관측 가능성 체계를 마련해 안정적인 배포를 가능케 한다. 이번 페이즈는 **비용 최적화 정비**에 중점을 둔다.

## Tasks
1. 비용 최적화 구성을 코드로 명문화한다.
2. 배포 실패 시나리오를 테스트하고 복구 절차를 검증한다.
3. 운영 대시보드를 정의하여 팀이 공통 지표를 보도록 한다.

## Deliverables
- IaC 템플릿
- 운영 가이드와 런북

## Success Metrics
- 배포 성공률 99%
- 비용 최적화 관련 인시던트 대응시간 15분 내

## Notes
- 관련 산출물과 회의록은 `docs/records/phase-190/` 경로에 보관한다.
- 다음 페이즈로 이관할 의존성을 Issue Tracker에 태깅한다.

## Cost & Translation Guardrails
- 모든 작업은 `docs/strategy/translation-guardrails.md`에 명시된 **저비용·로컬 AI 우선** 원칙을 따른다.
- 상용 번역 API는 기본적으로 비활성화하며, 필요 시 이번 페이즈 산출물에 비용/위험을 명시하고 책임 승인 후 사용한다.
- 16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face 모델과 QLoRA/양자화 기법을 우선 고려한다.
- Reddit 등 소스 콘텐츠는 핵심만 추출하여 NewsKoo 스타일로 재작성하고, 저작권 및 약관을 준수했음을 검수 로그에 남긴다.

