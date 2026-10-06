"""
OreSight Mining Analytics & KPI APIs
"""

from fastapi import APIRouter
from typing import Dict, Any
from backend.app.services.analytics_service import get_analytics_data

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("")
def get_analytics():
    return get_analytics_data()
