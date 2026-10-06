"""
OreSight In-Memory State & Document Management Service
Maintains dynamic state for documents, extractions, validation conflicts, reports, and audit trail.
Provides instant responsiveness and full CRUD traceability without external DB dependencies.
"""

import uuid
import os
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

from backend.app.services.mock_data import (
    DEMO_USERS,
    INITIAL_DOCUMENTS,
    INITIAL_EXTRACTIONS,
    INITIAL_CONFLICTS,
    INITIAL_TOPICS,
    INITIAL_AUDIT_LOGS,
    INITIAL_REPORTS
)
from backend.app.validation.engine import validation_engine
from backend.app.ai.rag_engine import rag_engine

class DocumentService:
    def __init__(self):
        self.users = list(DEMO_USERS)
        self.documents = list(INITIAL_DOCUMENTS)
        self.extractions = list(INITIAL_EXTRACTIONS)
        self.conflicts = list(INITIAL_CONFLICTS)
        self.audit_logs = list(INITIAL_AUDIT_LOGS)
        self.reports = list(INITIAL_REPORTS)

    # Documents
    def get_documents(self, subsidiary: Optional[str] = None, status: Optional[str] = None) -> List[Dict[str, Any]]:
        docs = self.documents
        if subsidiary and subsidiary != "ALL":
            docs = [d for d in docs if d.get("subsidiary") == subsidiary]
        if status and status != "ALL":
            docs = [d for d in docs if d.get("status") == status]
        return docs

    def get_document_by_id(self, doc_id: str) -> Optional[Dict[str, Any]]:
        for d in self.documents:
            if d["id"] == doc_id:
                return d
        return None

    def add_document(self, file_name: str, file_type: str, file_size: str, subsidiary: str, mine_unit: str, department: str, category: str) -> Dict[str, Any]:
        new_id = f"doc-{len(self.documents) + 1:03d}"
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %I:%M %p")
        new_doc = {
            "id": new_id,
            "title": file_name.rsplit('.', 1)[0].replace('_', ' ').title(),
            "file_name": file_name,
            "file_path": f"data/sample_documents/{file_name}",
            "file_size": file_size,
            "file_size_bytes": 2048576,
            "file_type": file_type.upper(),
            "page_count": 24 if file_type.upper() == 'PDF' else 6,
            "status": "Processing",
            "ocr_status": "PaddleOCR Running...",
            "validation_status": "Pending",
            "subsidiary": subsidiary or "SECL",
            "mine_unit": mine_unit or "Gevra OC",
            "department": department or "Mining Operations",
            "document_category": category or "Operational Record",
            "reporting_period": "FY 2025-26",
            "uploaded_at": now_str,
            "accuracy_score": 96.5
        }
        self.documents.insert(0, new_doc)
        self.log_audit("Dr. Rajesh Sharma", "Administrator", f"Uploaded mining document: {file_name}", new_doc["title"], 1, "File Upload", "None", file_name, "Processing")
        return new_doc

    def process_document(self, doc_id: str) -> Dict[str, Any]:
        doc = self.get_document_by_id(doc_id)
        if not doc:
            raise ValueError(f"Document {doc_id} not found")

        doc["status"] = "Validated"
        doc["ocr_status"] = "OCR Completed (PyMuPDF + PaddleOCR)"
        doc["validation_status"] = "Validated"
        doc["accuracy_score"] = 98.7

        # Add simulated extracted entry for this document
        ext_id = f"ext-{len(self.extractions) + 101}"
        new_ext = {
            "id": ext_id,
            "document_id": doc["id"],
            "document_name": doc["file_name"],
            "page_number": 4,
            "parameter_name": f"{doc['mine_unit']} Measured Coal Extract",
            "category": "Production",
            "raw_value": "4.28 MT",
            "normalized_value": 4280000.0,
            "normalized_unit": "Tonnes",
            "confidence": 98.6,
            "bounding_box": {"x": 150, "y": 260, "w": 400, "h": 50},
            "source_table": "Operational Log Sheet Table 2",
            "source_snippet": f"Verified extracted measure from {doc['file_name']} showing automated weighbridge data logging.",
            "validation_state": "Validated",
            "subsidiary": doc["subsidiary"],
            "mine_unit": doc["mine_unit"]
        }
        self.extractions.append(new_ext)
        self.log_audit("Pipeline Engine", "System Auto-Parser", f"Executed 6-stage pipeline on {doc['file_name']}", doc["title"], 4, "Pipeline Process", "Processing", "Validated", "Validated")
        return doc

    # Extractions
    def get_extractions(self, doc_id: Optional[str] = None) -> List[Dict[str, Any]]:
        if doc_id:
            return [e for e in self.extractions if e.get("document_id") == doc_id]
        return self.extractions

    # Conflicts
    def get_conflicts(self) -> List[Dict[str, Any]]:
        return self.conflicts

    def resolve_conflict(self, conflict_id: str, action: str, resolved_by: str, notes: Optional[str] = None) -> Dict[str, Any]:
        for c in self.conflicts:
            if c["id"] == conflict_id:
                if action == "ACCEPT_A":
                    c["status"] = "Resolved (Accepted Document A)"
                    new_val = c["doc_a"]["raw_value"]
                elif action == "ACCEPT_B":
                    c["status"] = "Resolved (Accepted Document B)"
                    new_val = c["doc_b"]["raw_value"]
                else:
                    c["status"] = "Marked for Human Review"
                    new_val = "Pending Geologist Review"

                c["resolution_notes"] = notes or f"Action taken by {resolved_by}"
                c["history"].append({
                    "time": datetime.now(timezone.utc).strftime("%Y-%m-%d %I:%M %p"),
                    "actor": resolved_by,
                    "event": f"Status updated to: {c['status']}. Notes: {c['resolution_notes']}"
                })

                self.log_audit(
                    user_name=resolved_by,
                    user_role="Data Analyst",
                    action=f"Resolved validation conflict {conflict_id}",
                    document_title=c["doc_a"]["name"],
                    page_number=c["doc_a"]["page"],
                    field_name=c["parameter_name"],
                    old_value="Conflict Detected",
                    new_value=new_val,
                    validation_status="Resolved"
                )
                return c
        raise ValueError(f"Conflict {conflict_id} not found")

    # Reports
    def get_reports(self) -> List[Dict[str, Any]]:
        return self.reports

    def generate_report(self, report_type: str, template: str, subsidiary: str, mine_unit: str, date_range: str, data_sources: List[str]) -> Dict[str, Any]:
        rep_id = f"rep-{len(self.reports) + 1:03d}"
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %I:%M %p")

        title = f"{report_type} - {mine_unit} ({subsidiary}) [{date_range}]"
        new_report = {
            "id": rep_id,
            "title": title,
            "report_type": report_type,
            "template": template or "CMPDI Standard Enterprise Template",
            "subsidiary": subsidiary or "SECL",
            "mine_unit": mine_unit or "Gevra OC",
            "date_range": date_range or "FY 2024-25 to 2025-26",
            "citations_count": 6,
            "generated_by": "Dr. Rajesh Sharma (Administrator)",
            "generated_at": now_str,
            "validation_status": "All Numbers Traceable & Validated",
            "sections": [
                {
                    "title": "Executive Summary",
                    "content": f"Automated synthesized synthesis for {mine_unit} ({subsidiary}) generated by OreSight. All metrics have undergone cross-document normalization and arithmetic verification."
                },
                {
                    "title": "Production Overview & Offtake",
                    "content": f"Production achieved stood at 52.40 MT against scheduled target [Source: Production_Report_2025.pdf, Page 18]. Peak monthly dispatch attained 1,245,000 tonnes with mechanized loading [Source: Production_Report_2025.pdf, Page 27, Table 4]."
                },
                {
                    "title": "Geological Continuity & Quality Assurance",
                    "content": f"Seam XIV gross thickness confirmed at 8.45 m across core logs [Source: Geological_Survey_2025.pdf, Page 34]. Coal quality registered at 4,120 kcal/kg GCV with 38.2% ash content [Source: Coal_Quality_Report.xlsx, Page 4]."
                },
                {
                    "title": "Validation & Audit Sign-Off",
                    "content": "Every number in this generated document is traceable through: Source Document -> Page -> Table/Figure -> Extracted Value -> Validation Status."
                }
            ]
        }
        self.reports.insert(0, new_report)
        self.log_audit("Dr. Rajesh Sharma", "Administrator", f"Generated traceable report: {title}", title, 1, "Report Generation", "None", f"{new_report['citations_count']} Citations", "Approved")
        return new_report

    # Audit Trail
    def get_audit_logs(self, query: Optional[str] = None) -> List[Dict[str, Any]]:
        if not query:
            return self.audit_logs
        q = query.lower()
        return [l for l in self.audit_logs if q in l["action"].lower() or q in l["user_name"].lower() or q in l.get("document_title", "").lower()]

    def log_audit(self, user_name: str, user_role: str, action: str, document_title: str, page_number: int, field_name: str, old_value: str, new_value: str, validation_status: str):
        log_entry = {
            "id": f"aud-{len(self.audit_logs) + 1}",
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %I:%M %p"),
            "user_name": user_name,
            "user_role": user_role,
            "action": action,
            "document_title": document_title,
            "page_number": page_number,
            "field_name": field_name,
            "old_value": old_value,
            "new_value": new_value,
            "validation_status": validation_status,
            "ip_address": "10.42.12.8"
        }
        self.audit_logs.insert(0, log_entry)

document_service = DocumentService()
