"""
OreSight System Health & Infrastructure Monitoring APIs
"""

from fastapi import APIRouter
from typing import Dict, Any
from backend.app.services.analytics_service import get_health_data

router = APIRouter(prefix="/system", tags=["System Health"])

@router.get("/health")
def get_system_health():
    return get_health_data()
