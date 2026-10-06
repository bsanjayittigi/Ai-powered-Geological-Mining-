"""
Pydantic Schemas for OreSight Documents & Pages
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DocumentBase(BaseModel):
    title: str
    file_name: str
    file_type: str
    subsidiary: str
    mine_unit: Optional[str] = None
    department: str
    document_category: str
    reporting_period: Optional[str] = None

class DocumentCreate(DocumentBase):
    file_size_bytes: int
    page_count: int = 1

class DocumentResponse(DocumentBase):
    id: str
    file_path: str
    file_size: str
    file_size_bytes: int
    page_count: int
    status: str
    ocr_status: str
    validation_status: str
    uploaded_at: str
    accuracy_score: float

class PageData(BaseModel):
    page_number: int
    text: str
    tables: List[Dict[str, Any]] = []
    entities: List[Dict[str, Any]] = []
    ocr_confidence: float
