"""
OreSight: AI-Powered Geological, Mining & Reporting Intelligence Platform
FastAPI Application Entry Point
Smart India Hackathon 2026 - Problem SIH26023 (CMPDI / Coal India Limited)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from backend.app.api.auth import router as auth_router
from backend.app.api.documents import router as documents_router
from backend.app.api.validation import router as validation_router
from backend.app.api.query import router as query_router
from backend.app.api.reports import router as reports_router
from backend.app.api.topics import router as topics_router
from backend.app.api.analytics import router as analytics_router
from backend.app.api.audit import router as audit_router
from backend.app.api.health import router as health_router

app = FastAPI(
    title="OreSight – Mining Intelligence Platform API",
    description="Backend API for CMPDI / Coal India Limited (SIH26023). Converts fragmented mining documents into structured, validated, searchable and traceable intelligence.",
    version="2.4.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for local Vite frontend dev server or external clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers under /api
app.include_router(auth_router, prefix="/api")
app.include_router(documents_router, prefix="/api")
app.include_router(validation_router, prefix="/api")
app.include_router(query_router, prefix="/api")
app.include_router(reports_router, prefix="/api")
app.include_router(topics_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")
app.include_router(audit_router, prefix="/api")
app.include_router(health_router, prefix="/api")

@app.get("/")
def root():
    return {
        "platform": "OreSight Mining Intelligence Platform",
        "organization": "CMPDI / Coal India Limited",
        "hackathon": "Smart India Hackathon 2026 (SIH26023)",
        "principle": "Every number is traceable (Document -> Page -> Table -> Extracted Value -> Validation)",
        "api_docs": "/docs",
        "status": "Operational"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
