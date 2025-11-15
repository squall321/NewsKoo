# NewsKoo

NewsKoo는 해외 유머 콘텐츠를 자동으로 수집·번역·검수하여 한국 사용자에게 제공하는 React + Flask 기반 서비스입니다. 운영 비용을 최소화하고, 16GB VRAM의 RTX 5070 Ti 단일 GPU에서 실행 가능한 오픈소스 AI 번역 모델을 재활용하며, 원문을 그대로 복제하지 않고 서비스만의 톤으로 재구성한다는 원칙을 따릅니다.

## 300 Phase 계획 아카이브
- `docs/phases/phase-001.md`부터 `phase-300.md`까지 각 페이즈별 목표, 작업, 산출물, 지표를 상세히 정리했습니다.
- 모든 기록은 추후 진행 상황을 `docs/records/phase-XXX/` 경로에 보관한다는 가이드를 포함합니다.

해당 계획을 토대로 프론트엔드, 백엔드, 크롤러, 번역 파이프라인, 모바일 앱, 수익화 전략까지 차례로 구현할 수 있습니다. 비용 절감을 위한 오픈소스 번역 전략과 저작권/약관을 고려한 재작성 가이드는 `docs/strategy/translation-guardrails.md`에서 확인할 수 있습니다.

## Backend quickstart
1. Python 3.11 이상을 준비하고 가상환경을 생성합니다.
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. 환경 변수를 정의합니다.
   ```bash
   cp .env.example .env
   ```
3. 표준 라이브러리만 사용하므로 별도의 의존성 설치가 필요하지 않습니다.
4. 개발 서버를 실행합니다.
   ```bash
   python -m backend.src.main
   ```

### 테스트 실행
```bash
python -m unittest backend.tests.test_health
```
