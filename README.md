# NewsKoo

NewsKoo는 해외 유머 콘텐츠를 자동으로 수집·번역·검수하여 한국 사용자에게 제공하는 React + Flask 기반 서비스입니다. 운영 비용을 최소화하고, 16GB VRAM RTX 5070 Ti 단일 GPU에서 실행 가능한 오픈소스 AI 번역 모델을 재활용하며, 원문을 그대로 복제하지 않고 서비스만의 톤으로 재구성한다는 원칙을 따릅니다.

## 목표
- 해외 유머 콘텐츠 번역/재작성 파이프라인을 자동화하여 **1시간 이내**에 콘텐츠를 제공한다.
- 프론트엔드/백엔드/인프라 구성을 모듈화해 향후 모바일 앱 및 추가 채널 확장을 쉽게 한다.
- 저작권·약관을 준수하는 번역 가드레일을 문서화하고, 자동 검수 도구와 연동한다.

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
## 기술 스택
| 영역 | 기술 | 비고 |
| --- | --- | --- |
| 프론트엔드 | React 18, Vite, TypeScript | 빠른 개발 경험과 번역 UI 컴포넌트 실험 |
| 백엔드 | Python 3.11, Flask, SQLAlchemy | 콘텐츠 파이프라인 및 API |
| 번역/검수 | 오픈소스 번역 모델 + Guardrail 스크립트 | `docs/strategy/translation-guardrails.md` 참고 |
| 인프라 | Terraform, Docker, GitHub Actions | 최소 비용 환경 자동화 |

## 리포지토리 구조
```
backend/    # Flask API, 번역 파이프라인, Python 의존성
frontend/   # React + Vite 클라이언트, npm 의존성 및 lint 설정
infra/      # IaC, 배포 스크립트, 모니터링/알림 템플릿
docs/       # 장기 로드맵, 번역 전략, 페이즈별 계획
```

## 빠른 시작
### 1. 백엔드 (Flask)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
flask --app backend/app.py run --debug
```

### 2. 프론트엔드 (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

## 문서와 기여 규칙
- 300 Phase 계획: `docs/phases/phase-001.md`부터 `phase-300.md`까지 각 페이즈별 목표, 작업, 산출물, 지표가 정리되어 있습니다.
- 모든 진행 기록은 `docs/records/phase-XXX/` 경로에 보관하며, 번역 가드레일은 `docs/strategy/translation-guardrails.md`를 참고합니다.
- 기여 전에는 [CONTRIBUTING.md](CONTRIBUTING.md)를 확인하고, Lint/Format 설정(`.editorconfig`, `backend/pyproject.toml`, `frontend/.eslintrc.json`, `.prettierrc.json`)을 준수해 주세요.
