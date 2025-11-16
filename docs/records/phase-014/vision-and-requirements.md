# Phase 014 — 전략 및 비전 정립 입력 정리

## Phase 014 핵심 요약
| 항목 | Phase 014 원문 근거 요약 |
| --- | --- |
| Objective | 경쟁사·대체재·잠재 진입자를 모두 맵핑해 틈새와 차별화를 명확히 규정하고 비전/핵심 가치표를 업데이트한다. |
| Tasks | 1) 정량/정성 데이터 기반 경쟁 구도 인벤토리, 2) 기능/콘텐츠/브랜드/수익 Scorecard·SWOT·Feature-Value Matrix 작성, 3) 2시간 워크숍으로 전략 시나리오 합의, 4) phase-015~020 백로그·리스크 연동. |
| Deliverables | 경쟁사 Landscape 보고서 및 원본 데이터 시트, Scorecard/SWOT/Matrix 원본, 워크숍 회의록과 합의된 전략 방향 3건 및 후속 백로그 목록. |
| SLA & Success Metrics | 10개 이상 경쟁사 커버 및 4개 축 점수 완비, 워크숍 합의율 90%·액션 아이템 5건 이상, 신규 리스크 5건 이상 레지스터 반영, D1~D5 일정(수집→초안→워크숍→QA)을 준수. |

## Workstreams & Evidence Backlog
각 워크스트림은 Phase 014 Tasks를 직접 구현하며, 증빙은 `docs/records/phase-014/evidence/` 하위 폴더에 저장한다.

### WS-014A — 경쟁 Landscape 인벤토리
- **설명**: SimilarWeb, SensorTower, 공개 IR 데이터, 커뮤니티 피드백을 수집·정규화해 최소 10개 경쟁사/대체재 항목을 정리한다.
- **주요 산출물**: `landscape/competitive-landscape.yaml`, 원본 데이터 시트 스냅샷, 레이블링 로그.
- **의존 이슈**: `#ISS-410` (데이터 소스 접근 권한), `#ISS-411` (AI 요약 도구 튜닝).

### WS-014B — Scorecard & Matrix 제작
- **설명**: 기능/콘텐츠/브랜드/수익 4축 점수화, SWOT, Feature-Value Matrix를 작성하고 아이콘/색상 코드를 정의한다.
- **주요 산출물**: `scorecard/feature-value-scorecard.csv`, Matrix Figma 링크 로그, 시각화 스펙 문서.
- **의존 이슈**: `#ISS-412` (평가 기준 확정), `#ISS-413` (Figma 템플릿 반영).

### WS-014C — 전략 워크숍 & 시나리오 플래닝
- **설명**: PM/콘텐츠/BizDev 2시간 워크숍으로 방어/공격/협력 시나리오 3건을 합의하고 합의율 90% 이상을 목표로 한다.
- **주요 산출물**: `workshop/workshop-minutes.md`, 참석자 피드백 YAML, 액션 아이템 백로그 초안.
- **의존 이슈**: `#ISS-414` (워크숍 일정/참석자 확정), `#ISS-415` (시나리오 템플릿 배포).

### WS-014D — 백로그/리스크 연동 및 전달
- **설명**: phase-015~020에서 사용할 백로그 티켓을 작성하고 신규 리스크 5건 이상을 레지스터에 입력, Guardrail 준수 로그 포함.
- **주요 산출물**: `decision-log.md`, `risk-register.md`, 후속 Phase 이관 메모.
- **의존 이슈**: `#ISS-416` (백로그 동기화), `#ISS-417` (리스크 라벨 기준).

## Handoff & Guardrails
- 모든 산출물은 `docs/strategy/translation-guardrails.md`의 저비용·로컬 AI 우선 원칙을 준수하며, 16GB VRAM RTX 5070 Ti 기준으로 재현 가능해야 한다.
- 워크숍에서 합의되지 않은 항목은 Needs-Decision 태그를 달고 Phase 015로 escalated 된다.
- Competitive 자료는 출처/저작권을 명시하고 인용문 재작성 여부를 로그에 남긴다.
