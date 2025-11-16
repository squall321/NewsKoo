export type JourneyMessaging = {
  id: string;
  title: string;
  persona: string;
  situation: string;
  copy: string;
  proofHook: string;
  uiPlacement: string;
  guardrailMemo: string;
};

export const journeyMessagingExamples: JourneyMessaging[] = [
  {
    id: 'journey-a',
    title: 'Journey A — Onboarding “주니어 PM”',
    persona: 'Product generalist',
    situation: '번역체와 맥락 부족으로 회의 준비 시간이 지연됨',
    copy:
      '“Product Panic Room 브리프로 3분 안에 밈과 실험 로그를 정리하세요. [EN] "flag the meme" 히스토리와 LLM-Llama3-8B-Q4 추론 로그를 함께 보냅니다.”',
    proofHook: 'Trust panel에 source_url, guardrail_notes를 자동 노출해 번역 출처 의심을 줄임',
    uiPlacement: 'Home hero CTA “Explore Docs” hover 툴팁, Segment 카드 주니어 PM pains/gains 하단',
    guardrailMemo: '1시간 SLA 강조, 상용 API 호출 0건 명시',
  },
  {
    id: 'journey-b',
    title: 'Journey B — Adoption “운영 큐레이터”',
    persona: 'Content ops',
    situation: '검수 시간과 모델 재실행 부담이 큼',
    copy:
      '“Ops Laugh Lab 체크리스트는 모델 캐시 30일과 자동 재실행 SLA 6초를 보장합니다. "Rewritten for Korean punchlines" 메모와 KPI 태그가 함께 기록됩니다.”',
    proofHook: '카드 footer에 “Model cache mode: auto (6s)”와 badge_states를 노출',
    uiPlacement: '카테고리 카드, Timeline slot hover',
    guardrailMemo: 'GPU 사용량을 Phase 011 스케줄러에 묶어 추론 피크를 분산',
  },
  {
    id: 'journey-c',
    title: 'Journey C — Revenue Stakeholder “광고 파트너”',
    persona: 'Revenue stakeholder',
    situation: '비용·출처 투명성 요구',
    copy:
      '“Exec Trend Roast 프루프 덱은 파트너 위젯과 PDF transparency export를 동시에 제공합니다. LLM-NanoTranslate-13B-Q8 로그와 비용 상한(6 GPUh/wk)을 표기해 계약 리스크를 줄입니다.”',
    proofHook: 'Bundle 카드에 KPI 리포트, pricing model, dependencies를 함께 노출',
    uiPlacement: 'Revenue panel “Bundles & guardrails”',
    guardrailMemo: 'Translation guardrails 링크를 기본 CTA로 노출',
  },
  {
    id: 'journey-d',
    title: 'Journey D — Mobile Reader “모바일 독자”',
    persona: 'On-the-go reader',
    situation: '스크롤과 광고 피로',
    copy:
      '“All-hands Catch-up 카드는 카드형 UX와 원탭 공유만 남기고 광고성 문장을 제거했습니다. Rewrite reason은 "Converted analytics memo into card macro"로 명시해 신뢰도를 유지합니다.”',
    proofHook: 'CTA “Share recap” 설명에 "omni-channel CTA stack snapshot"을 유지',
    uiPlacement: '카드 리스트 및 Push notification onboarding defaults',
    guardrailMemo: 'Push 템플릿에도 원문 링크·저자 표기 유지',
  },
  {
    id: 'journey-e',
    title: 'Journey E — Partner-facing Curator “Marketing Meme Board”',
    persona: 'Brand steward',
    situation: '브랜딩 안전성과 투명성 요구를 동시에 충족해야 함',
    copy:
      '“Marketing Meme Board 템플릿은 투명성 배지 + 원문 CTA를 강제하며, 재작성 사유(rewriteReason)를 툴팁에 노출합니다. KPI catalog에서 해당 메시지의 metric을 바로 확인하세요.”',
    proofHook: 'KPI catalog 섹션과 Value prop experiments 리스트를 한 화면에 배치',
    uiPlacement: 'KPI & value prop snapshot 패널',
    guardrailMemo: 'Issue Tracker #ISS-311에서 템플릿-메트릭 링크 자동화를 추적',
  },
];
