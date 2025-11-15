# Backend

Flask 기반 API와 번역/검수 파이프라인을 구성합니다.

## 로컬 실행
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app.py run --debug
```

## 품질 도구
- `black`: `python -m black .`
- `ruff`: `python -m ruff check .`

API 스펙은 `docs/`에 추가될 예정입니다.

## API 엔드포인트 요약

| 경로 | 설명 |
| --- | --- |
| `GET /health` | 백엔드 기동 상태 확인 |
| `GET /transparency/logs` | Phase 002 투명성 로그 프로토타입 노출 |
| `GET /phases/progress` | Phase 003~007 구현 현황 카드 |
| `GET /phases/readiness` | 세그먼트/카테고리/KPI 스냅샷 |
| `GET /revenue/phase-008` | Phase 008 수익 가설·번들·실험·가드레일 페이로드 |
