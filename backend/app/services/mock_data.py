"""
OreSight: Geological, Mining & Reporting Intelligence Platform
Mock Data & Knowledge Corpus for CMPDI / Coal India Limited (CIL)
Smart India Hackathon 2026 (SIH26023)
"""

import uuid
from datetime import datetime, timezone

DEMO_USERS = [
    {
        "id": "u-admin-1",
        "employee_id": "ADMIN-001",
        "full_name": "Dr. Rajesh Sharma",
        "role": "Administrator",
        "organization": "CMPDI / Coal India Limited",
        "subsidiary": "CMPDI HQ Ranchi",
        "department": "IT & Systems Architecture",
        "email": "r.sharma@cmpdi.co.in"
    },
    {
        "id": "u-geo-1",
        "employee_id": "GEO-104",
        "full_name": "Ananya Sengupta",
        "role": "Geologist",
        "organization": "CMPDI Regional Institute II",
        "subsidiary": "CMPDI RI-II Dhanbad",
        "department": "Exploration & Geosciences",
        "email": "a.sengupta@cmpdi.co.in"
    },
    {
        "id": "u-eng-1",
        "employee_id": "ENG-208",
        "full_name": "Vikram Singh Chouhan",
        "role": "Mining Engineer",
        "organization": "South Eastern Coalfields Ltd (SECL)",
        "subsidiary": "SECL Bilaspur",
        "department": "Open Cast Operations",
        "email": "vs.chouhan@secl.gov.in"
    },
    {
        "id": "u-ana-1",
        "employee_id": "ANA-315",
        "full_name": "Pooja Deshmukh",
        "role": "Data Analyst",
        "organization": "Coal India Limited",
        "subsidiary": "CIL HQ Kolkata",
        "department": "Corporate Planning & Statistics",
        "email": "p.deshmukh@coalindia.in"
    },
    {
        "id": "u-rep-1",
        "employee_id": "REP-402",
        "full_name": "Manoj Kumar Verma",
        "role": "Reporting Officer",
        "organization": "CMPDI",
        "subsidiary": "CMPDI HQ Ranchi",
        "department": "Parliamentary & Ministry Liaison",
        "email": "mk.verma@cmpdi.co.in"
    },
    {
        "id": "u-view-1",
        "employee_id": "VIEW-501",
        "full_name": "Sunita Rao",
        "role": "Viewer",
        "organization": "Ministry of Coal",
        "subsidiary": "MoC New Delhi",
        "department": "Coal Monitoring Cell",
        "email": "s.rao@coal.gov.in"
    }
]

