import { useEffect, useState } from 'react';
import { fetchPhaseData } from '../api/phases';
import { phaseProgressFallback, phaseReadinessFallback } from '../data/phaseReadiness';
import { PhaseProgress, PhaseReadiness } from '../types/phases';

type Status = 'idle' | 'loading' | 'ready' | 'error';

type UsePhaseDataResult = {
  progress: PhaseProgress[];
  readiness: PhaseReadiness | null;
  status: Status;
  source: 'api' | 'fallback';
};

export const usePhaseData = (): UsePhaseDataResult => {
  const [progress, setProgress] = useState<PhaseProgress[]>(phaseProgressFallback);
  const [readiness, setReadiness] = useState<PhaseReadiness | null>(null);
  const [status, setStatus] = useState<Status>('idle');
  const [source, setSource] = useState<'api' | 'fallback'>('fallback');

  useEffect(() => {
    let mounted = true;
    const load = async () => {
      setStatus('loading');
      try {
        const payload = await fetchPhaseData();
        if (!mounted) return;
        setProgress(payload.progress);
        setReadiness(payload.readiness);
        setSource(payload.source);
        setStatus('ready');
      } catch (error) {
        console.error('Failed to load phase data', error);
        if (!mounted) return;
        setProgress(phaseProgressFallback);
        setReadiness(phaseReadinessFallback);
        setSource('fallback');
        setStatus('error');
      }
    };

    load();

    return () => {
      mounted = false;
    };
  }, []);

  return { progress, readiness, status, source };
};
