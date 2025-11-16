export type TranslationGuardrailStack = {
  metadataFields: string[];
  runtimeLimits: {
    slaMinutes: number;
    gpuHoursPerWeek: number;
  };
  modelPolicy: string;
  rewritePolicy: string;
  references: {
    doc: string;
    issues: string[];
  };
};

export const translationGuardrailStack: TranslationGuardrailStack = {
  metadataFields: ['source_url', 'model_name', 'rewriteReason', 'guardrail_notes', 'cost_ceiling'],
  runtimeLimits: {
    slaMinutes: 60,
    gpuHoursPerWeek: 6,
  },
  modelPolicy: '로컬 7B~13B 모델을 4bit/QLoRA로 구동하고 상용 API 호출은 0건을 유지합니다.',
  rewritePolicy:
    '모든 카드 카피는 원문 출처를 링크하고 “Rewritten for Korean punchlines per translation guardrails.” 메시지와 함께 모델/재작성 사유를 표기합니다.',
  references: {
    doc: '/docs/strategy/translation-guardrails.md',
    issues: ['#ISS-308', '#ISS-311'],
  },
};