INITIAL_DOCUMENTS = [
    {
        "id": "doc-001",
        "title": "Annual Production & Dispatch Report FY 2024-25",
        "file_name": "Production_Report_2025.pdf",
        "file_path": "data/sample_documents/Production_Report_2025.pdf",
        "file_size": "4.8 MB",
        "file_size_bytes": 5033164,
        "file_type": "PDF",
        "page_count": 48,
        "status": "Validated",
        "ocr_status": "OCR Completed (PyMuPDF + PaddleOCR)",
        "validation_status": "Validated",
        "subsidiary": "SECL",
        "mine_unit": "Gevra Mega Open Cast",
        "department": "Mining Operations",
        "document_category": "Annual Production Report",
        "reporting_period": "FY 2024-25",
        "uploaded_at": "2026-09-12 10:14 AM",
        "accuracy_score": 98.4
    },
    {
        "id": "doc-002",
        "title": "Geological Survey & Seam Thickness Assessment: Jharia Basin Seam XIV",
        "file_name": "Geological_Survey_2025.pdf",
        "file_path": "data/sample_documents/Geological_Survey_2025.pdf",
        "file_size": "12.2 MB",
        "file_size_bytes": 12792627,
        "file_type": "PDF",
        "page_count": 64,
        "status": "Validated",
        "ocr_status": "OCR Completed (High Precision)",
        "validation_status": "Validated",
        "subsidiary": "BCCL",
        "mine_unit": "North Tisra & Lodna Area",
        "department": "Geological Exploration",
        "document_category": "Geological Assessment",
        "reporting_period": "Q1 2025-26",
        "uploaded_at": "2026-09-18 02:45 PM",
        "accuracy_score": 97.2
    },
    {
        "id": "doc-003",
        "title": "Coal Quality & Equilibrated Moisture/Ash Analysis Sheet",
        "file_name": "Coal_Quality_Report.xlsx",
        "file_path": "data/sample_documents/Coal_Quality_Report.xlsx",
        "file_size": "1.4 MB",
        "file_size_bytes": 1468006,
        "file_type": "XLSX",
        "page_count": 12,
        "status": "Validated",
        "ocr_status": "Structured Table Parser",
        "validation_status": "Validated",
        "subsidiary": "ECL",
        "mine_unit": "Rajmahal Open Cast",
        "department": "Quality Assurance",
        "document_category": "Coal Quality Analysis",
        "reporting_period": "August 2025",
        "uploaded_at": "2026-09-24 11:20 AM",
        "accuracy_score": 99.1
    },
    {
        "id": "doc-004",
        "title": "Historical Mine Statistics & Overburden Stripping Ratio 2024",
        "file_name": "Mine_Statistics_2024.csv",
        "file_path": "data/sample_documents/Mine_Statistics_2024.csv",
        "file_size": "850 KB",
        "file_size_bytes": 870400,
        "file_type": "CSV",
        "page_count": 1,
        "status": "Validated",
        "ocr_status": "Tabular Ingestion",
        "validation_status": "Validated",
        "subsidiary": "NCL",
        "mine_unit": "Dudhichua & Jayant Projects",
        "department": "Mine Planning",
        "document_category": "Historical Statistics",
        "reporting_period": "CY 2024",
        "uploaded_at": "2026-09-29 04:10 PM",
        "accuracy_score": 99.5
    },
    {
        "id": "doc-005",
        "title": "Kusmunda OCP Expansion Project Scanned Lithology & Core Recovery Log",
        "file_name": "Borehole_Lithology_BH402.pdf",
        "file_path": "data/sample_documents/Borehole_Lithology_BH402.pdf",
        "file_size": "18.7 MB",
        "file_size_bytes": 19608371,
        "file_type": "PDF",
        "page_count": 82,
        "status": "Validation Required",
        "ocr_status": "OCR Completed (Scanned 300 DPI)",
        "validation_status": "Validation Required",
        "subsidiary": "SECL",
        "mine_unit": "Kusmunda OCP",
        "department": "Core Drilling Division",
        "document_category": "Borehole Log",
        "reporting_period": "July 2025",
        "uploaded_at": "2026-10-01 09:30 AM",
        "accuracy_score": 94.6
    },
    {
        "id": "doc-006",
        "title": "Ministry Parliamentary Submission - Coal Offtake & Rail Rake Allocation",
        "file_name": "Ministry_Submission_CIL_Q2.docx",
        "file_path": "data/sample_documents/Ministry_Submission_CIL_Q2.docx",
        "file_size": "2.1 MB",
        "file_size_bytes": 2202009,
        "file_type": "DOCX",
        "page_count": 16,
        "status": "Validation Required",
        "ocr_status": "DOCX Parsed",
        "validation_status": "Validation Required",
        "subsidiary": "CIL HQ",
        "mine_unit": "All CIL Subsidiaries",
        "department": "Logistics & Transport",
        "document_category": "Ministry Submission",
        "reporting_period": "Q2 2025-26",
        "uploaded_at": "2026-10-03 01:15 PM",
        "accuracy_score": 95.8
    }
]

