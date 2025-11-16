# Phase 010 — Decision & Narrative Log

Phase 010 워크숍에서는 React 목업과 번역 파이프라인 가드레일을 동시에 만족하는 내러티브 원칙을 재정의하고, 콘텐츠 자동화 시 금지해야 할 패턴을 명시했다.

| ID | 날짜 | 결정 내용 | 근거 | 영향/의존성 |
| --- | --- | --- | --- | --- |
| DEC-045 | 2024-07-02 | Hero/카드 카피는 “Transparent Confidence · Playful Utility · Guardrail-first Credibility” 3축을 모두 포함해야 한다. | `frontend/src/pages/Home.tsx`의 hero 톤, Phase 073 톤 조정 목표, `translation-guardrails.md` 비용·출처 규정 | Phase 011 Notification 템플릿, Phase 018 로그 스키마, Issue Tracker `#ISS-311` |
| DEC-046 | 2024-07-02 | 직역·밈 남용·출처 미기재·과장 CTA 등 4가지 금지 패턴을 가드레일 스크립트에 추가한다. | README 번역 파이프라인 목표, Phase 009 리스크 RSK-041~043 재발 방지 필요 | Phase 018 Guardrail 체크리스트, Issue Tracker `#ISS-312` |
| DEC-047 | 2024-07-02 | Journey별 메시지 예시는 trust panel 메타데이터(`source_url`, `model`, `rewriteReason`)와 연결된 CMS 필드로 관리한다. | PhaseReadiness 세그먼트 데이터, React 카드 구조, 워크숍 메모 | Backend CMS 모델(Phase 099), Phase 011 Push 템플릿, Issue Tracker `#ISS-313` |

## Narrative Principles
1. **Transparent Confidence** — 출처, 모델명, 재작성 사유를 제목·툴팁·CTA 어디서든 숨기지 않고 드러낸다.
2. **Playful Utility** — 카테고리명·헤드라인에 유머 코드를 유지하되, 부제·excerpt에는 KPI나 작업 시간을 명시한다.
3. **Guardrail-first Credibility** — 모든 메시지에 비용/시간 제한, 저작권 준수 문구, 검수 메모 슬롯을 기본 포함한다.

## Forbidden Patterns
- **직역 또는 원문 재게시**: “raw source dump”, “literal translation”이 감지되면 자동으로 재작성 경로로 폴백한다.
- **출처/모델 미기재**: CTA·badge·푸터 중 하나라도 모델명/출처가 없으면 릴리스 금지.
- **밈·슬랭 남용**: KPI가 빠지고 밈만 남은 문장은 QA에서 차단한다 (5초 이내 설명 불가 시 수정 요구).
- **과장형 CTA**: “무료 영원히”, “실패 0%” 등 검증 불가 표현 금지, 대신 구체적 guardrail 수치를 기재한다.

## Follow-ups
- Issue Tracker `#ISS-311`: 톤 가이드와 KPI/템플릿 매핑 자동화.
- Issue Tracker `#ISS-312`: 금지 패턴 검출 스크립트 업데이트.
- Issue Tracker `#ISS-313`: CMS 필드-Trust panel 메타데이터 싱크.
