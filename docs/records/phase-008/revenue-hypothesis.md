# Phase 008 — Revenue Hypothesis Draft

## Executive Summary
Phase 007의 카테고리 구조와 Phase 003 시장 리서치 데이터를 결합해 **직무 기반 스폰서십 + 투명성 증빙 번들**을 핵심 수익 가설로 설정했다. 직무별 KPI와 출처 투명성을 묶은 패키지가 광고주 신뢰도를 높여 리텐션·재구매율을 견인한다는 전제다.

## Research Inputs & Signals
| 출처 | 주요 시사점 | 수익 기회 연결 |
| --- | --- | --- |
| Phase 007 카테고리 KPI 정렬 | Ops/Product 카테고리가 주당 5회 편성, KPI는 처리량/MAJR 등 운영 지표 중심 | 고빈도 직무 슬롯을 스폰서슬롯으로 묶어 **"운영팀 가속" 패키지** 구성 |
| Phase 003 커뮤니티 설문(512명) | 모바일 카드형 선호 64%, 원문 CTA 신뢰도를 가장 높게 평가 | 카드형 광고도 원문/출처 CTA를 함께 제공하는 **신뢰형 네이티브 광고** 시도 |
| Phase 003 광고 파트너 콜(4곳) | 투명성 API 미리보기 요구, 로그 증빙 없으면 예산 배정 곤란 | Transparency 로그를 샘플 PDF로 먼저 제공하는 **증빙 플랜**으로 진입 장벽 완화 |
| SNS 리스닝 & Exec 인터뷰 | Exec/마케터는 인사이트 카드 묶음에 프리미엄 지불 의향 | Exec Trend Roast/Marketing Meme Board 번들을 **프리미엄 리포트**로 업셀 |

## Revenue Hypotheses
1. **HYP-008A — 직무 스폰서 번들**: Ops Laugh Lab + Product Panic Room을 묶어 주 10회 노출 보장 + KPI 대시보드를 제공하면 CPM이 18%↑. (근거: Ops/PM 세그먼트의 KPI 직접 연결 요구)
2. **HYP-008B — 투명성 증빙 플랜**: Transparency 로그 + 재작성 템플릿을 패키징해 광고 딜 전 단계에서 제공하면 파트너 전환율 12%p↑. (근거: Phase 003 광고주 콜에서 증빙 부재를 최대 리스크로 언급)
3. **HYP-008C — Exec Premium Insights**: Exec Trend Roast + All-hands Catch-up을 48시간 선공개 + 맞춤형 CTA로 제공하는 구독형 상품을 만들면 ARPU가 1.6배. (근거: Exec 세그먼트의 시각 자료 선호와 리포트 요구)

## Pricing & KPI Guardrails
- **모델 선택**: `translation-guardrails.md` 기준에 따라 LLaMA-3-8B 4bit(로컬) 또는 Qwen2-7B 번역 파이프라인만 사용해 콘텐츠 재작성 비용을 통제한다. 상용 API는 법무 승인 없는 호출 금지.
- **출처/저작권**: 모든 스폰서 슬롯은 원문 링크/저자 표기를 포함하며, 광고 크리에이티브도 로컬 재작성 후 검수한다.
- **비용 상한**: GPU 단일 16GB 환경에서 주당 30시간 이내 추론으로 제한, 추가 모델은 Issue Tracker `#ISS-142`에 승인을 남긴다.
- **핵심 KPI**: (i) 스폰서 재구매율 40% 이상, (ii) 증빙 패키지 첨부 시 평균 세일즈 사이클 15일 이내, (iii) Exec 프리미엄 구독 ARPU 15USD 이상.

## Experiment Roadmap
| 실험 | 가설 | 지표 | 일정 | 의존성 |
| --- | --- | --- | --- | --- |
| EX-008-01 | Ops/Product 번들 스폰서가 KPI 태깅 보고서를 요구할 것이다 | 번들 CPM, 보고서 다운로드율 | 7월 1주 | Phase 018 데이터 파이프라인, Issue Tracker `#ISS-188` |
| EX-008-02 | 증빙 플랜을 체험판으로 제공하면 파트너 전환율이 증가한다 | 체험→계약 전환율 | 7월 2주 | Phase 024 파트너 온보딩, Issue Tracker `#ISS-205` |
| EX-008-03 | Exec 선공개 구독이 ARPU를 1.6배 이상 높인다 | ARPU, 푸시 CTR | 7월 3주 | Phase 011 알림/CTA, Issue Tracker `#ISS-219` |

## Next Actions
1. 워크숍 합의안에 따라 HYP-008A/B/C를 우선순위로 확정하고 KPI 정의서를 업데이트.
2. 증빙 플랜을 위한 PDF/CSV 샘플을 Phase 018 로그 파이프라인에서 추출.
3. Exec 프리미엄 구독 실험을 위해 Push 템플릿과 선공개 접근 제어 정책을 설계.
4. 모든 실험 결과는 `docs/strategy/translation-guardrails.md` 준수 여부와 함께 Phase 009 상태 보고에 포함.
