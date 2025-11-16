# Phase 013 Evidence Archive

Phase 013 리서치 원본과 가공 데이터를 저장하는 표준 경로다. 모든 산출물은 아래 규칙을 따라야 후속 페이즈가 자동으로 연동된다.

## 파일 구조
- `surveys/` — WS-013A 정량 패널 설문 문항, 응답 CSV, 요약 스크립트
- `interviews/` — WS-013B 인터뷰 가이드, 녹취 요약, 톤/로그 태그
- `benchmarks/` — WS-013C 경쟁 서비스 비교 표, 링크 스냅샷
- `cost-model/` — WS-013D 추론 시간 로그, GPU/전력 계산 시트
- `trust-signals/` — WS-013E 증빙 패키지 필수 필드, KPI 샘플

필요 시 세부 하위 디렉터리를 추가할 수 있으나, 상기 5개 최상위 폴더명은 변경하지 않는다.

## 버전 및 포맷 가이드
1. **머신 리더블 우선**: 모든 핵심 수치는 `*-metrics-phase-013.yaml` 또는 `.json` 으로 저장하고, 동일 내용을 PDF/이미지로 중복 저장할 때는 README에 링크한다.
2. **가드레일 태그**: translation-guardrails 준수 여부를 `guardrails:` 키에 `cost`, `copyright`, `model` 플래그로 표시한다.
3. **Issue 레퍼런스**: 파일 헤더(Front Matter)에 `issues: ["#ISS-33x", ...]` 형식으로 연결된 태스크를 명시한다.
4. **타임스탬프**: `2024-07-18T13:00Z` 처럼 UTC ISO8601 형식을 사용한다.

## 승인 흐름
- 초안은 `draft/` 접미사 폴더를 임시로 사용할 수 있으나, 워크숍 승인 후 24시간 내 `surveys/` 등 정규 경로로 이동해야 한다.
- 승인본에는 의사결정 번호(예: `DEC-051`)를 Front Matter 또는 YAML 필드로 기록한다.
- 민감 데이터(개인 식별 등)는 Issue Tracker에서 익명화 여부를 확인한 뒤 저장한다.

## 향후 페이즈와의 연동
- Phase 018 Telemetry 훅은 `cost-model/`과 `trust-signals/` 내 YAML 스키마를 파싱해 자동으로 필드 검증을 수행한다.
- Phase 019 큐레이션 워크플로는 `surveys/`/`interviews/` 내 ARPU, 톤 편향 지표를 그대로 사용하므로 수치 변경 시 의사결정 로그 업데이트가 필요하다.
- Phase 024 세일즈 Enablement는 `benchmarks/`/`trust-signals/` 산출물을 KPI 패키지로 재사용하므로, 라벨/단위 변경 시 README를 동기화한다.
