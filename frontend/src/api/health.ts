const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '';

export const checkApiHealth = async (): Promise<{ ok: boolean; message: string }> => {
  if (!API_BASE_URL) {
    return { ok: false, message: 'API base URL is not configured.' };
  }

  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (!response.ok) {
      return { ok: false, message: `API responded with status ${response.status}` };
    }
    const payload = await response.json().catch(() => ({ message: 'Healthy' }));
    return { ok: true, message: payload.message ?? 'Healthy' };
  } catch (error) {
    return { ok: false, message: error instanceof Error ? error.message : 'Unknown error' };
  }
};
