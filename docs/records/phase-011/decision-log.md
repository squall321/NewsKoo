# Phase 011 — Decision & Dependency Log

Phase 011 워크숍에서는 HYP-008 수익 가설, KPI 트리, translation guardrails 문서를 교차 검토하여 **요구사항 우선순위와 구현 순서**를 확정했다. 우선순위는 Must/Should/Could 체계를 사용했으며, 각 항목은 다음 페이즈 의존성과 담당 조직을 명시했다.

| ID | 날짜 | 결정 내용 | 근거/데이터 | 우선순위·의존성 | 담당 조직 |
| --- | --- | --- | --- | --- | --- |
| DEC-043 | 2024-07-02 | FR-041을 Must로 지정하고 Phase 090 알림 스택과 동시 설계한다. Exec 선공개와 무료 사용자 카피를 같은 템플릿 엔진에서 관리해 Push CTR과 ARPU를 동시에 측정. | Phase 003 모바일 선호도, Phase 007 템플릿 가이드, Phase 008 EX-008-03, RSK-043 고객 신뢰 시나리오. | Must. Phase 007 콘텐츠 프레임워크, Phase 090 알림 전략, Issue `#ISS-311`. | Product (소유), Platform (구현) |
| DEC-044 | 2024-07-02 | FR-042 KPI 증빙 패널을 Must로 고정하고 Phase 018/019 파이프라인에 선행 의존성을 둔다. QA 체크리스트·카테고리 태그를 자동으로 붙여 스폰서 재구매율 KPI를 실시간 검증. | HYP-008A/B KPI 정의, DEC-040 QA 요구, RSK-040/042 영향 분석. | Must. Phase 018 로그 스키마, Phase 019 큐레이션 워크플로, Issue `#ISS-312`. | Product Ops (소유), Data (구현) |
| DEC-045 | 2024-07-02 | FR-043 직무 온보딩 계측을 Must로 설정하고 KPI 카탈로그(YAML)를 싱글 소스로 사용한다. 온보딩 폼에서 직무/세그먼트 수집 실패 시 게시 파이프라인을 차단한다. | DEC-026 North Star, DEC-023 직무 필수 단계, KPI 트리 정확도(NFR-017) 요구. | Must. Phase 006 KPI 관리, Phase 021 마케팅 퍼널, Issue `#ISS-313`. | Growth (소유), Product Ops (지원) |
| DEC-046 | 2024-07-02 | FR-045 및 NFR-025~NFR-027을 Guardrail로 지정하고 Phase 018 Telemetry 훅을 선행 조건으로 명문화한다. GPU 비용·템플릿 QA 로그가 없으면 Exec 선공개 실험을 배포하지 않는다. | RSK-041 비용 리스크, translation guardrails 비용 상한, DEC-041 GPU 폴백 정책. | Should. Phase 018 Telemetry, Infra GPU 스케줄러, QA 체크리스트, Issue `#ISS-315-#ISS-318`. | Infra (소유), Product Ops (검증) |

## Dependency Threads
- **Phase 018/019 연동**: KPI 증빙 패널, Guardrail Telemetry는 Phase 018 데이터 스키마 확정 전에 스펙이 잠겨야 하므로 2주 내 리뷰 세션을 예약한다.
- **Phase 012 실험 대기**: Exec 선공개 범위는 Phase 012 NPS/실험 결과 승인 후 확정되며, 결과가 지연되면 FR-041의 무료 사용자 카피를 기본으로 배포한다.
- **Translation Guardrails**: NFR-025~028 준수 여부는 translation guardrails 체크리스트에 추가 필드를 만들어 승인 시 첨부한다.
