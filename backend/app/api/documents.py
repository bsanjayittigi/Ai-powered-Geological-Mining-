"""
OreSight Document Ingestion & Pipeline APIs
"""

from fastapi import APIRouter, HTTPException, Query, UploadFile, File, Form
from typing import Optional, List, Dict, Any
from backend.app.services.document_service import document_service
from backend.app.ocr.parser import parser_engine

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("")
def list_documents(
    subsidiary: Optional[str] = Query(None),
    status: Optional[str] = Query(None)
):
    return document_service.get_documents(subsidiary, status)

@router.get("/{doc_id}")
def get_document(doc_id: str):
    doc = document_service.get_document_by_id(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/upload")
def upload_document(
    file_name: str = Form(...),
    file_type: str = Form("PDF"),
    file_size: str = Form("3.5 MB"),
    subsidiary: str = Form("SECL"),
    mine_unit: str = Form("Gevra OC"),
    department: str = Form("Mining Operations"),
    category: str = Form("Annual Production Report")
):
    new_doc = document_service.add_document(
        file_name=file_name,
        file_type=file_type,
        file_size=file_size,
        subsidiary=subsidiary,
        mine_unit=mine_unit,
        department=department,
        category=category
    )
    return new_doc

@router.post("/{doc_id}/process")
def process_document(doc_id: str):
    try:
        updated = document_service.process_document(doc_id)
        return {
            "status": "success",
            "message": f"Pipeline completed for {updated['file_name']}",
            "document": updated
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{doc_id}/extractions")
def get_document_extractions(doc_id: str):
    extractions = document_service.get_extractions(doc_id)
    return extractions
