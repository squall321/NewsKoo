# Phase 013 — Decision & Dependency Log

| ID | 날짜 | 결정 내용 | 근거 | 영향/의존성 |
| --- | --- | --- | --- | --- |
| DEC-048 | 2024-07-16 | 시장 조사 항목을 WS-013A~E 5개 스트림으로 고정하고, 각 스트림이 최소 1개의 정량 지표와 1개의 정성 인사이트를 동시에 제출하도록 표준화한다. | Phase 003 설문, Phase 012 워크숍 메모, Phase 004 경쟁 표를 교차 검토한 결과 데이터 일관성 문제 발견 | Phase 018 데이터 스키마 요구사항, Phase 019 큐레이션 워크플로 정의, Issue Tracker `#ISS-330~#ISS-334` 태깅 | 
| DEC-049 | 2024-07-16 | 합의율 90% 기준을 충족하기 전까지 시장 포지셔닝 문구/가치 제안 카피를 외부 공개하지 않고 Repo 내 `docs/records/phase-013/`에서만 관리한다. | Phase 011 DEC-045 온보딩 계측, Phase 012 Persona 표에서 발견된 톤 편차, 번역 가드레일 비용 제약 | Phase 020 스토리텔링, Phase 073 카피 가이드, Growth/Brand 채널 배포 일정 | 
| DEC-050 | 2024-07-16 | 모든 조사 결과에 비용·저작권 가드레일 체크리스트(상용 API 금지, 원문 30일 보관, 16GB RTX 5070 Ti 우선)를 첨부하여 승인 절차를 병행한다. | translation-guardrails 문서, DEC-041 GPU 폴백 정책, RSK-041 비용 리스크 재발 우려 | Phase 018 Telemetry 훅, Infra GPU 스케줄러, Legal 승인 로그, Issue Tracker `#ISS-188` 업데이트 |
| DEC-051 | 2024-07-17 | WS-013A~E 산출물은 `docs/records/phase-013/evidence/` 하위 폴더에 YAML/CSV 쌍으로 저장하고, Front Matter에 `issues`·`guardrails`·`decisions` 키를 명시한다. | WS 산출물이 Notion/슬라이드에만 존재해 후속 페이즈 자동화가 막힌 이력, Phase 018 Telemetry 요구 | Phase 018/019/024 백로그 자동 수집, Evidence README 버전 관리, Repo 중심 워크플로 고정 |
| DEC-052 | 2024-07-17 | WS-013A 패널과 WS-013B 인터뷰 샘플은 동일한 세그먼트 라벨(Ops/Product/Exec, Region, Experience)을 사용하고, 혼합 결과만 워크숍에 상정한다. | RSK-049 샘플 편향 위험, Phase 003 설문/Phase 012 인터뷰 비교에서 발견된 라벨 불일치 | Growth Research 샘플 검증 체크리스트, Phase 020 스토리텔링 메시지 정합성, Issue Tracker `#ISS-330`, `#ISS-332` |

## Alignment Notes
- WS별 산출물은 Notion 대신 Repo 우선 저장을 기본으로 하고, 승인된 버전만 사내 위키에 요약한다.
- Phase 018/019/024 담당자는 WS-013E 산출물에서 정의한 KPI/로그 필드를 48시간 내 반영 여부를 회신해야 한다.
- 상용 번역 API나 외부 데이터 구매가 필요할 경우 DEC-050 개정이 필요하며, 승인 없이 비용을 발생시키면 워크숍에 Escalation 한다.
