# Phase 010 — Vision & Requirements

Phase 010은 React 목업(`frontend/src/pages/Home.tsx`)에서 확인한 톤앤매너와 번역 파이프라인 요구사항(`README.md`, `docs/strategy/translation-guardrails.md`, `docs/phases/phase-073.md`)을 교차 검토해 향후 자동화/콘텐츠 생산 툴킷에 적용할 음성·형식 가이드와 사용자 여정별 메시지 예시를 정의한다.

## Tone & Format Guide (Draft)
### 입력 근거
- **Hero & 카드 카피**: “Curate tomorrow's headlines”, “Book a Demo”, “Spotlight a category…” 등은 플레이풀하지만 증빙과 투명성 메시지를 반복한다. (`frontend/src/pages/Home.tsx`)
- **데이터 세그먼트**: `phaseReadiness` 페이로드는 세그먼트 pains/gains, KPI, 카테고리 톤, CTA 매크로 등을 이미 구조화했다. (`frontend/src/data/phaseReadiness.ts`)
- **Guardrail 요구사항**: 16GB VRAM 환경, 로컬 7B~13B 모델 우선, 1시간 내 제공, 원문 재작성, 메타데이터 보존이 필수다. (`README.md`, `docs/strategy/translation-guardrails.md`, `docs/phases/phase-073.md`)

### 톤 기둥
| Pillar | 설명 | 적용 패턴 |
| --- | --- | --- |
| **Transparent Confidence** | 원문 출처·모델·가드레일을 숨기지 않고 강조한다. | CTA/배너에서 “View original”, “Model: LLM-Llama3-8B-Q4” 같이 모델명을 노출하고, 번역/재작성 이유를 1문장으로 요약한다. |
| **Playful Utility** | “Ops Laugh Lab”, “Marketing Meme Board”처럼 위트를 섞되 기능적 이득을 붙인다. | 제목은 위트, 부제는 KPI 또는 작업 시간 절감을 언급한다. |
| **Guardrail-first Credibility** | 비용/시간/출처 제한을 사전에 명시해 법무·파트너 우려를 줄인다. | 카드 하단이나 툴팁에서 “Rewritten for Korean punchlines per translation guardrails.”처럼 면책 문구를 표준화한다. |

### 형식 규칙
1. **문단 구조**: 제목 → 1문장 효익 → 신뢰/모델 정보 → CTA 순으로 고정해 카드형 UX와 정렬한다.
2. **CTA Copy**: 기본은 동사 + 명사 2~3어절(예: “Share checklist”). 동일 CTA의 설명 푸터에는 구체적 증빙(“badge + source metadata”)을 넣는다.
3. **가드레일 표기**: 모든 메시지에 `source_url`, `model_name`, `rewriteReason`를 한글로 재작성하여 검수자가 복사해 넣을 수 있게 한다.
4. **다국어 처리**: 원문 키워드 인용 시 따옴표와 원문 언어 태그(예: `[EN] “punchline commits”`)를 붙여 로컬 번역 모델이 후속 재번역할 때 컨텍스트를 확보한다.
5. **시간/비용 한정 표시**: GPU 사용 예산(주 6 GPU 시간) 또는 1시간 SLA 같은 제한을 각 섹션 푸터에 “Guardrail: 1h SLA · 6 GPUh/wk” 형태로 기재한다.

### 번역 파이프라인 정렬
| 단계 | 요구사항 | 콘텐츠 가이드 영향 |
| --- | --- | --- |
| 크롤링·정규화 | 허용된 소스, Robots, 민감정보 제거 | 메시지 초안에 "redacted", "context rebuilt" 같은 표현을 추가해 재작성 여부를 명시 |
| 로컬 번역 | 7B~13B 모델, 4bit/QLoRA, 상용 API 최소화 | 카피 예시에도 모델/양자화 표기를 남겨 프롬프트 가드레일로 재사용 |
| 스타일 재작성 | NewsKoo 템플릿, 플레이풀 톤 | 템플릿마다 톤 키워드(예: `tone=playful+operational`)를 표기해 프롬프트에서 재활용 |
| 인간 검수 | 문화 민감성, 저작권 확인 | 메시지 예시에 검수 체크리스트 슬롯(“검수 메모: ____”)을 포함 |
| 기록 보관 | 모델/프롬프트/수정 내역 보존 | 각 예시에 Log ID placeholder를 추가, 자동화 툴이 채울 수 있게 함 |

