import { useEffect, useState } from 'react';
import { checkApiHealth } from '../api/health';

export const useHealthCheck = () => {
  const [status, setStatus] = useState<'idle' | 'loading' | 'ok' | 'error'>('idle');
  const [message, setMessage] = useState('');

  useEffect(() => {
    let mounted = true;

    const run = async () => {
      setStatus('loading');
      const result = await checkApiHealth();
      if (!mounted) return;
      setStatus(result.ok ? 'ok' : 'error');
      setMessage(result.message);
    };

    run();

    return () => {
      mounted = false;
    };
  }, []);

  return { status, message };
};
