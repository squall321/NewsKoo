import { useEffect, useState } from 'react';
import { fetchRevenuePlan } from '../api/revenue';
import { revenuePlanFallback } from '../data/revenue';
import { PhaseEightRevenuePlan } from '../types/revenue';

type Status = 'idle' | 'loading' | 'ready' | 'error';

type UseRevenuePlanResult = {
  plan: PhaseEightRevenuePlan;
  status: Status;
  source: 'api' | 'fallback';
};

export const useRevenuePlan = (): UseRevenuePlanResult => {
  const [plan, setPlan] = useState<PhaseEightRevenuePlan>(revenuePlanFallback);
  const [status, setStatus] = useState<Status>('idle');
  const [source, setSource] = useState<'api' | 'fallback'>('fallback');

  useEffect(() => {
    let mounted = true;

    const load = async () => {
      setStatus('loading');
      try {
        const payload = await fetchRevenuePlan();
        if (!mounted) return;
        setPlan(payload.plan);
        setSource(payload.source);
        setStatus('ready');
      } catch (error) {
        console.error('Failed to load revenue plan', error);
        if (!mounted) return;
        setPlan(revenuePlanFallback);
        setSource('fallback');
        setStatus('error');
      }
    };

    load();

    return () => {
      mounted = false;
    };
  }, []);

  return { plan, status, source };
};
