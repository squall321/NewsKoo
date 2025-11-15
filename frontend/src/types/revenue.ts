export type RevenueBundle = {
  bundle_id: string;
  name: string;
  categories: string[];
  deliverables: string[];
  kpi_reporting: string[];
  pricing_model: string;
  floor_cpm: number;
  notes: string;
  guardrail_ref: string;
  dependencies: string[];
};

export type RevenueHypothesis = {
  hypothesis_id: string;
  title: string;
  statement: string;
  bundle_id: string;
  target_segments: string[];
  evidence: string[];
  success_metrics: string[];
};

export type RevenueExperiment = {
  experiment_id: string;
  hypothesis_id: string;
  goal_metric: string;
  schedule: string;
  dependencies: string[];
  issue_tags: string[];
  status: string;
};

export type RevenueGuardrails = {
  reference_doc: string;
  model_policy: string;
  source_policy: string;
  cost_ceiling: string;
  approval_path: string;
};

export type RevenuePlanApprovals = {
  workshop: string;
  decision_log: string[];
  risk_register: string[];
};

export type PhaseEightRevenuePlan = {
  phase: string;
  last_synced_at: string;
  guardrails: RevenueGuardrails;
  bundles: RevenueBundle[];
  hypotheses: RevenueHypothesis[];
  experiments: RevenueExperiment[];
  dependencies: { id: string; description: string; issue_tags: string[]; phases: string[] }[];
  approvals: RevenuePlanApprovals;
};
