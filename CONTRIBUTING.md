# Contributing to NewsKoo

감사합니다! 아래 절차를 따라 기여해 주세요.

## 1. 브랜치 전략
- `main`: 배포 가능한 상태.
- `develop`: 주요 기능 통합.
- 기능별 브랜치: `feature/<scope>` 형식 사용.

## 2. 개발 환경 준비
1. README의 빠른 시작 가이드를 따라 백엔드/프론트엔드 의존성을 설치합니다.
2. Python 코드는 `black` + `ruff` (`backend/pyproject.toml`)으로, 프론트엔드는 `eslint` + `prettier` (`frontend/.eslintrc.json`, `.prettierrc.json`)으로 포맷합니다.
3. 커밋 전에는 관련 테스트/빌드 명령(`npm run lint`, `ruff check`, `black --check`)을 실행합니다.

## 3. 이슈와 PR
- 이슈 작성 시 재현 절차, 기대 동작, 실제 동작, 스크린샷/로그를 첨부합니다.
- PR에는 변경 요약, 테스트 결과, 문서 업데이트 여부를 명시합니다.
- 가벼운 문서 수정을 제외하고는 최소 1인 이상의 리뷰를 받아야 합니다.

## 4. 커밋 규칙
- Conventional Commits(`feat:`, `fix:`, `docs:`, `chore:` 등)를 따릅니다.
- 한 커밋에는 하나의 논리적 변경만 포함합니다.

## 5. 코드 리뷰 팁
- 성능/보안/번역 가드레일 영향을 중점적으로 확인합니다.
- TODO/임시 코드는 추적 가능한 이슈 번호를 달아 주세요.
