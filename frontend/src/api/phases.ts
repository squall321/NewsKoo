import { phaseProgressFallback, phaseReadinessFallback } from '../data/phaseReadiness';
import { PhaseProgress, PhaseReadiness } from '../types/phases';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '';

const fetchJson = async <T>(url: string): Promise<T> => {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}`);
  }
  return (await response.json()) as T;
};

export type PhaseDataResponse = {
  progress: PhaseProgress[];
  readiness: PhaseReadiness;
  source: 'api' | 'fallback';
};

export const fetchPhaseData = async (): Promise<PhaseDataResponse> => {
  if (!API_BASE_URL) {
    return {
      progress: phaseProgressFallback,
      readiness: phaseReadinessFallback,
      source: 'fallback',
    };
  }

  try {
    const [progressPayload, readinessPayload] = await Promise.all([
      fetchJson<{ phases: PhaseProgress[] }>(`${API_BASE_URL}/phases/progress`),
      fetchJson<{ snapshot: PhaseReadiness }>(`${API_BASE_URL}/phases/readiness`),
    ]);

    return {
      progress: progressPayload?.phases ?? phaseProgressFallback,
      readiness: readinessPayload?.snapshot ?? phaseReadinessFallback,
      source: 'api',
    };
  } catch (error) {
    console.warn('Falling back to embedded phase readiness payload', error);
    return {
      progress: phaseProgressFallback,
      readiness: phaseReadinessFallback,
      source: 'fallback',
    };
  }
};
