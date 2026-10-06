"""
Pydantic Schemas for OreSight Extractions, Validation, Query & Reports
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ExtractionResponse(BaseModel):
    id: str
    document_id: str
    document_name: str
    page_number: int
    parameter_name: str
    category: str
    raw_value: str
    normalized_value: Optional[float] = None
    normalized_unit: Optional[str] = None
    confidence: float
    bounding_box: Optional[Dict[str, Any]] = None
    source_table: Optional[str] = None
    source_snippet: Optional[str] = None
    validation_state: str
    subsidiary: str
    mine_unit: Optional[str] = None

class ConflictResolutionRequest(BaseModel):
    conflict_id: str
    resolution_action: str # "ACCEPT_A", "ACCEPT_B", "MARK_REVIEW", "CUSTOM_OVERRIDE"
    override_value: Optional[str] = None
    notes: Optional[str] = None
    resolved_by: str

class QueryRequest(BaseModel):
    query: str
    filters: Optional[Dict[str, Any]] = None

class QuerySource(BaseModel):
    document_id: str
    document_name: str
    page_number: int
    table: Optional[str] = None
    extracted_value: Optional[str] = None
    confidence: float
    validation_status: str
    snippet: str

class QueryResponse(BaseModel):
    query: str
    answer: str
    sources: List[QuerySource]
    confidence: float
    is_sufficient_evidence: bool
    pipeline_steps: Dict[str, float]
    traceability_status: str

class ReportGenerateRequest(BaseModel):
    report_type: str
    template_name: str
    subsidiary: Optional[str] = None
    mine_unit: Optional[str] = None
    date_range: Optional[str] = None
    data_sources: Optional[List[str]] = None
