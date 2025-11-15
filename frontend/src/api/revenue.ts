import { revenuePlanFallback } from '../data/revenue';
import { PhaseEightRevenuePlan } from '../types/revenue';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '';

const fetchJson = async <T>(url: string): Promise<T> => {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}`);
  }
  return (await response.json()) as T;
};

export type RevenuePlanResponse = {
  plan: PhaseEightRevenuePlan;
  meta: {
    phase: string;
    hypotheses: number;
    experiments: number;
    guardrail_ref: string;
  };
};

export const fetchRevenuePlan = async (): Promise<{
  plan: PhaseEightRevenuePlan;
  source: 'api' | 'fallback';
}> => {
  if (!API_BASE_URL) {
    return { plan: revenuePlanFallback, source: 'fallback' };
  }

  try {
    const payload = await fetchJson<RevenuePlanResponse>(`${API_BASE_URL}/revenue/phase-008`);
    return {
      plan: payload?.plan ?? revenuePlanFallback,
      source: 'api',
    };
  } catch (error) {
    console.warn('Falling back to embedded revenue plan payload', error);
    return { plan: revenuePlanFallback, source: 'fallback' };
  }
};
