# Phase 010 — Risk Register & Guardrails

Phase 010에서는 콘텐츠 생성 툴과 번역 모델을 동시에 조정하면서 새로운 톤/포맷 가이드가 도입된다. 이에 따라 **모델 선택 오류, guardrail 누락, 톤 일관성 붕괴** 등 신규 리스크를 정의하고 Issue Tracker 연계를 생성했다.

## Impact / Likelihood Scale
| 점수 | 영향도 | 발생도 |
| --- | --- | --- |
| 5 | 브랜드/법무 리스크로 즉시 롤백 | 자동화 단계마다 반복 발생 |
| 4 | 페이즈 목표 지연, 추가 검수 필요 | 주 단위로 발생 가능 |
| 3 | 단일 기능 지연 | 조건부 발생 |
| 2 | 국지적 영향 | 낮음 |
| 1 | 미미 | 매우 낮음 |

## Risk Inventory
| ID | 카테고리 | 설명 | 영향 | 발생 | 점수 | 대응 전략 | 상태 | 구현 이슈 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSK-044 | 톤/포맷 | 신규 Tone Guide가 프롬프트·CMS에 반영되지 않으면 Journey별 메시지가 혼재되어 QA 지연이 발생한다. | 3 | 4 | 12 | Issue `#ISS-311`에서 톤 필드/템플릿 매핑 자동화, Lint 스크립트로 CTA 길이·구조 검증. | 계획 중 | `#ISS-311` |
| RSK-045 | 모델/비용 | 콘텐츠 생성 툴이 상용 API나 13B 초과 모델을 선택하면 6 GPUh/wk guardrail을 초과한다. | 4 | 3 | 12 | Issue `#ISS-314`에서 모델 화이트리스트(7B~13B 로컬, QLoRA/4bit)와 비용 모니터링 훅 추가. 초과 시 로컬 4bit 폴백. | 완화 중 | `#ISS-314` |
| RSK-046 | 투명성 | Trust panel 메타데이터(`source_url`, `model`, `rewriteReason`)가 번역 툴에서 누락되면 파트너/법무 증빙이 무력화된다. | 5 | 2 | 10 | Issue `#ISS-313`을 통해 CMS-프론트 동기화, QA 체크리스트에 필드 누락 감지 로직 추가. | 계획 중 | `#ISS-313` |
| RSK-047 | 금지 패턴 | 자동화된 카피 생성기가 직역/과장형 CTA를 통과시키면 Phase 009 리스크가 재발한다. | 4 | 3 | 12 | Issue `#ISS-312`에 금지 패턴 감지 룰 추가, QA에서 “literal translation” 문자열을 차단. | 계획 중 | `#ISS-312` |

## Guardrail Updates for Tools & Models
1. **모델 허용 목록**: LLM-Llama3-8B-Q4, LLM-NanoTranslate-13B-Q8 등 7B~13B 로컬 모델만 자동화 도구에 노출한다. 새 모델 추가 시 `translation-guardrails.md` 비용 섹션을 근거로 GPU 예산 산정 후 승인해야 한다.
2. **콘텐츠 생성 툴 입력 필수 값**: `source_url`, `original_language`, `rewriteReason`, `model_name`, `cost_ceiling`, `guardrail_notes`. 미입력 시 저장 금지.
3. **자동 검수 룰**: 직역/밈 남용/출처 미기재/과장 CTA 금지 패턴을 파이프라인에서 Regex·LLM 분류로 동시 검증한다.
4. **로그 보존**: 번역/재작성 프롬프트, 모델 파라미터, 검수자 메모를 Phase 018 로그 스키마와 동일 필드명으로 저장한다.

## Impact × Likelihood Matrix
| 영향 \ 발생 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| **5** |  | RSK-046 |  |  |  |
| **4** |  |  | RSK-045 · RSK-047 | RSK-044 |  |
| **3** |  |  |  |  |  |
| **2** |  |  |  |  |  |
| **1** |  |  |  |  |  |

## Follow-up Checklist
- `#ISS-311`: Tone Guide → CMS → 프론트 템플릿 동기화.
- `#ISS-312`: 금지 패턴 룰셋과 QA 봇 업데이트.
- `#ISS-313`: Trust panel 메타데이터 필수값 검증.
- `#ISS-314`: 모델 화이트리스트와 GPU 예산 모니터링 훅.
