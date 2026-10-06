import React, { useState, useEffect } from 'react';
import { 
  Layers, LayoutDashboard, FileText, GitBranch, ScanEye, 
  TableProperties, ShieldAlert, Sparkles, Cloud, FileCheck2, 
  BarChart3, History, Network, Settings, Search, Bell, CheckCircle2,
  AlertTriangle, ExternalLink, ChevronRight, UserCheck, ShieldCheck,
  UploadCloud, Play, User
} from 'lucide-react';
import { api } from './services/api';
import { User as UserType, Document, Conflict, ExtractedData } from './types';

export default function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');
  const [currentUser, setCurrentUser] = useState<UserType>({
    id: 'u-admin-1',
    employee_id: 'ADMIN-001',
    full_name: 'Dr. Rajesh Sharma',
    role: 'Administrator',
    organization: 'CMPDI / Coal India Limited',
    subsidiary: 'CMPDI HQ Ranchi',
    department: 'IT & Systems Architecture',
    email: 'r.sharma@cmpdi.co.in'
  });

  const [documents, setDocuments] = useState<Document[]>([]);
  const [extractions, setExtractions] = useState<ExtractedData[]>([]);
  const [conflicts, setConflicts] = useState<Conflict[]>([]);
  const [activeViewerDoc, setActiveViewerDoc] = useState<Document | null>(null);
  const [viewerPage, setViewerPage] = useState<number>(18);

  // AI Query state
  const [queryInput, setQueryInput] = useState('');
  const [queryResult, setQueryResult] = useState<any>(null);
  const [isQueryLoading, setIsQueryLoading] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [docs, exts, confs] = await Promise.all([
        api.getDocuments(),
        api.getExtractions(),
        api.getConflicts()
      ]);
      setDocuments(docs || []);
      setExtractions(exts || []);
      setConflicts(confs || []);
      if (docs && docs.length > 0) setActiveViewerDoc(docs[0]);
    } catch (e) {
      console.error(e);
    }
  };

  const handleAskQuery = async (queryText?: string) => {
    const q = queryText || queryInput;
    if (!q.trim()) return;
    setIsQueryLoading(true);
    try {
      const res = await api.askQuery(q);
      setQueryResult(res);
    } catch (err) {
      console.error(err);
    } finally {
      setIsQueryLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col font-sans bg-slate-50 text-slate-800">
      {/* SIH Official Banner */}
      <header className="bg-slate-900 text-slate-300 text-xs px-4 py-1.5 flex items-center justify-between border-b border-slate-800">
        <div className="flex items-center space-x-3">
          <span className="font-bold bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">
            SIH 2026: SIH26023
          </span>
          <span className="font-medium text-slate-200">
            CMPDI / Coal India Limited (CIL) &bull; “Every Number is Traceable”
          </span>
        </div>
        <div className="flex items-center space-x-2 text-emerald-400 font-semibold">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>DEMO ENVIRONMENT – Validated Mining Intelligence Corpus</span>
        </div>
      </header>

      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 bg-slate-900 text-slate-300 border-r border-slate-800 flex flex-col">
          <div className="p-4 border-b border-slate-800 flex items-center space-x-3">
            <div className="w-9 h-9 rounded-lg bg-gradient-to-tr from-amber-600 to-yellow-400 flex items-center justify-center text-slate-950 font-black">
              <Layers className="w-5 h-5 text-slate-950" />
            </div>
            <div>
              <div className="font-bold text-white text-base">OreSight</div>
              <div className="text-[11px] text-slate-400">CMPDI / CIL Intelligence</div>
            </div>
          </div>

          <nav className="flex-1 p-3 space-y-1 text-xs font-semibold">
            {[
              { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
              { id: 'documents', label: 'Documents', icon: FileText, badge: documents.length },
              { id: 'pipeline', label: 'Processing Pipeline', icon: GitBranch },
              { id: 'viewer', label: 'Document Viewer (3-Pane)', icon: ScanEye },
              { id: 'extractions', label: 'Data Extraction', icon: TableProperties },
              { id: 'validation', label: 'Data Validation', icon: ShieldAlert, badge: conflicts.length, badgeColor: 'bg-rose-500/20 text-rose-300' },
              { id: 'query', label: 'Ask OreSight (RAG)', icon: Sparkles },
              { id: 'topics', label: 'Topic Explorer', icon: Cloud },
              { id: 'reports', label: 'Report Generator', icon: FileCheck2 },
              { id: 'analytics', label: 'Mining Analytics', icon: BarChart3 },
              { id: 'audit', label: 'Audit Trail', icon: History },
              { id: 'architecture', label: 'Architecture', icon: Network },
              { id: 'settings', label: 'Settings & Health', icon: Settings }
            ].map(item => {
              const Icon = item.icon;
              const active = currentPage === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setCurrentPage(item.id)}
                  className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left transition ${
                    active ? 'bg-slate-800 text-amber-400 font-bold' : 'hover:bg-slate-800/60 text-slate-300'
                  }`}
                >
                  <Icon className="w-4 h-4 shrink-0" />
                  <span className="flex-1">{item.label}</span>
                  {item.badge !== undefined && (
                    <span className={`text-[10px] px-1.5 py-0.5 rounded font-mono ${item.badgeColor || 'bg-slate-800 text-slate-300'}`}>
                      {item.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </nav>

          <div className="p-3 border-t border-slate-800 bg-slate-950/60 text-xs">
            <div className="font-bold text-white truncate">{currentUser.full_name}</div>
            <div className="text-[11px] text-amber-400 font-semibold">{currentUser.role} &bull; {currentUser.subsidiary.split(' ')[0]}</div>
          </div>
        </aside>

        {/* Main Content Area */}
        <main className="flex-1 p-6 overflow-y-auto">
          {currentPage === 'dashboard' && (
            <div className="space-y-6">
              <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex justify-between items-center">
                <div>
                  <h1 className="text-xl font-black text-slate-900">Geological & Mining Intelligence Dashboard</h1>
                  <p className="text-xs text-slate-500 mt-1">Smart India Hackathon 2026 Problem SIH26023 (CMPDI / Coal India Limited)</p>
                </div>
                <div className="flex gap-2">
                  <button onClick={() => setCurrentPage('documents')} className="px-3 py-1.5 bg-slate-900 text-white rounded-lg text-xs font-semibold">
                    Upload Documents
                  </button>
                  <button onClick={() => setCurrentPage('query')} className="px-3 py-1.5 bg-blue-600 text-white rounded-lg text-xs font-semibold">
                    Ask AI
                  </button>
                </div>
              </div>

              {/* Pilot Targets */}
              <div className="bg-slate-900 text-white p-4 rounded-2xl border border-slate-800 space-y-3">
                <div className="flex justify-between items-center text-xs">
                  <span className="font-bold uppercase tracking-wider text-slate-300">OreSight Concept Targets</span>
                  <span className="text-[10px] text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/30">
                    Pilot Targets (Not guaranteed production results)
                  </span>
                </div>
                <div className="grid grid-cols-4 gap-3 text-xs">
                  <div className="bg-slate-800/60 p-3 rounded-xl">
                    <div className="text-slate-400 text-[10px]">Report Prep Time</div>
                    <div className="text-base font-black text-amber-400 mt-0.5">70% – 80% Less</div>
                  </div>
                  <div className="bg-slate-800/60 p-3 rounded-xl">
                    <div className="text-slate-400 text-[10px]">Extraction Accuracy</div>
                    <div className="text-base font-black text-emerald-400 mt-0.5">95%+ Target</div>
                  </div>
                  <div className="bg-slate-800/60 p-3 rounded-xl">
                    <div className="text-slate-400 text-[10px]">Workflow Automation</div>
                    <div className="text-base font-black text-blue-400 mt-0.5">80%+ Target</div>
                  </div>
                  <div className="bg-slate-800/60 p-3 rounded-xl">
                    <div className="text-slate-400 text-[10px]">Query Response Time</div>
                    <div className="text-base font-black text-purple-400 mt-0.5">&lt; 5 Seconds</div>
                  </div>
                </div>
              </div>

              {/* KPI Cards */}
              <div className="grid grid-cols-6 gap-3">
                <div className="bg-white p-4 rounded-xl border border-slate-200">
                  <div className="text-slate-500 text-xs">Processed</div>
                  <div className="text-xl font-black text-slate-900 mt-1">1,482</div>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200">
                  <div className="text-slate-500 text-xs">Accuracy</div>
                  <div className="text-xl font-black text-emerald-600 mt-1">96.8%</div>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200">
                  <div className="text-slate-500 text-xs">Validation</div>
                  <div className="text-xl font-black text-slate-900 mt-1">94.2%</div>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200">
                  <div className="text-slate-500 text-xs">Reports</div>
                  <div className="text-xl font-black text-slate-900 mt-1">284</div>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200">
                  <div className="text-slate-500 text-xs">AI Queries</div>
                  <div className="text-xl font-black text-slate-900 mt-1">3,150</div>
                </div>
                <div className="bg-white p-4 rounded-xl border border-slate-200 cursor-pointer" onClick={() => setCurrentPage('validation')}>
                  <div className="text-slate-500 text-xs">Conflicts</div>
                  <div className="text-xl font-black text-rose-600 mt-1">{conflicts.length} Active</div>
                </div>
              </div>
            </div>
          )}

          {currentPage === 'query' && (
            <div className="space-y-6 max-w-4xl mx-auto">
              <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <h2 className="text-lg font-bold text-slate-900">Ask OreSight – Natural Language RAG Assistant</h2>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={queryInput}
                    onChange={(e) => setQueryInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleAskQuery()}
                    placeholder="Ask about coal production, seam XIV thickness, GCV, or Kusmunda..."
                    className="flex-1 p-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <button 
                    onClick={() => handleAskQuery()} 
                    disabled={isQueryLoading}
                    className="px-4 py-2 bg-blue-600 text-white text-xs font-bold rounded-xl hover:bg-blue-700"
                  >
                    {isQueryLoading ? 'Searching...' : 'Ask AI'}
                  </button>
                </div>
              </div>

              {queryResult && (
                <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4 text-xs">
                  <div className="flex justify-between font-bold text-slate-900 pb-2 border-b border-slate-100">
                    <span>AI Answer</span>
                    <span className="text-emerald-700">Confidence: {queryResult.confidence}%</span>
                  </div>
                  <p className="text-sm text-slate-800 leading-relaxed">{queryResult.answer}</p>

                  <div className="space-y-2 pt-2">
                    <span className="font-bold text-slate-900">Traceable Evidence Citations:</span>
                    {queryResult.sources?.map((src: any, i: number) => (
                      <div key={i} className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1">
                        <div className="font-bold text-blue-900">[Source {i+1}: {src.document_name}, Page {src.page_number}]</div>
                        <div className="text-slate-600 italic">"{src.snippet}"</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
