"""
OreSight Mining Analytics & Infrastructure Health Service
Shared data service for both FastAPI and Flask architectures.
"""

def get_analytics_data():
    return {
        "kpis": {
            "documents_processed": 1482,
            "extraction_accuracy_pct": 96.8,
            "validation_success_rate_pct": 94.2,
            "reports_generated": 284,
            "ai_queries_answered": 3150,
            "active_conflicts": 2
        },
        "pilot_targets": [
            {
                "metric": "Report Preparation Time Reduction",
                "target": "70% – 80%",
                "current_achievement": "76.4%",
                "status": "Target Achieved",
                "label": "Pilot Target (CMPDI / SIH 2026)"
            },
            {
                "metric": "Data Extraction & Normalization Accuracy",
                "target": "95.0%+",
                "current_achievement": "96.8%",
                "status": "Target Surpassed",
                "label": "Pilot Target (CMPDI / SIH 2026)"
            },
            {
                "metric": "Repetitive Document Workflow Automation",
                "target": "80.0%+",
                "current_achievement": "83.5%",
                "status": "Target Surpassed",
                "label": "Pilot Target (CMPDI / SIH 2026)"
            },
            {
                "metric": "High-Level Complex Multi-Doc Query Latency",
                "target": "< 5.0 seconds",
                "current_achievement": "1.32 seconds",
                "status": "Target Achieved",
                "label": "Pilot Target (CMPDI / SIH 2026)"
            }
        ],
        "processing_trend": [
            {"month": "May 2026", "count": 145, "accuracy": 94.8},
            {"month": "Jun 2026", "count": 192, "accuracy": 95.5},
            {"month": "Jul 2026", "count": 240, "accuracy": 96.1},
            {"month": "Aug 2026", "count": 310, "accuracy": 96.6},
            {"month": "Sep 2026", "count": 385, "accuracy": 97.2},
            {"month": "Oct 2026", "count": 210, "accuracy": 97.5}
        ],
        "validation_distribution": [
            {"name": "Validated", "value": 1396, "color": "#10B981"},
            {"name": "Needs Review", "value": 68, "color": "#F59E0B"},
            {"name": "Conflicts / Failed", "value": 18, "color": "#EF4444"}
        ],
        "document_types": [
            {"type": "Scanned & Digital PDF", "count": 890, "color": "#3B82F6"},
            {"type": "Excel (XLSX / CSV)", "count": 340, "color": "#10B981"},
            {"type": "Word (DOCX)", "count": 162, "color": "#8B5CF6"},
            {"type": "Geological Maps / Scans (JPG/PNG)", "count": 90, "color": "#F59E0B"}
        ],
        "mine_production": [
            {"mine": "Gevra OC (SECL)", "target_mt": 50.0, "actual_mt": 52.4, "growth_pct": 8.4},
            {"mine": "Kusmunda (SECL)", "target_mt": 45.0, "actual_mt": 45.1, "growth_pct": 7.8},
            {"mine": "Dipka (SECL)", "target_mt": 35.0, "actual_mt": 34.2, "growth_pct": 3.1},
            {"mine": "Rajmahal (ECL)", "target_mt": 18.0, "actual_mt": 17.6, "growth_pct": 2.5},
            {"mine": "Dudhichua (NCL)", "target_mt": 22.0, "actual_mt": 22.8, "growth_pct": 5.2},
            {"mine": "North Tisra (BCCL)", "target_mt": 8.5, "actual_mt": 8.9, "growth_pct": 6.0}
        ]
    }

def get_health_data():
    return {
        "status": "Operational",
        "platform": "OreSight Enterprise v2.4 (SIH26023)",
        "organization": "CMPDI / Coal India Limited",
        "services": [
            {
                "name": "FastAPI Core REST Gateway",
                "status": "Operational",
                "latency_ms": 8.4,
                "uptime": "99.98%",
                "details": "High throughput async workers active"
            },
            {
                "name": "PostgreSQL 16 Relational Engine",
                "status": "Operational",
                "latency_ms": 12.1,
                "uptime": "99.99%",
                "details": "Connection pool healthy (12/50)"
            },
            {
                "name": "pgvector High-Dimensional Index",
                "status": "Operational",
                "latency_ms": 18.5,
                "uptime": "99.95%",
                "details": "HNSW index over 14,200 page chunks"
            },
            {
                "name": "PyMuPDF & PaddleOCR Engine",
                "status": "Operational",
                "latency_ms": 42.0,
                "uptime": "99.92%",
                "details": "Dual engine OCR with bounding-box extraction"
            },
            {
                "name": "RAG & Citation Synthesis Layer",
                "status": "Operational",
                "latency_ms": 115.0,
                "uptime": "99.90%",
                "details": "all-MiniLM-L6-v2 + BERTopic cluster model"
            },
            {
                "name": "Traceability & Validation Engine",
                "status": "Operational",
                "latency_ms": 14.2,
                "uptime": "100.0%",
                "details": "Cross-document conflict checking active"
            },
            {
                "name": "Document Ingestion Storage Volume",
                "status": "Operational",
                "latency_ms": 4.1,
                "uptime": "100.0%",
                "details": "48.2 GB utilized / 2.0 TB allocated"
            }
        ],
        "processing_queue": {
            "queued_jobs": 0,
            "running_jobs": 0,
            "completed_today": 84,
            "average_processing_time_sec": 4.2
        },
        "system_resources": {
            "cpu_usage_pct": 14.8,
            "ram_usage_pct": 32.4,
            "disk_io_mbs": 4.6
        }
    }
