# NewsKoo

NewsKoo는 해외 유머 콘텐츠를 자동으로 수집·번역·검수하여 한국 사용자에게 제공하는 React + Flask 기반 서비스입니다. 운영 비용을 최소화하고, 16GB VRAM의 RTX 5070 Ti 단일 GPU에서 실행 가능한 오픈소스 AI 번역 모델을 재활용하며, 원문을 그대로 복제하지 않고 서비스만의 톤으로 재구성한다는 원칙을 따릅니다.

## 300 Phase 계획 아카이브
- `docs/phases/phase-001.md`부터 `phase-300.md`까지 각 페이즈별 목표, 작업, 산출물, 지표를 상세히 정리했습니다.
- 모든 기록은 추후 진행 상황을 `docs/records/phase-XXX/` 경로에 보관한다는 가이드를 포함합니다.

해당 계획을 토대로 프론트엔드, 백엔드, 크롤러, 번역 파이프라인, 모바일 앱, 수익화 전략까지 차례로 구현할 수 있습니다. 비용 절감을 위한 오픈소스 번역 전략과 저작권/약관을 고려한 재작성 가이드는 `docs/strategy/translation-guardrails.md`에서 확인할 수 있습니다.

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
