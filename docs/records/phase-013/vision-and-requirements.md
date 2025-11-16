# Phase 013 — Market Research & Positioning Brief

## Executive Summary
Phase 013는 Phase 001~012에서 확정된 번역 가드레일·카테고리 전략·페르소나 가설을 토대로 **시장 조사 정교화**를 수행하는 시작점이다.
이번 페이즈에서는 (1) TAM/SOM 재산정, (2) 경쟁 포지셔닝, (3) 구매 동기별 콘텐츠/수익 접점, (4) AI/번역 비용 구조, (5) 파트너 신뢰 지표를
동시에 정리해 Phase 018, 019, 024, 040 등 후속 백로그가 의존할 입력을 제공한다. 모든 활동은 `docs/strategy/translation-guardrails.md`
의 저비용·로컬 AI 우선 원칙과 Reddit/9GAG 재작성 규정을 그대로 상속한다.

## Research Objectives & Guiding Questions
1. **시장 용량 재산정** — Ops/Product/Exec 3대 카테고리에서 월간 직무 독자(TAM)와 구독 의향(SOM)을 어떻게 업데이트할 것인가?
2. **경쟁 포지셔닝** — Phase 004 경쟁사 8곳과 비교해 투명성 배지·증빙 로그·밈 톤 조합이 차별화되는 영역은 어디인가?
3. **구매 동기 & 수익 경로** — Phase 008 HYP-008A/B/C에서 정의한 수익 가설을 어떤 고객 세그먼트와 결합해야 ARPU가 극대화되는가?
4. **AI/번역 비용 구조** — 로컬 7B~8B 모델과 QLoRA/4bit 추론 시 GPU·인력 비용을 어떤 범위로 예측해야 Phase 018 Telemetry가 맞춰지는가?
5. **신뢰/리스크 시그널** — 파트너/독자가 확인하고자 하는 투명성 로그, 출처 배지, 민감 태깅 KPI는 무엇이며 어떤 빈도로 노출해야 하는가?
6. **콘텐츠/채널 믹스** — 카드형/스트림형·알림/웹·SNS 재배포 등 채널별 성과를 어떻게 측정하고 실험에 배정할 것인가?

