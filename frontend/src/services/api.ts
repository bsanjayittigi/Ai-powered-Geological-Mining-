/**
 * OreSight Frontend API Client Service
 */

const API_BASE = '/api';

export const api = {
  // Auth
  login: async (employeeId: string) => {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ employee_id: employeeId, password: 'demo' })
    });
    return res.json();
  },

  // Documents
  getDocuments: async (subsidiary?: string, status?: string) => {
    const params = new URLSearchParams();
    if (subsidiary && subsidiary !== 'ALL') params.append('subsidiary', subsidiary);
    if (status && status !== 'ALL') params.append('status', status);
    const res = await fetch(`${API_BASE}/documents?${params.toString()}`);
    return res.json();
  },

  getDocument: async (docId: string) => {
    const res = await fetch(`${API_BASE}/documents/${docId}`);
    return res.json();
  },

  processDocument: async (docId: string) => {
    const res = await fetch(`${API_BASE}/documents/${docId}/process`, { method: 'POST' });
    return res.json();
  },

  // Extractions & Validation
  getExtractions: async (docId?: string) => {
    const url = docId ? `${API_BASE}/validation/extractions?doc_id=${docId}` : `${API_BASE}/validation/extractions`;
    const res = await fetch(url);
    return res.json();
  },

  getConflicts: async () => {
    const res = await fetch(`${API_BASE}/validation/conflicts`);
    return res.json();
  },

  resolveConflict: async (conflictId: string, action: string, resolvedBy: string, notes?: string) => {
    const res = await fetch(`${API_BASE}/validation/resolve`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ conflict_id: conflictId, action, resolved_by: resolvedBy, notes })
    });
    return res.json();
  },

  // AI Query
  askQuery: async (query: string) => {
    const res = await fetch(`${API_BASE}/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    return res.json();
  },

  // Reports
  getReports: async () => {
    const res = await fetch(`${API_BASE}/reports`);
    return res.json();
  },

  generateReport: async (payload: any) => {
    const res = await fetch(`${API_BASE}/reports/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    return res.json();
  },

  // Analytics & Health
  getAnalytics: async () => {
    const res = await fetch(`${API_BASE}/analytics`);
    return res.json();
  },

  getSystemHealth: async () => {
    const res = await fetch(`${API_BASE}/system/health`);
    return res.json();
  }
};
