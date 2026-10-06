"""
OreSight Data Validation & Conflict Resolution APIs
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from backend.app.services.document_service import document_service
from backend.app.validation.engine import validation_engine

router = APIRouter(prefix="/validation", tags=["Data Validation"])

class ConflictResolvePayload(BaseModel):
    conflict_id: str
    action: str # "ACCEPT_A", "ACCEPT_B", "MARK_REVIEW"
    resolved_by: str
    notes: Optional[str] = None

@router.get("/conflicts")
def get_conflicts():
    return document_service.get_conflicts()

@router.post("/resolve")
def resolve_conflict(payload: ConflictResolvePayload):
    try:
        updated = document_service.resolve_conflict(
            conflict_id=payload.conflict_id,
            action=payload.action,
            resolved_by=payload.resolved_by,
            notes=payload.notes
        )
        return {
            "status": "success",
            "conflict": updated
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/run")
def trigger_validation():
    all_extractions = document_service.get_extractions()
    new_conflicts = validation_engine.detect_conflicts(all_extractions)
    return {
        "status": "success",
        "message": f"Validation sweep completed across {len(all_extractions)} data points.",
        "conflicts_detected": len(new_conflicts),
        "total_active_conflicts": len(document_service.get_conflicts())
    }

@router.get("/extractions")
def get_all_extractions(doc_id: Optional[str] = None):
    return document_service.get_extractions(doc_id)
