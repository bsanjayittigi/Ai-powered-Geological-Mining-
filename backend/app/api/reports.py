"""
OreSight Automated Report Generation APIs
Supports Ministry Query Responses, Production Summaries, and Geological Assessments with clickable citations.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from backend.app.services.document_service import document_service

router = APIRouter(prefix="/reports", tags=["Report Generation"])

class ReportGenRequest(BaseModel):
    report_type: str
    template: str
    subsidiary: str = "SECL"
    mine_unit: str = "Gevra OC"
    date_range: str = "FY 2024-25"
    data_sources: List[str] = ["Production_Report_2025.pdf", "Geological_Survey_2025.pdf"]

@router.get("")
def list_reports():
    return document_service.get_reports()

@router.get("/{report_id}")
def get_report(report_id: str):
    reports = document_service.get_reports()
    for r in reports:
        if r["id"] == report_id:
            return r
    raise HTTPException(status_code=404, detail="Report not found")

@router.post("/generate")
def generate_report(req: ReportGenRequest):
    new_rep = document_service.generate_report(
        report_type=req.report_type,
        template=req.template,
        subsidiary=req.subsidiary,
        mine_unit=req.mine_unit,
        date_range=req.date_range,
        data_sources=req.data_sources
    )
    return new_rep

@router.get("/templates/all")
def get_templates():
    return [
        {"id": "t1", "name": "Ministry/Parliamentary Query Response", "category": "Liaison & Policy"},
        {"id": "t2", "name": "Annual Production & Offtake Summary", "category": "Operations"},
        {"id": "t3", "name": "Geological Seam & Borehole Assessment", "category": "Exploration"},
        {"id": "t4", "name": "Coal Quality & Equilibrated GCV Matrix", "category": "Quality Assurance"},
        {"id": "t5", "name": "Monthly Pithead Stripping Ratio & HEMM Review", "category": "Engineering"}
    ]