INITIAL_EXTRACTIONS = [
    {
        "id": "ext-101",
        "document_id": "doc-001",
        "document_name": "Production_Report_2025.pdf",
        "page_number": 18,
        "parameter_name": "Annual Raw Coal Production",
        "category": "Production",
        "raw_value": "52.40 MT",
        "normalized_value": 52400000.0,
        "normalized_unit": "Tonnes",
        "confidence": 98.4,
        "bounding_box": {"x": 140, "y": 380, "w": 420, "h": 45},
        "source_table": "Table 4: Annual Production & Offtake Summary",
        "source_snippet": "The total raw coal production achieved from Gevra Mega Open Cast project for FY 2024-25 stood at 52.40 MT against a target of 50.00 MT, registering an achievement of 104.8%.",
        "validation_state": "Validated",
        "subsidiary": "SECL",
        "mine_unit": "Gevra OC"
    },
    {
        "id": "ext-102",
        "document_id": "doc-001",
        "document_name": "Production_Report_2025.pdf",
        "page_number": 27,
        "parameter_name": "Monthly Peak Dispatch",
        "category": "Production",
        "raw_value": "1,245,000 tonnes",
        "normalized_value": 1245000.0,
        "normalized_unit": "Tonnes",
        "confidence": 97.4,
        "bounding_box": {"x": 120, "y": 240, "w": 380, "h": 50},
        "source_table": "Production Summary Table 4",
        "source_snippet": "Peak monthly dispatch was recorded in January 2025 reaching 1,245,000 tonnes through mechanized merry-go-round (MGR) and in-pit conveyor loops.",
        "validation_state": "Validated",
        "subsidiary": "SECL",
        "mine_unit": "Gevra OC"
    },
    {
        "id": "ext-103",
        "document_id": "doc-002",
        "document_name": "Geological_Survey_2025.pdf",
        "page_number": 34,
        "parameter_name": "Seam XIV Gross Thickness",
        "category": "Geology",
        "raw_value": "8.45 metres",
        "normalized_value": 8.45,
        "normalized_unit": "Metres",
        "confidence": 96.5,
        "bounding_box": {"x": 160, "y": 420, "w": 350, "h": 40},
        "source_table": "Seam Lithology Correlation Chart 3B",
        "source_snippet": "Seam XIV exhibits a persistent average gross thickness of 8.45 metres across boreholes BH-12 through BH-28, with minor shale parting ranging from 0.15 to 0.40 m.",
        "validation_state": "Validated",
        "subsidiary": "BCCL",
        "mine_unit": "North Tisra Area"
    },
    {
        "id": "ext-104",
        "document_id": "doc-003",
        "document_name": "Coal_Quality_Report.xlsx",
        "page_number": 4,
        "parameter_name": "Gross Calorific Value (GCV)",
        "category": "Coal Quality",
        "raw_value": "4,120 kcal/kg",
        "normalized_value": 4120.0,
        "normalized_unit": "kcal/kg",
        "confidence": 99.1,
        "bounding_box": {"x": 200, "y": 180, "w": 400, "h": 60},
        "source_table": "Equilibrated Proximate Analysis Table",
        "source_snippet": "Average GCV determined by bomb calorimeter on 60 mesh equilibrated sample is 4,120 kcal/kg, qualifying the seam under CIL Grade G11.",
        "validation_state": "Validated",
        "subsidiary": "ECL",
        "mine_unit": "Rajmahal OC"
    },
    {
        "id": "ext-105",
        "document_id": "doc-003",
        "document_name": "Coal_Quality_Report.xlsx",
        "page_number": 4,
        "parameter_name": "Equilibrated Ash Content",
        "category": "Coal Quality",
        "raw_value": "38.2 %",
        "normalized_value": 38.2,
        "normalized_unit": "%",
        "confidence": 98.7,
        "bounding_box": {"x": 200, "y": 250, "w": 400, "h": 50},
        "source_table": "Equilibrated Proximate Analysis Table",
        "source_snippet": "Ash percentage at 60% relative humidity and 40°C temperature: 38.2% wt, suitable for pithead thermal power plant consumption without heavy washing.",
        "validation_state": "Validated",
        "subsidiary": "ECL",
        "mine_unit": "Rajmahal OC"
    },
    {
        "id": "ext-106",
        "document_id": "doc-005",
        "document_name": "Borehole_Lithology_BH402.pdf",
        "page_number": 19,
        "parameter_name": "Core Recovery Percentage (Seam Lower)",
        "category": "Geology",
        "raw_value": "91.8 %",
        "normalized_value": 91.8,
        "normalized_unit": "%",
        "confidence": 93.2,
        "bounding_box": {"x": 130, "y": 510, "w": 390, "h": 45},
        "source_table": "Drilling Log Depth Interval 142m - 178m",
        "source_snippet": "Core recovery recorded in BH-402 between depths 155.20 m and 168.40 m across the lower carbonaceous shale and dull banded coal reached 91.8%.",
        "validation_state": "Needs Review",
        "subsidiary": "SECL",
        "mine_unit": "Kusmunda OCP"
    },
    {
        "id": "ext-107",
        "document_id": "doc-006",
        "document_name": "Ministry_Submission_CIL_Q2.docx",
        "page_number": 8,
        "parameter_name": "Peak Dispatch (Ministry Statement)",
        "category": "Production",
        "raw_value": "1,268,000 tonnes",
        "normalized_value": 1268000.0,
        "normalized_unit": "Tonnes",
        "confidence": 95.8,
        "bounding_box": {"x": 110, "y": 310, "w": 440, "h": 50},
        "source_table": "Annexure II - Subsidiary Dispatch Breakdown",
        "source_snippet": "Gevra mine recorded highest dispatch volume in Jan 2025 with 1,268,000 tonnes dispatched through railway sidings and dedicated road corridors.",
        "validation_state": "Conflict Detected",
        "subsidiary": "SECL",
        "mine_unit": "Gevra OC"
    }
]

