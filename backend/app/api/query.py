"""
OreSight Natural Language AI Query & RAG APIs
"Ask OreSight" with source-backed evidence citations and hallucination guardrails.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from backend.app.ai.rag_engine import rag_engine

router = APIRouter(prefix="/query", tags=["AI Query & RAG"])

class QueryRequest(BaseModel):
    query: str
    department: Optional[str] = None
    mine_unit: Optional[str] = None

@router.post("")
def ask_oresight(req: QueryRequest):
    result = rag_engine.query(req.query)
    return result

@router.get("/suggestions")
def get_query_suggestions():
    return [
        "What was the annual coal production in 2025 across SECL mines?",
        "Compare production between 2024 and 2025 for Gevra and Kusmunda.",
        "Which mines showed production decline or stripping ratio anomaly?",
        "What are the recurring geological topics in the Jharia basin reports?",
        "Show documents containing information about coal quality Grade G11-G13.",
        "What are the major findings in the latest geological survey?"
    ]
