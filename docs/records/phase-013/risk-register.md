# Phase 013 — Risk Register

| ID | 카테고리 | 설명 | 영향 | 대응 전략 | 상태 |
| --- | --- | --- | --- | --- | --- |
| RSK-049 | 리서치 품질 | WS-013A 설문과 WS-013B 인터뷰가 다른 세그먼트 샘플을 사용하면 TAM/SOM 추정과 톤 가이드가 불일치할 수 있다. | 시장 규모/수익 추정 오류로 Phase 018~024 우선순위가 왜곡 | 합쳐진 샘플 프레임을 워크숍 전에 교차 검증하고, DEC-048에 따라 정량/정성 짝지어진 결과만 승인 | 계획 중 |
| RSK-050 | 비용/가드레일 | WS-013D 비용 시뮬레이션을 위해 상용 번역 API를 임시로 호출하면 translation-guardrails 위반 및 예산 초과가 발생할 수 있다. | GPU 스케줄/Telemetry 설계 지연, 법무 Escalation | DEC-050 체크리스트 준수, 상용 API 호출이 필요하면 Legal+Infra 공동 승인과 비용 캡을 로그에 기록 | 모니터링 |
| RSK-051 | 파트너 신뢰 | WS-013E에서 정의한 투명성 로그 필수 필드가 Phase 018 스키마에 반영되지 않으면 스폰서 증빙 패키지가 늦춰진다. | 스폰서/광고주 온보딩 지연, 수익 목표 미달 | Phase 018/019/024 담당자가 WS-013E 회신 SLA(48h)를 준수하도록 주간 스탠드업에서 체크하고, 누락 시 Issue Tracker `#ISS-241`에 블로커 기록 | 완화 중 |
| RSK-052 | 일정 | 패널 리쿠르팅 및 인터뷰 보안 동의서 검토가 지연되면 7월 22일 워크숍 일정이 밀려 Phase 018/019 백로그 반영이 늦어진다. | 의존 페이즈 일정 차질, Phase 040 세일즈 준비 지연 | DEC-051 근거로 Repo 업로드를 선행하고, Legal 검토 SLA(24h)를 Issue 템플릿으로 추적 | 계획 중 |
| RSK-053 | 데이터 정합성 | Evidence 폴더 내 YAML/CSV 포맷이 서로 다르면 Phase 018 Telemetry 훅과 Phase 019 자동화 스크립트가 ingest 실패할 수 있다. | 로깅/Telemetry 지연, KPI 검증 실패 | Evidence README 가이드 준수 여부를 리뷰 체크리스트에 추가하고, `metrics-phase-013-schema.json`을 lint 도구로 배포 | 모니터링 |

## Escalation Notes
- WS-013A/B 샘플 편향이 발견되면 Growth Research가 즉시 보완 설문을 발송하고 결과를 DEC-048 개정으로 재승인한다.
- 비용/가드레일 이슈는 Infra가 GPU 스케줄 로그와 함께 Legal에 보고하며, 승인되지 않은 API 호출은 해당 WS를 중단한다.
- 파트너 신뢰 리스크는 Phase 024 세일즈 Enablement 오너가 주간 리뷰에서 KPI 로그 누락 여부를 확인하고, 지연 시 Phase 020 스토리텔링 일정도 조정한다.
