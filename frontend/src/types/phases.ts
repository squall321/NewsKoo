export type PhaseProgress = {
  identifier: string;
  phase: number;
  title: string;
  summary: string;
  status: 'implemented' | 'in-flight';
  requirements: string[];
  delivered_capabilities: string[];
  api_surface: string[];
  last_synced_at: string;
};

export type SegmentProfile = {
  segment: string;
  persona: string;
  pains: string[];
  gains: string[];
  toggles: string[];
  default_filters: string[];
  content_needs: string;
  translation_tone: string;
  monetization_hooks: string[];
  onboarding_defaults: {
    notifications: string[];
    categories: string[];
  };
};

export type CategoryMetadata = {
  id: string;
  title: string;
  tone: string;
  cadence: string;
  kpi_tags: string[];
  default_push: string;
  default_cta: string;
};

export type CategoryPerformance = {
  leading: string;
  lagging: string;
};

export type PhaseReadiness = {
  trust_panel: {
    fields: string[];
    cta_macro: {
      label: string;
      description: string;
      footer_copy: string;
    };
    badge_states: { state: string; label: string; color: string }[];
  };
  segments: SegmentProfile[];
  model_cache: {
    modes: { id: string; label: string; description: string; sla_seconds: number }[];
    cache_window_days: number;
    default_mode: string;
  };
  transparency_exports: {
    formats: { type: string; fields?: string[]; sections?: string[] }[];
    delivery: { cadence: string; channels: string[] };
  };
  competitor_diff: {
    categories: {
      category: string;
      newskoo: string;
      competitors: string;
      highlight: string;
    }[];
    update_sla_days: number;
  };
  template_library: {
    templates: {
      id: string;
      title: string;
      segments: string[];
      tone: string;
      macros: string[];
    }[];
    recommendations: {
      inputs: string[];
      engine: string;
    };
  };
  partner_widgets: {
    variants: { id: string; description: string; bundle_size: number }[];
    embed_requirements: string[];
  };
  competitor_watch: {
    tracked_competitors: number;
    alerts: { name: string; status: string }[];
    next_review: string;
  };
  value_props: {
    test_window_days: number;
    messages: { id: string; copy: string; segments: string[] }[];
  };
  cta_stack: {
    channels: string[];
    badges: string[];
    defaults: Record<string, string>;
  };
  partner_reports: {
    formats: string[];
    weekly_reports: number;
    tracker: { partner: string; status: string }[];
  };
  kpi_catalog: {
    items: { metric: string; type: string; target: string; source: string }[];
    accuracy_tolerance: string;
    freshness: { leading: string; lagging: string };
  };
  curation_stream: {
    last_batch_id: string;
    avg_cards_per_batch: number;
    sla_minutes: number;
    recent_batches: { id: string; cards: number; badge_coverage: number }[];
  };
  onboarding_schema: {
    fields: { name: string; type: string; required: boolean }[];
    anonymization: string;
  };
  badge_alerts: {
    open_alerts: { category: string; coverage: number }[];
    sla_minutes: number;
    notification_channels: string[];
  };
  categories: {
    metadata: CategoryMetadata[];
    calendar: { day: string; slots: number; focus: string[] }[];
    performance: Record<string, CategoryPerformance>;
  };
};
