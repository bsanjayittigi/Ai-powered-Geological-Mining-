# OreSight: AI-Powered Geological, Mining & Reporting Intelligence Platform

[![Smart India Hackathon 2026](https://img.shields.io/badge/SIH-2026-orange.svg)](https://sih.gov.in/)
[![Problem Statement](https://img.shields.io/badge/Problem-SIH26023-blue.svg)](#)
[![Target Organization](https://img.shields.io/badge/Client-CMPDI%20%2F%20Coal%20India%20Limited-green.svg)](#)
[![Traceability](https://img.shields.io/badge/Core%20Principle-Every%20Number%20is%20Traceable-yellow.svg)](#)

> **OreSight** is an enterprise AI intelligence and reporting platform developed for **Central Mine Planning & Design Institute (CMPDI)** and **Coal India Limited (CIL)** subsidiaries. It ingests fragmented geological maps, borehole lithology logs, annual production reports, and coal quality sheets, converting them into structured, validated, searchable, and citation-backed intelligence.

---

## 🏛️ Core Design Philosophy: "Every Number is Traceable"

Unlike generic conversational PDF chatbots that hallucinate mining metrics, OreSight enforces a deterministic evidence audit chain:

```
Source Document (PDF/DOCX/XLSX)
   │
   ▼
Page & Bounding Box Coordinates
   │
   ▼
Table / Figure / Lithology Column
   │
   ▼
Extracted Value & Normalized Unit (MT, kcal/kg, %)
   │
   ▼
Validation Status (Rules + Cross-Document Consistency)
```

---

## 🚀 Key Modules & Capabilities

1. **Document Ingestion Hub**: Multi-format drag-and-drop processing for scanned PDFs, borehole logs, DOCX, XLSX/CSV, and high-resolution geological maps.
2. **6-Step Pipeline Architecture**: Upload → OCR/Parse → Normalize Units/Dates → Validate Cross-Document → AI Layer (RAG + BERTopic) → Cited Report.
3. **Advanced 3-Pane Document Viewer**: Interactive visual inspector with page thumbnails, highlighted bounding boxes, and live evidence traceability.
4. **Data Extraction & Normalization**: Automatically standardizes metric units (`MT`, `Lakh Tonnes`, `m`, `kcal/kg`) and extracts geological seam parameters.
5. **Data Validation & Conflict Resolution**: Cross-checks figures across disparate departmental reports (e.g. Annual Production vs. Sub-committee submission) with side-by-side human review diffing.
6. **"Ask OreSight" (RAG AI Query)**: Natural language query engine backed by semantic vector search, generating cited responses with exact page numbers and evidence snippets.
7. **Topic Explorer & Semantic Archives**: Historical archive exploration using BERTopic-style semantic clusters, word cloud, and subsidiary frequency trends.
8. **Automated Report Generation**: One-click generation of Ministry/Parliamentary query responses, geological assessments, and annual production summaries with clickable source links.
9. **Mining Analytics Dashboard**: Visualizations for Run-of-Mine (ROM) production, Overburden Removal (OBR), stripping ratios, and coal quality grade distributions.
10. **Tamper-Evident Audit Trail**: Role-based change logs tracking every manual override, validation approval, and parameter modification.

---

## 👥 Role-Based Access Control (RBAC)

| Role | Default User ID | Capabilities |
| :--- | :--- | :--- |
| **Administrator** | `ADMIN-001` | Full administrative access, audit trail, user & pipeline configuration |
| **Geologist** | `GEO-104` | Borehole log analysis, seam thickness validation, lithology extraction |
| **Mining Engineer** | `ENG-208` | Production figures, OBR, stripping ratio analytics, equipment tracking |
| **Data Analyst** | `ANA-315` | Cross-document conflict resolution, OCR accuracy scoring, data reconciliation |
| **Reporting Officer** | `REP-402` | Automated Ministry query responses, parliamentary briefings, PDF exports |
| **Viewer** | `VIEW-501` | Read-only inspection of validated intelligence and approved mining reports |

*Default Password for all demo accounts:* `oresight2026`

---

## 🛠️ Technology Stack

- **Frontend**: React 18, Vite, TypeScript, Tailwind CSS, Lucide React Icons, Recharts / Chart.js
- **Backend**: Python 3.11+, FastAPI / Flask REST APIs, Pydantic, PyMuPDF (fitz), PaddleOCR / Tesseract
- **AI & RAG**: Sentence Transformers (`all-MiniLM-L6-v2`), BERTopic semantic topic modeling, Vector Cosine Search
- **Database**: PostgreSQL 16 with `pgvector` extension
- **Deployment**: Docker, Docker Compose, Windows & Linux native runners

---

## ⚡ Instant Quick Start

### Option 1: Zero-Dependency Local Runner (Immediate Launch)
You can launch the full OreSight web application and REST API server immediately using Python:

```bash
cd oresight
python run_app.py
```
Open your browser at: **`http://127.0.0.1:8000`**

### Option 2: Docker Compose Deployment
```bash
docker-compose up --build
```
- Frontend UI: `http://localhost:3000`
- Backend REST API & Swagger Docs: `http://localhost:8000/docs`
- PostgreSQL & pgvector: `localhost:5432`

---

## 🎯 Smart India Hackathon 2026 Targets (Pilot Metrics)
- **70–80%** reduction in manual report preparation time
- **95%+** extraction and unit normalization accuracy
- **80%+** repetitive geological document workflow automation
- High-level multi-document queries answered in **< 3 seconds** with page citations