## Workstreams & Evidence Backlog
| Workstream | 설명 | 주요 입력 | 산출 | 담당 |
| --- | --- | --- | --- | --- |
| WS-013A — 정량 패널 | 모바일 우선 설문(모집 N=400)을 재가동해 TAM/SOM, 카드형/스트림형 선호, 지불 의향을 업데이트한다. | Phase 003 설문 문항, Phase 011 템플릿 KPI, NPS(#ISS-233) | KPI 보정치, Persona별 ARPU 추정 | Growth Research |
| WS-013B — 정성 인터뷰 | Ops 큐레이터·프리랜스 에디터·스폰서 12명을 인터뷰해 번역체·증빙 로그·가드레일 체감도를 검증한다. | Phase 002/003 인터뷰 가이드, Phase 012 워크숍 메모 | 인용록, 톤/로그/비용 요구사항 | Product Ops |
| WS-013C — 경쟁 리포트 | Phase 004 벤치마크 + 2024 Q3 신규 3개 서비스를 비교해 가드레일·수익 모델 사례를 수집한다. | Phase 004 비교표, HYP-008A/B/C | 업데이트된 경쟁 매트릭스, 차별화 메세지 초안 | Strategy |
| WS-013D — 비용 시뮬레이션 | 16GB RTX 5070 Ti 기준 추론 시간·전력비를 측정하고 상용 API 대비 절감율을 문서화한다. | translation-guardrails, Phase 009 DEC-041 | 비용·리스크 표, Telemetry 요구사항 | Infra |
| WS-013E — 리스크/신뢰 로그 | 파트너가 요구하는 증빙 패키지와 노출 빈도를 조사해 Phase 018 로그 스키마 필수 필드를 정의한다. | Phase 012 페르소나 표, Phase 018 backlog | KPI/로그 필드 정의, Issue 태깅 | Product Ops + Data |

## Milestones & Issue Tracker Mapping
| 마일스톤 | 일정 | 설명 | 연결 이슈 |
| --- | --- | --- | --- |
| 패널 리쿠르팅 완료 | 2024-07-17 | WS-013A 패널 400명 모집 및 사전 검증, Guardrail 체크리스트 포함 | `#ISS-330`, `#ISS-331` |
| 인터뷰/벤치마크 1차 정리 | 2024-07-19 | WS-013B/C 초안과 증빙 스냅샷을 Repo 우선 저장 | `#ISS-332` |
| 비용·신뢰 로그 시뮬레이션 | 2024-07-20 | WS-013D/E 스크립트 실행, YAML 스키마(`cost-model-metrics-phase-013.yaml`) 제출 | `#ISS-333` |
| 정합성 리뷰 & 워크숍 | 2024-07-22 | 전 스트림 결과물 검수, 의사결정/리스크 로그 업데이트 | `#ISS-334`, `#ISS-335` |

## Instrumentation & Data Handoff Requirements
- WS-013A/B는 `docs/records/phase-013/evidence/surveys/` 및 `interviews/` 경로에 **머신 리더블 YAML**과 CSV를 동시에 보관하고, `guardrails.cost=true` 여부를 필수로 기록한다.
- WS-013C 경쟁 매트릭스는 Phase 020 스토리텔링과 공유되므로, 각 행에 `story-hook` 태그와 외부 URL의 스냅샷 해시를 남겨 재현 가능성을 보장한다.
- WS-013D 비용 시뮬레이션은 16GB RTX 5070 Ti 환경 로그(전력, 추론 시간, 모델 버전)를 포함한 `cost-model/metrics-phase-013.yaml`을 기본 산출물로 하여 Telemetry 훅이 바로 ingest 할 수 있도록 한다.
- WS-013E KPI/로그 정의는 Phase 018/019/024 담당자가 48시간 내 준수 여부를 회신하도록 Issue 템플릿(`kpi-sync.md`)을 사용하며, 회신 누락 시 자동으로 `RSK-051` 상태를 `심각`으로 승격한다.

## Workshop & Alignment Plan
- **사전 자료 배포**: WS-013A~E 초안은 2024-07-18까지 Notion/Repo에 정리하고, 워크숍 참석자에게 시장 지표·경쟁사 요약을 공유한다.
- **핵심 워크숍**: 2024-07-22(1.5h) 세션에서 Growth/Product/Data/Legal 14명이 합의율 90% 이상을 목표로 질문·가정·비용 표를 검토한다.
- **출력 검증**: 승인된 항목은 `docs/records/phase-013/decision-log.md`와 `risk-register.md`에 즉시 반영하고, Issue Tracker에 WS별 태그를 부여한다.

## Deliverables & Dependencies
- Market Research Brief v0.1(본 문서)
- DEC-048~DEC-050 결정 로그
- RSK-049~RSK-051 리스크 레지스터
- Phase 018 데이터 스키마 요구사항, Phase 019 워크플로 요구사항, Phase 024 세일즈 Enablement 입력
- Milestone/Issue 매핑 표 및 `docs/records/phase-013/evidence/` 폴더 구조
- Telemetry/로그 연동을 위한 YAML/CSV 포맷 가이드

## Guardrails & Documentation
- 모든 조사·기록은 `docs/strategy/translation-guardrails.md`의 저비용·로컬 AI 우선, 상용 번역 API 차단, 원문 30일 보관 정책을 따른다.
- Reddit/9GAG 등 외부 콘텐츠는 요약 및 재작성 후 저작권 준수 여부를 로그에 남기며, 민감 소재는 Phase 011 경고 배지 템플릿을 사용한다.
- 조사 데이터, 인터뷰 녹취, 비용 시뮬레이션 스크립트는 `docs/records/phase-013/` 하위 폴더에 버전별로 저장하고 워크숍 이후에도 동일 경로로 갱신한다.