## User Journey Messaging Examples
세그먼트 pains/gains와 React 카드 톤을 재작성해 여정별 메시지 예시를 정의했다. 모든 카피는 Guardrail 표준 문구와 함께 제공된다.

### Journey A — Onboarding “주니어 PM”
- **상황**: 번역체와 맥락 부족으로 회의 준비 시간이 지연됨.
- **Copy 예시 (KR)**: “Product Panic Room 브리프로 3분 안에 밈과 실험 로그를 정리하세요. [EN] "flag the meme" 히스토리와 LLM-Llama3-8B-Q4 추론 로그를 함께 보냅니다.”
- **Proof hook**: Trust panel에 `source_url`, `guardrail_notes`를 자동 노출해 번역 출처 의심을 줄인다.
- **UI 위치**: Home hero CTA “Explore Docs” hover 툴팁, Segment 카드 `주니어 PM` pains/gains 하단.
- **Guardrail 메모**: 1시간 SLA 강조, 상용 API 호출 0건 명시.

### Journey B — Adoption “운영 큐레이터”
- **상황**: 검수 시간·모델 재실행 부담이 큼.
- **Copy 예시 (KR)**: “Ops Laugh Lab 체크리스트는 모델 캐시 30일과 자동 재실행 SLA 6초를 보장합니다. "Rewritten for Korean punchlines" 메모와 KPI 태그가 함께 기록됩니다.”
- **Proof hook**: 카드 footer에 “Model cache mode: auto (6s)”와 `badge_states`를 노출.
- **UI 위치**: 카테고리 카드, Timeline slot hover.
- **Guardrail 메모**: GPU 사용량을 Phase 011 스케줄러에 묶어 추론 피크를 분산.

### Journey C — Revenue Stakeholder “광고 파트너”
- **상황**: 비용·출처 투명성 요구.
- **Copy 예시 (KR)**: “Exec Trend Roast 프루프 덱은 파트너 위젯과 PDF transparency export를 동시에 제공합니다. LLM-NanoTranslate-13B-Q8 로그와 비용 상한(6 GPUh/wk)을 표기해 계약 리스크를 줄입니다.”
- **Proof hook**: Bundle 카드에 KPI 리포트, pricing model, dependencies를 함께 노출.
- **UI 위치**: Revenue panel "Bundles & guardrails".
- **Guardrail 메모**: Translation guardrails 링크를 기본 CTA로 노출.

### Journey D — Mobile Reader “모바일 독자”
- **상황**: 스크롤·광고 피로.
- **Copy 예시 (KR)**: “All-hands Catch-up 카드는 카드형 UX와 원탭 공유만 남기고 광고성 문장을 제거했습니다. Rewrite reason은 'Converted analytics memo into card macro'로 명시해 신뢰도를 유지합니다.”
- **Proof hook**: CTA `Share recap` 설명에 "omni-channel CTA stack snapshot"을 유지.
- **UI 위치**: 카드 리스트 및 Push notification onboarding defaults.
- **Guardrail 메모**: Push 템플릿에도 원문 링크·저자 표기 유지.

### Journey E — Partner-facing Curator “Marketing Meme Board”
- **상황**: 브랜딩 안전성과 투명성 요구를 동시에 충족해야 함.
- **Copy 예시 (KR)**: “Marketing Meme Board 템플릿은 투명성 배지 + 원문 CTA를 강제하며, 재작성 사유(`rewriteReason`)를 툴팁에 노출합니다. KPI catalog에서 해당 메시지의 metric을 바로 확인하세요.”
- **Proof hook**: KPI catalog 섹션과 Value prop experiments 리스트를 한 화면에 배치해 실험 맥락을 준다.
- **UI 위치**: KPI & value prop snapshot 패널.
- **Guardrail 메모**: Issue Tracker `#ISS-311`에서 템플릿-메트릭 링크 자동화를 추적.

## Next Steps
1. 톤/포맷 가이드를 프롬프트 템플릿(`translation guardrails` 참조)과 CMS 필드 스키마에 적용한다.
2. Journey별 메시지를 Notification/CTA 매핑 테이블에 싱크하고, 테스트 시나리오를 QA 체크리스트에 추가한다.
3. Guardrail 메타데이터(`model`, `rewriteReason`, `cost ceiling`)는 번역 툴과 프런트 목업 양쪽에서 동일 명칭으로 유지한다.
