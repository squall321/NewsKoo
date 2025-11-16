import { PhaseProgress, PhaseReadiness } from '../types/phases';

export const phaseProgressFallback: PhaseProgress[] = [
  {
    identifier: 'phase-003',
    phase: 3,
    title: 'Market Research Synthesis',
    summary:
      'Implements the source trust panel, segment toggles, CTA macro, model cache controls, and transparency export scaffolding.',
    status: 'implemented',
    requirements: ['FR-011', 'FR-012', 'FR-013', 'FR-014', 'FR-015'],
    delivered_capabilities: ['trust_panel', 'segment_toggles', 'cta_macro', 'model_cache_control', 'transparency_exports'],
    api_surface: [
      '/phases/readiness#trust_panel',
      '/phases/readiness#segments',
      '/phases/readiness#model_cache',
      '/phases/readiness#transparency_exports',
    ],
    last_synced_at: '2024-05-20T09:00:00+00:00',
  },
  {
    identifier: 'phase-004',
    phase: 4,
    title: 'Competitive Landscape Brief',
    summary:
      'Adds competitive diff snapshots, the rewrite template library, transparency badges, partner widget samples, and the watch queue.',
    status: 'implemented',
    requirements: ['FR-016', 'FR-017', 'FR-018', 'FR-019', 'FR-020'],
    delivered_capabilities: ['competitor_diff', 'template_library', 'transparency_badges', 'partner_widgets', 'competitor_watch'],
    api_surface: [
      '/phases/readiness#competitor_diff',
      '/phases/readiness#template_library',
      '/phases/readiness#partner_widgets',
      '/phases/readiness#competitor_watch',
    ],
    last_synced_at: '2024-05-20T10:00:00+00:00',
  },
  {
    identifier: 'phase-005',
    phase: 5,
    title: 'Value Proposition Canvas',
    summary:
      'Delivers the rotating message tests, segment-based onboarding defaults, shared CTA stack, partner evidence report, and template recommendations.',
    status: 'implemented',
    requirements: ['FR-021', 'FR-022', 'FR-023', 'FR-024', 'FR-025'],
    delivered_capabilities: ['value_prop_tests', 'segment_onboarding', 'cta_stack', 'partner_reports', 'template_recommendations'],
    api_surface: [
      '/phases/readiness#value_props',
      '/phases/readiness#segments',
      '/phases/readiness#cta_stack',
      '/phases/readiness#partner_reports',
      '/phases/readiness#template_library',
    ],
    last_synced_at: '2024-05-20T11:00:00+00:00',
  },
  {
    identifier: 'phase-006',
    phase: 6,
    title: 'Success Metrics Blueprint',
    summary:
      'Exposes the KPI catalog, live curation batch stream, onboarding event schema, badge quality alerts, and partner report tracker.',
    status: 'implemented',
    requirements: ['FR-026', 'FR-027', 'FR-028', 'FR-029', 'FR-030'],
    delivered_capabilities: ['kpi_catalog', 'curation_stream', 'onboarding_schema', 'badge_alerts', 'report_tracker'],
    api_surface: [
      '/phases/readiness#kpi_catalog',
      '/phases/readiness#curation_stream',
      '/phases/readiness#onboarding_schema',
      '/phases/readiness#badge_alerts',
      '/phases/readiness#partner_reports',
    ],
    last_synced_at: '2024-05-20T12:00:00+00:00',
  },
  {
    identifier: 'phase-007',
    phase: 7,
    title: 'Content Category Architecture',
    summary:
      'Publishes category metadata, weekly production calendars, KPI tagging rules, CTA defaults, and category performance dashboards.',
    status: 'implemented',
    requirements: ['FR-031', 'FR-032', 'FR-033', 'FR-034', 'FR-035'],
    delivered_capabilities: ['category_metadata', 'production_calendar', 'kpi_tagging', 'cta_defaults', 'category_performance'],
    api_surface: [
      '/phases/readiness#categories',
      '/phases/readiness#categories.calendar',
      '/phases/readiness#categories.performance',
    ],
    last_synced_at: '2024-05-20T13:00:00+00:00',
  },
];

