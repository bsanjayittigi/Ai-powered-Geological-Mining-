export interface User {
  id: string;
  employee_id: string;
  full_name: string;
  role: string;
  organization: string;
  subsidiary: string;
  department: string;
  email: string;
}

export interface Document {
  id: string;
  title: string;
  file_name: string;
  file_path: string;
  file_size: string;
  file_type: string;
  page_count: number;
  status: string;
  ocr_status: string;
  validation_status: string;
  subsidiary: string;
  mine_unit?: string;
  department: string;
  document_category: string;
  accuracy_score: number;
}

export interface ExtractedData {
  id: string;
  document_id: string;
  document_name: string;
  page_number: number;
  parameter_name: string;
  category: string;
  raw_value: string;
  normalized_value: number;
  normalized_unit: string;
  confidence: number;
  source_table?: string;
  source_snippet?: string;
  validation_state: string;
  subsidiary: string;
  mine_unit?: string;
}

export interface Conflict {
  id: string;
  title: string;
  parameter_name: string;
  mine_unit: string;
  period: string;
  doc_a: {
    id: string;
    name: string;
    page: number;
    raw_value: string;
    table: string;
    confidence: number;
  };
  doc_b: {
    id: string;
    name: string;
    page: number;
    raw_value: string;
    table: string;
    confidence: number;
  };
  discrepancy: string;
  status: string;
  recommended_action: string;
}

export interface QueryResponse {
  query: string;
  answer: string;
  sources: Array<{
    document_id: string;
    document_name: string;
    page_number: number;
    table?: string;
    extracted_value?: string;
    confidence: number;
    validation_status: string;
    snippet: string;
  }>;
  confidence: number;
  is_sufficient_evidence: boolean;
  pipeline_steps: {
    total_ms: number;
    semantic_search_ms: number;
    evidence_extraction_ms: number;
    llm_synthesis_ms: number;
  };
}
