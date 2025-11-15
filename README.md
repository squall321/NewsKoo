# NewsKoo

NewsKoo는 해외 유머 콘텐츠를 자동으로 수집·번역·검수하여 한국 사용자에게 제공하는 React + Flask 기반 서비스입니다. 운영 비용을 최소화하고, 16GB VRAM RTX 5070 Ti 단일 GPU에서 실행 가능한 오픈소스 AI 번역 모델을 재활용하며, 원문을 그대로 복제하지 않고 서비스만의 톤으로 재구성한다는 원칙을 따릅니다.

## 목표
- 해외 유머 콘텐츠 번역/재작성 파이프라인을 자동화하여 **1시간 이내**에 콘텐츠를 제공한다.
- 프론트엔드/백엔드/인프라 구성을 모듈화해 향후 모바일 앱 및 추가 채널 확장을 쉽게 한다.
- 저작권·약관을 준수하는 번역 가드레일을 문서화하고, 자동 검수 도구와 연동한다.

해당 계획을 토대로 프론트엔드, 백엔드, 크롤러, 번역 파이프라인, 모바일 앱, 수익화 전략까지 차례로 구현할 수 있습니다. 비용 절감을 위한 오픈소스 번역 전략과 저작권/약관을 고려한 재작성 가이드는 `docs/strategy/translation-guardrails.md`에서 확인할 수 있습니다.

## Frontend 개발 환경

React + Vite로 구성된 초기 프론트엔드 앱은 `frontend/`에 위치합니다. 프로젝트를 실행하기 전에 아래 단계를 따라 환경을 구성하세요.

1. **환경 변수 설정**
   - 루트 경로의 `.env` 파일에서 `VITE_API_BASE_URL` 값을 원하는 API 엔드포인트로 바꿉니다.
2. **의존성 설치**
   - `cd frontend`
   - `npm install` (네트워크가 제한된 환경이면 자체 레지스트리 또는 캐시를 사용하세요.)
3. **개발 서버 실행**
   - `npm run dev`
   - 브라우저에서 `http://localhost:5173` 접속 후 홈/Articles 목업 페이지를 확인할 수 있습니다.
4. **정적 빌드 & 품질 검사**
   - `npm run build`로 프로덕션 번들을 생성합니다.
   - `npm run lint`로 ESLint + Prettier 규칙을 검증합니다.

앱은 `.env`에 설정된 API 베이스 URL의 `/health` 엔드포인트를 호출해 상태 배너를 표시하므로, 백엔드 헬스 체크 API를 함께 준비하면 더욱 원활하게 연동할 수 있습니다.
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
5. Phase 002에서 정의한 투명성 로그 프로토타입을 확인하려면 `/transparency/logs` 엔드포인트를 호출해 최근 번역/검수 로그 샘플을 받아볼 수 있습니다. 응답에는 모델명, 추론 시간, 검수자, 가드레일 메모가 포함됩니다.
6. Phase 003~007 범위의 시장/가치 제안/카테고리 요구사항은 `/phases/progress`와 `/phases/readiness`로 확인할 수 있습니다. 전자는 페이즈별 구현 상태를, 후자는 세그먼트 토글, KPI 카탈로그, 카테고리 캘린더 등 통합 데이터를 반환합니다.
7. Phase 008 워크숍에서 승인된 수익 가설·번들·실험 일정은 `/revenue/phase-008` 엔드포인트로 노출되며, 응답에는 `translation-guardrails.md` 기준이 명시됩니다.

### 테스트 실행
```bash
python -m unittest backend.tests.test_health
python -m unittest backend.tests.test_transparency
```
## Backend database setup

백엔드 서비스는 PostgreSQL 15를 기본 데이터 저장소로 사용하며, `backend/src/db/models.py`에 정의된 SQLAlchemy 모델을 기준으로 생성됩니다. 애플리케이션이 참조하는 핵심 환경 변수는 다음과 같습니다.

| 환경 변수 | 기본값 | 설명 |
| --- | --- | --- |
| `DB_USER` | `newskoo` | 데이터베이스 사용자명 |
| `DB_PASSWORD` | `newskoo` | 데이터베이스 비밀번호 |
| `DB_HOST` | `localhost` | 접속 호스트명 |
| `DB_PORT` | `5432` | PostgreSQL 포트 |
| `DB_NAME` | `newskoodb` | 데이터베이스 이름 |

`backend/src/db/config.py`와 `backend/src/db/session.py`가 위 환경 변수를 읽어 SQLAlchemy 엔진과 세션을 생성합니다. `backend/migrations/001_initial.py` 스크립트를 실행하면 모든 테이블을 한 번에 생성할 수 있습니다.

## Local docker-compose services

로컬 개발자는 다음 예시 `docker-compose.yml` 조각을 프로젝트 루트에 추가해 데이터베이스를 손쉽게 실행할 수 있습니다.

```yaml
services:
  postgres:
    image: postgres:15-alpine
    container_name: newskoo-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: newskoo
      POSTGRES_PASSWORD: newskoo
      POSTGRES_DB: newskoodb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres-data:
```

컨테이너가 올라오면 `python backend/migrations/001_initial.py` 명령으로 스키마를 초기화하고, 애플리케이션 환경 변수만 맞춰주면 곧바로 CRUD 기능을 테스트할 수 있습니다.
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
