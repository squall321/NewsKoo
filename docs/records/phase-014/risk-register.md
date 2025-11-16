# Phase 014 — Risk Register

| ID | Category | Severity | Probability | Description | Mitigation |
| --- | --- | --- | --- | --- | --- |
| RSK-052 | Data Access | High | Medium | SimilarWeb/SensorTower API 할당량 부족으로 10개 이상 경쟁사 데이터를 확보하지 못할 위험. | `#ISS-410`을 통해 얼리 Access Token을 미리 확보하고, 대체 공개 IR 데이터 시트도 병렬 수집한다. |
| RSK-053 | Evaluation Bias | Medium | Medium | 기능/콘텐츠/브랜드/수익 점수 가중치가 팀별 주관으로 왜곡될 가능성. | DEC-052 스케일 정의를 문서화하고, WS-014B 리뷰에 Growth/Product/Data 3개 팀을 모두 참여시켜 교차 검증한다. |
| RSK-054 | Workshop Alignment | High | Low | 2시간 워크숍에서 합의율 90%에 도달하지 못해 시나리오 확정이 지연될 수 있음. | 워크숍 전날 사전 리딩 패킷을 배포하고, Needs-Decision 항목은 즉시 `risk-handshake.md` 템플릿으로 이관해 후속 처리한다. |
| RSK-055 | Legal/Brand Exposure | Medium | Medium | 경쟁사 자료 인용 시 저작권/이용약관 위반 가능성. | WS-014A 수집 단계에서 출처/라이선스를 YAML에 기록하고, 번역/재작성 로그를 `docs/strategy/translation-guardrails.md` 기준으로 검수한다. |
| RSK-056 | Backlog Drift | Medium | High | Phase 015~020 백로그로 연동될 티켓이 제때 생성되지 않아 의존 작업이 지연될 수 있음. | WS-014D에서 D4 워크숍 종료 즉시 `#ISS-416` 상태를 갱신하고, Needs-Decision 태그에는 due date를 기입해 추적한다. |
