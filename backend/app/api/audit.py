"""
OreSight Tamper-Evident Audit Trail APIs
"""

from fastapi import APIRouter, Query
from typing import Optional, List, Dict, Any
from backend.app.services.document_service import document_service

router = APIRouter(prefix="/audit", tags=["Audit Trail"])

@router.get("")
def get_audit_trail(q: Optional[str] = Query(None)):
    return document_service.get_audit_logs(q)