export const phaseReadinessFallback: PhaseReadiness = {
  trust_panel: {
    fields: ['source_url', 'language_pair', 'model_name', 'inference_time_ms', 'reviewer', 'status', 'guardrail_notes'],
    cta_macro: {
      label: 'View original',
      description: 'Attach original link and rewrite rationale to every card.',
      footer_copy: 'Rewritten for Korean punchlines per translation guardrails.',
    },
    badge_states: [
      { state: 'approved', label: 'Transparency badge', color: '#34d399' },
      { state: 'needs_review', label: 'Awaiting curator', color: '#fcd34d' },
    ],
  },
  segments: [
    {
      segment: 'Ops 큐레이터',
      persona: '사내 운영',
      pains: ['25분 세션 내 검수 압박', '출처/모델 로그 전환'],
      gains: ['카드·스트림 즉시 비교', '로그·버전 한 화면'],
      toggles: ['Ops Laugh Lab', 'All-hands Catch-up'],
      default_filters: ['Ops Laugh Lab', 'All-hands Catch-up'],
      content_needs:
        '25분 집중 세션 안에 6~8건을 검수할 수 있도록 출처·번역 로그·모델 버전을 한 화면에서 확인하고 카드형/스트림형을 즉시 비교해야 한다.',
      translation_tone:
        '원문 구조를 유지하면서 오류·번역체를 표시해 빠르게 수정할 수 있는 "중립·메모형" 톤과 가드레일 준수 메시지를 자동 주석으로 노출.',
      monetization_hooks: [
        'Phase 019 큐레이션 타이머/우선순위 큐와 연결해 운영 비용 절감 KPI 추적',
        'SLA 준수 로그를 스폰서 패키지 증빙으로 활용',
      ],
      onboarding_defaults: {
        notifications: ['Batch readiness'],
        categories: ['Ops Laugh Lab'],
      },
    },
    {
      segment: '프리랜스 콘텐츠 에디터',
      persona: '외부 편집 파트너',
      pains: ['카테고리 톤 지침 탐색', '법무 메모 누락'],
      gains: ['원문 맥락/법무 메모 동시 확인', '톤 가이드 즉시 적용'],
      toggles: ['Marketing Meme Board', 'Product Panic Room'],
      default_filters: ['Marketing Meme Board', 'Product Panic Room'],
      content_needs:
        '카테고리 6종 톤 가이드를 바로 적용하고 원문 맥락과 법무 메모를 함께 확인해 2차 편집을 마칠 수 있어야 한다.',
      translation_tone:
        '"카테고리별 펀/프로페셔널 믹스"로 한국 독자에게 자연스러운 punchline을 강조하되 원문 CTA/저자 표기를 유지.',
      monetization_hooks: [
        '프리미엄 구독 번들에서 QA 비용 절감 근거 제공',
        'Phase 018 투명성 로그와 연동한 검수 횟수 기반 과금 모델 실험',
      ],
      onboarding_defaults: {
        notifications: ['Editorial wrap'],
        categories: ['Marketing Meme Board'],
      },
    },
    {
      segment: '밈 애호가 독자 (모바일)',
      persona: '커뮤니티 얼리어답터',
      pains: ['출근길 3분 콘텐츠', '민감 소재 노출 걱정'],
      gains: ['카드형 스크롤', '원문 스레드 손쉬운 공유'],
      toggles: ['Marketing Meme Board', 'All-hands Catch-up'],
      default_filters: ['Marketing Meme Board', 'All-hands Catch-up'],
      content_needs:
        '출근길 3분 내에 카드형으로 업계 밈을 소비하고 원문 스레드도 쉽게 찾아 공유할 수 있어야 한다.',
      translation_tone:
        '"구어체·짧은 문장 + 문화적 각색"으로 번역체를 최소화하고 punchline을 한국식으로 재작성, 민감 소재는 경고 배지로 명시.',
      monetization_hooks: [
        '카드형 뷰 하단 광고/추천 슬롯 운영',
        'Phase 090 개인화 알림 CTA 실험(HYP-008A)로 CPM/구독 전환 추적',
      ],
      onboarding_defaults: {
        notifications: ['Push personalization'],
        categories: ['All-hands Catch-up'],
      },
    },
    {
      segment: '주니어 PM/마케터 독자',
      persona: '실행 인사이트 수요자',
      pains: ['근거 기반 사례 부족', '저작권/브랜드 세이프티 우려'],
      gains: ['데이터 포인트 포함 요약', '출처 명확한 적용 팁'],
      toggles: ['Product Panic Room', 'Exec Trend Roast'],
      default_filters: ['Product Panic Room', 'Exec Trend Roast'],
      content_needs:
        '해외 트렌드 요약과 실행 인사이트(데이터 포인트, 참고 링크)가 포함된 스트림형 뷰를 선호하며 브랜드 세이프티나 저작권 논란 없는 사례를 원한다.',
      translation_tone:
        '"프로페셔널·근거 기반" 톤으로 수치/출처를 명확히 언급하고 한국 독자를 위한 적용 팁을 덧붙인다.',
      monetization_hooks: [
        '프리미엄 구독/리포트 업셀 리드 생성',
        'Phase 024 세일즈 Enablement KPI 리포트 샘플·번들 판매(HYP-008B) 연계',
      ],
      onboarding_defaults: {
        notifications: ['AM digest'],
        categories: ['Product Panic Room'],
      },
    },
    {
      segment: '스폰서·광고 파트너',
      persona: 'Revenue stakeholder',
      pains: ['브랜드 세이프티 증빙', '저작권/허가 추적'],
      gains: ['투명성 로그', 'KPI 태깅/감사 체인'],
      toggles: ['Exec Trend Roast', 'Marketing Meme Board'],
      default_filters: ['Exec Trend Roast', 'Marketing Meme Board'],
      content_needs:
        '브랜드 세이프티를 입증할 수 있는 투명성 로그, KPI 태깅, 검수자 감사 체인을 한 번에 확인하고 싶다.',
      translation_tone:
        '"포멀·감사 대응" 톤으로 모델 버전, 가드레일 준수, 민감 주제 필터링 현황을 데이터 중심으로 보고.',
      monetization_hooks: [
        'Transparency API/증빙 패키지(HYP-008B/C) 판매',
        'Phase 018 로그 스키마·Phase 024 온보딩 자료에 KPI/CTA 매핑 포함',
      ],
      onboarding_defaults: {
        notifications: ['Weekly proof'],
        categories: ['Exec Trend Roast'],
      },
    },
  ],
  model_cache: {
    modes: [
      { id: 'auto', label: '자동', description: '모델 추론 6초 SLA 내 자동 재실행', sla_seconds: 6 },
      { id: 'on_demand', label: '온디맨드', description: '큐레이터가 필요 시 재실행', sla_seconds: 15 },
    ],
    cache_window_days: 30,
    default_mode: 'auto',
  },
  transparency_exports: {
    formats: [
      { type: 'csv', fields: ['log_id', 'model', 'reviewer', 'status', 'source_url'] },
      { type: 'pdf', sections: ['executive_summary', 'model_matrix', 'guardrail_notes'] },
    ],
    delivery: { cadence: 'weekly', channels: ['email', 's3'] },
  },
  competitor_diff: {
    categories: [
      {
        category: 'Transparency',
        newskoo: '로그/모델 전면 공개',
        competitors: '출처 미표기 또는 API 비공개',
        highlight: '유일한 투명성 배지',
      },
      {
        category: '템플릿',
        newskoo: '업계별 템플릿 6종',
        competitors: '모범 사례 없음',
        highlight: '큐레이터 처리량 20% 향상',
      },
      {
        category: '파트너 위젯',
        newskoo: '로그 포함 미니 피드',
        competitors: '딥링크 전용',
        highlight: '광고주 파일럿 4곳',
      },
    ],
    update_sla_days: 30,
  },
  template_library: {
    templates: [
      {
        id: 'ops-checklist',
        title: 'Ops Laugh Lab Template',
        segments: ['운영 큐레이터'],
        tone: '체크리스트형 밈',
        macros: ['상황', '맥락', '한국식 punchline'],
      },
      {
        id: 'product-story',
        title: 'Product Panic Narrative',
        segments: ['주니어 PM'],
        tone: '스토리 카드',
        macros: ['문제', '실험', '교훈'],
      },
      {
        id: 'marketing-slide',
        title: 'Marketing Meme Board',
        segments: ['시니어 마케터', '광고 파트너'],
        tone: '슬라이드 카드',
        macros: ['후킹', '성과', 'CTA'],
      },
    ],
    recommendations: {
      inputs: ['segment', 'tone', 'industry'],
      engine: 'rule_based',
    },
  },
  partner_widgets: {
    variants: [
      { id: 'inline', description: '카드 3개 미니 피드', bundle_size: 3 },
      { id: 'story', description: '스토리 하이라이트', bundle_size: 1 },
    ],
    embed_requirements: ['no external trackers', 'load under 1s'],
  },
  competitor_watch: {
    tracked_competitors: 8,
    alerts: [
      { name: 'MemeDigest pricing', status: 'monitoring' },
      { name: 'TLDR Biz mobile update', status: 'investigating' },
    ],
    next_review: '2024-06-15',
  },
  value_props: {
    test_window_days: 14,
    messages: [
      {
        id: 'transparency-first',
        copy: 'Know which model touched every punchline.',
        segments: ['시니어 마케터', '광고 파트너'],
      },
      {
        id: 'industry-memes',
        copy: 'Instantly reuse industry-ready memes with context.',
        segments: ['주니어 PM', '운영 큐레이터'],
      },
      {
        id: 'low-latency',
        copy: 'Local AI costs under 100k KRW/month.',
        segments: ['광고 파트너'],
      },
    ],
  },
  cta_stack: {
    channels: ['카카오', 'Slack', 'Email'],
    badges: ['Transparency', 'Value Prop'],
    defaults: {
      ops: 'Share checklist',
      product: 'Open brief',
      marketing: 'Book partner session',
    },
  },
  partner_reports: {
    formats: ['pdf', 'csv'],
    weekly_reports: 5,
    tracker: [
      { partner: 'Agency A', status: 'sent' },
      { partner: 'Brand B', status: 'scheduled' },
    ],
  },
  kpi_catalog: {
    items: [
      { metric: '월간 활성 직무 독자', type: 'Lagging', target: '50k', source: 'web/app events' },
      { metric: '세그먼트 온보딩 완료율', type: 'Leading', target: '80%', source: 'onboarding events' },
      { metric: '큐레이터 배치당 승인 카드 수', type: 'Leading', target: '10', source: '검수 로그' },
      { metric: '출처 배지 노출률', type: 'Leading', target: '99.5%', source: '퍼블리싱 로그' },
      { metric: '파트너 증빙 리포트 발송 수', type: 'Lagging', target: '30/month', source: '로그 Export' },
    ],
    accuracy_tolerance: '±2%',
    freshness: { leading: '2h', lagging: '24h' },
  },
  curation_stream: {
    last_batch_id: 'BATCH-20240520-01',
    avg_cards_per_batch: 10,
    sla_minutes: 60,
    recent_batches: [
      { id: 'BATCH-20240519-02', cards: 11, badge_coverage: 1 },
      { id: 'BATCH-20240518-01', cards: 9, badge_coverage: 0.98 },
    ],
  },
  onboarding_schema: {
    fields: [
      { name: 'segment', type: 'string', required: true },
      { name: 'seniority', type: 'string', required: true },
      { name: 'channel', type: 'string', required: false },
    ],
    anonymization: 'hash user ids, drop PII',
  },
  badge_alerts: {
    open_alerts: [{ category: 'Marketing Meme Board', coverage: 0.97 }],
    sla_minutes: 120,
    notification_channels: ['Slack', 'Email'],
  },
  categories: {
    metadata: [
      {
        id: 'ops-laugh-lab',
        title: 'Ops Laugh Lab',
        tone: '체크리스트형 밈',
        cadence: '5/week',
        kpi_tags: ['curation_throughput', 'badge_coverage'],
        default_push: '09:00 local',
        default_cta: 'Share to Ops Slack',
      },
      {
        id: 'product-panic-room',
        title: 'Product Panic Room',
        tone: '스토리 카드',
        cadence: '5/week',
        kpi_tags: ['majr', 'session_time'],
        default_push: '11:00 local',
        default_cta: 'Open Product brief',
      },
      {
        id: 'marketing-meme-board',
        title: 'Marketing Meme Board',
        tone: '슬라이드 카드',
        cadence: '4/week',
        kpi_tags: ['share_rate', 'partner_reports'],
        default_push: '13:00 local',
        default_cta: 'Book partner session',
      },
      {
        id: 'dev-standup-satires',
        title: 'Dev Standup Satires',
        tone: '코드 스니펫',
        cadence: '3/week',
        kpi_tags: ['return_rate', 'bug_reports'],
        default_push: '15:00 local',
        default_cta: 'File bug roast',
      },
      {
        id: 'exec-trend-roast',
        title: 'Exec Trend Roast',
        tone: '인포그래픽',
        cadence: '2/week',
        kpi_tags: ['partner_reports', 'revenue'],
        default_push: 'Tuesday 08:00',
        default_cta: 'Download proof deck',
      },
      {
        id: 'all-hands-catch-up',
        title: 'All-hands Catch-up',
        tone: '주간 요약',
        cadence: '1/week',
        kpi_tags: ['onboarding_completion', 'push_ctr'],
        default_push: 'Friday 17:00',
        default_cta: 'Share recap',
      },
    ],
    calendar: [
      { day: 'Mon', slots: 3, focus: ['Ops Laugh Lab', 'Product Panic Room'] },
      { day: 'Tue', slots: 3, focus: ['Marketing Meme Board', 'Exec Trend Roast'] },
      { day: 'Wed', slots: 3, focus: ['Dev Standup Satires', 'Ops Laugh Lab'] },
      { day: 'Thu', slots: 3, focus: ['Product Panic Room', 'Marketing Meme Board'] },
      { day: 'Fri', slots: 2, focus: ['All-hands Catch-up'] },
    ],
    performance: {
      'ops-laugh-lab': { leading: '11 cards/batch', lagging: '+8% ops CTR' },
      'product-panic-room': { leading: '48s avg dwell', lagging: '+6% MAJR' },
      'marketing-meme-board': { leading: '34% share rate', lagging: '+2 partner proofs' },
      'dev-standup-satires': { leading: '3 bug CTA/day', lagging: '+5% dev return' },
      'exec-trend-roast': { leading: '2 reports/week', lagging: '+1 enterprise lead' },
      'all-hands-catch-up': { leading: '82% push CTR', lagging: '+4% onboarding' },
    },
  },
};