INITIAL_CONFLICTS = [
    {
        "id": "conf-001",
        "title": "Production & Dispatch Discrepancy (Gevra OC)",
        "parameter_name": "Peak Monthly Dispatch (January 2025)",
        "mine_unit": "Gevra Mega Open Cast (SECL)",
        "period": "January 2025",
        "doc_a": {
            "id": "doc-001",
            "name": "Production_Report_2025.pdf",
            "page": 27,
            "table": "Production Summary Table 4",
            "raw_value": "1,245,000 tonnes",
            "normalized": 1245000,
            "unit": "Tonnes",
            "confidence": 97.4,
            "department": "Mining Operations"
        },
        "doc_b": {
            "id": "doc-006",
            "name": "Ministry_Submission_CIL_Q2.docx",
            "page": 8,
            "table": "Annexure II - Dispatch Breakdown",
            "raw_value": "1,268,000 tonnes",
            "normalized": 1268000,
            "unit": "Tonnes",
            "confidence": 95.8,
            "department": "Logistics & Transport"
        },
        "discrepancy": "+23,000 tonnes (+1.85%)",
        "status": "Conflict Detected",
        "severity": "High",
        "root_cause": "Document B includes provisional road transport dispatch without final weighbridge reconciliation; Document A uses final audited weighbridge net figures.",
        "recommended_action": "Accept Value A (Audited Production Report weighbridge data)",
        "history": [
            {"time": "2026-10-03 01:20 PM", "actor": "Automated Cross-Document Engine", "event": "Detected 1.85% discrepancy exceeding 0.5% threshold."}
        ]
    },
    {
        "id": "conf-002",
        "title": "Coal Grade Assignment Divergence (Rajmahal Seam IV)",
        "parameter_name": "Equilibrated Gross Calorific Value",
        "mine_unit": "Rajmahal OC (ECL)",
        "period": "August 2025",
        "doc_a": {
            "id": "doc-003",
            "name": "Coal_Quality_Report.xlsx",
            "page": 4,
            "table": "Equilibrated Proximate Analysis Table",
            "raw_value": "4,120 kcal/kg (Grade G11)",
            "normalized": 4120,
            "unit": "kcal/kg",
            "confidence": 99.1,
            "department": "Quality Assurance"
        },
        "doc_b": {
            "id": "doc-004",
            "name": "Mine_Statistics_2024.csv",
            "page": 1,
            "table": "Annual Seam Master Sheet",
            "raw_value": "3,890 kcal/kg (Grade G12)",
            "normalized": 3890,
            "unit": "kcal/kg",
            "confidence": 94.0,
            "department": "Mine Planning"
        },
        "discrepancy": "+230 kcal/kg (+5.91%)",
        "status": "Under Review",
        "severity": "Medium",
        "root_cause": "Recent selective mining reduced carbonaceous shale contamination, upgrading delivered quality from G12 to G11.",
        "recommended_action": "Mark for Geologist Human Review & Core Sample Re-testing",
        "history": [
            {"time": "2026-09-30 11:15 AM", "actor": "Validation Engine", "event": "Triggered Grade boundary transition alert (G12 -> G11)."}
        ]
    }
]

INITIAL_TOPICS = [
    {
        "id": 1,
        "name": "Geological Exploration & Boreholes",
        "category": "Geology",
        "document_count": 342,
        "frequency": 88.5,
        "keywords": ["borehole", "seam thickness", "lithology", "parting", "core recovery", "shale", "coal horizon", "dip"],
        "yearly_trend": {"2021": 42, "2022": 58, "2023": 79, "2024": 110, "2025": 142},
        "subsidiaries": {"BCCL": 120, "CMPDI": 95, "SECL": 75, "ECL": 52}
    },
    {
        "id": 2,
        "name": "Open Cast Production & Draglines",
        "category": "Production",
        "document_count": 485,
        "frequency": 96.2,
        "keywords": ["ROM coal", "overburden", "stripping ratio", "dragline", "shovel dumper", "in-pit crushing", "dispatch", "rake"],
        "yearly_trend": {"2021": 60, "2022": 82, "2023": 115, "2024": 140, "2025": 188},
        "subsidiaries": {"SECL": 180, "NCL": 145, "MCL": 110, "CCL": 50}
    },
    {
        "id": 3,
        "name": "Coal Quality & Equilibrated GCV",
        "category": "Coal Quality",
        "document_count": 274,
        "frequency": 79.4,
        "keywords": ["GCV", "ash content", "moisture", "volatile matter", "grade G11", "grade G12", "bomb calorimeter", "FSI"],
        "yearly_trend": {"2021": 35, "2022": 44, "2023": 61, "2024": 82, "2025": 102},
        "subsidiaries": {"ECL": 90, "CCL": 70, "BCCL": 64, "SECL": 50}
    },
    {
        "id": 4,
        "name": "Safety & Slope Stability",
        "category": "Safety",
        "document_count": 196,
        "frequency": 68.1,
        "keywords": ["slope stability", "radar monitoring", "bench height", "dump failure", "DGMS compliance", "gas drainage"],
        "yearly_trend": {"2021": 20, "2022": 32, "2023": 48, "2024": 62, "2025": 74},
        "subsidiaries": {"BCCL": 70, "SECL": 55, "ECL": 40, "CMPDI": 31}
    },
    {
        "id": 5,
        "name": "Environmental Clearance & Forestry",
        "category": "Environment",
        "document_count": 162,
        "frequency": 61.3,
        "keywords": ["reclamation", "topsoil", "afforestation", "MoEFCC", "particulate matter", "water sprinkling", "green belt"],
        "yearly_trend": {"2021": 18, "2022": 26, "2023": 39, "2024": 52, "2025": 67},
        "subsidiaries": {"CMPDI": 60, "MCL": 42, "SECL": 35, "CCL": 25}
    },
    {
        "id": 6,
        "name": "Heavy Earth Moving Machinery (HEMM)",
        "category": "Equipment",
        "document_count": 218,
        "frequency": 72.8,
        "keywords": ["HEMM", "caterpillar", "komatsu", "240T dumper", "availability %", "utilization %", "breakdown", "MTBF"],
        "yearly_trend": {"2021": 30, "2022": 41, "2023": 54, "2024": 69, "2025": 84},
        "subsidiaries": {"NCL": 85, "SECL": 72, "MCL": 41, "WCL": 20}
    }
]

INITIAL_AUDIT_LOGS = [
    {
        "id": "aud-1",
        "timestamp": "2026-10-04 11:32 AM",
        "user_name": "Dr. Rajesh Sharma",
        "user_role": "Administrator",
        "action": "Updated production value after weighbridge reconciliation",
        "document_title": "Production_Report_2025.pdf",
        "page_number": 27,
        "field_name": "Monthly Peak Dispatch",
        "old_value": "1,245,000 tonnes",
        "new_value": "1,247,000 tonnes",
        "validation_status": "Human Verified",
        "ip_address": "10.42.12.8"
    },
    {
        "id": "aud-2",
        "timestamp": "2026-10-04 10:15 AM",
        "user_name": "Pooja Deshmukh",
        "user_role": "Data Analyst",
        "action": "Triggered cross-document reconciliation check",
        "document_title": "Ministry_Submission_CIL_Q2.docx",
        "page_number": 8,
        "field_name": "Peak Dispatch (Ministry Statement)",
        "old_value": "Pending",
        "new_value": "Conflict Detected (vs Production_Report_2025.pdf)",
        "validation_status": "Conflict Detected",
        "ip_address": "10.42.15.22"
    },
    {
        "id": "aud-3",
        "timestamp": "2026-10-03 04:50 PM",
        "user_name": "Ananya Sengupta",
        "user_role": "Geologist",
        "action": "Verified Seam XIV lithological boundary",
        "document_title": "Geological_Survey_2025.pdf",
        "page_number": 34,
        "field_name": "Seam XIV Gross Thickness",
        "old_value": "8.40 metres (Initial OCR)",
        "new_value": "8.45 metres",
        "validation_status": "Validated",
        "ip_address": "10.42.18.104"
    },
    {
        "id": "aud-4",
        "timestamp": "2026-10-02 02:10 PM",
        "user_name": "Manoj Kumar Verma",
        "user_role": "Reporting Officer",
        "action": "Synthesized Ministry Briefing on Coal Offtake Trends",
        "document_title": "Ministry_Parliamentary_Response_2026_Q2.pdf",
        "page_number": 1,
        "field_name": "Automated Report Generation",
        "old_value": "Draft",
        "new_value": "Generated with 14 Traceable Citations",
        "validation_status": "Approved",
        "ip_address": "10.42.10.5"
    }
]

INITIAL_REPORTS = [
    {
        "id": "rep-001",
        "title": "Ministry of Coal Parliamentary Briefing: SECL & BCCL High-Volume Performance",
        "report_type": "Ministry/Parliamentary Query Response",
        "template": "Official MoC Briefing Template",
        "subsidiary": "SECL & BCCL",
        "mine_unit": "Gevra OC & North Tisra",
        "date_range": "FY 2024-25 to Q2 2025-26",
        "citations_count": 8,
        "generated_by": "Manoj Kumar Verma (Reporting Officer)",
        "generated_at": "2026-10-02 02:30 PM",
        "validation_status": "All Numbers Traceable & Validated",
        "sections": [
            {
                "title": "Executive Summary",
                "content": "In response to Parliamentary Lok Sabha starred question regarding raw coal evacuation, SECL Gevra Mega OC maintained peak dispatch rates surpassing targets, supported by automated rail rapid loading systems (RLS). Borehole assessments in BCCL Jharia confirmed persistent Seam XIV thickness supporting high-coking reserves."
            },
            {
                "title": "Production Overview & Evacuation Metrics",
                "content": "SECL Gevra achieved annual production of 52.40 MT (104.8% achievement against target) [Source: Production_Report_2025.pdf, Page 18]. Peak monthly dispatch reached 1,245,000 tonnes in January 2025 [Source: Production_Report_2025.pdf, Page 27, Table 4]."
            },
            {
                "title": "Geological & Quality Assurance Findings",
                "content": "Jharia Basin Seam XIV shows gross thickness of 8.45 metres across boreholes BH-12 to BH-28 [Source: Geological_Survey_2025.pdf, Page 34]. Rajmahal open cast coal testing yielded Gross Calorific Value of 4,120 kcal/kg with 38.2% ash [Source: Coal_Quality_Report.xlsx, Page 4]."
            }
        ]
    }
]
