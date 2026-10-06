-- ==============================================================================
-- OreSight: AI-Powered Geological, Mining & Reporting Intelligence Platform
-- Smart India Hackathon 2026 - Problem Statement: SIH26023
-- Target Organizations: CMPDI / Coal India Limited (CIL) Subsidiaries
-- Database: PostgreSQL 15+ with pgvector extension
-- Philosophy: "Every number is traceable."
-- ==============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "vector";

-- -----------------------------------------------------------------------------
-- 1. ROLES & USERS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    permissions JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    employee_id VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    organization VARCHAR(100) DEFAULT 'CMPDI / Coal India Limited',
    subsidiary VARCHAR(50) DEFAULT 'HQ Ranchi', -- ECL, BCCL, CCL, WCL, SECL, MCL, NCL, CMPDI
    department VARCHAR(100) NOT NULL, -- Geology, Mining Operations, Quality Control, Planning, IT
    role_id INTEGER REFERENCES roles(id) ON DELETE RESTRICT,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 2. DOCUMENTS & PAGES
-- -----------------------------------------------------------------------------
CREATE TYPE document_status AS ENUM (
    'Uploaded',
    'Processing',
    'OCR Completed',
    'Data Extracted',
    'Validation Required',
    'Validated',
    'Failed'
);

CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    file_size_bytes BIGINT NOT NULL,
    file_type VARCHAR(50) NOT NULL, -- PDF, DOCX, XLSX, CSV, JPG, PNG
    mime_type VARCHAR(100),
    page_count INTEGER DEFAULT 1,
    status document_status DEFAULT 'Uploaded',
    ocr_status VARCHAR(50) DEFAULT 'Pending',
    validation_status VARCHAR(50) DEFAULT 'Pending',
    uploaded_by UUID REFERENCES users(id) ON DELETE SET NULL,
    subsidiary VARCHAR(50) NOT NULL,
    mine_unit VARCHAR(100),
    document_category VARCHAR(100), -- Annual Report, Geological Survey, Borehole Log, Coal Quality, Production Log
    reporting_period VARCHAR(50), -- e.g. FY 2024-25, Q3 2025
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS document_pages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER NOT NULL,
    page_text TEXT,
    page_image_path VARCHAR(500),
    ocr_confidence NUMERIC(5,2),
    raw_ocr_data JSONB, -- Coordinates, words, bounding boxes
    embedding vector(768), -- For dense semantic retrieval
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_doc_page UNIQUE (document_id, page_number)
);

-- -----------------------------------------------------------------------------
-- 3. EXTRACTED DATA, TABLES & ENTITIES (TRACEABILITY CORE)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS extracted_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER NOT NULL,
    parameter_name VARCHAR(150) NOT NULL, -- e.g. Annual Coal Production, Seam XIV Thickness, Gross Calorific Value (GCV)
    category VARCHAR(100) NOT NULL, -- Production, Geology, Coal Quality, Reserves, Financial
    raw_value VARCHAR(150) NOT NULL, -- As extracted e.g. "1.245 MT" or "12.45 Lakh Tonnes"
    normalized_value NUMERIC(18,4), -- 1245000.00
    normalized_unit VARCHAR(50), -- Tonnes, Metres, kcal/kg, %
    confidence NUMERIC(5,2) NOT NULL, -- 97.4
    bounding_box JSONB, -- {"x0": 120, "y0": 340, "x1": 450, "y1": 390}
    source_table VARCHAR(150), -- Table 4: Production Summary
    source_snippet TEXT,
    validation_state VARCHAR(50) DEFAULT 'Pending', -- Validated, Needs Review, Conflict Detected
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tables (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER NOT NULL,
    table_index INTEGER NOT NULL,
    table_title VARCHAR(255),
    headers JSONB NOT NULL,
    rows JSONB NOT NULL,
    bounding_box JSONB,
    confidence NUMERIC(5,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS entities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER NOT NULL,
    entity_type VARCHAR(50) NOT NULL, -- MINE, SEAM, BOREHOLE, COAL_GRADE, COMPANY, DATE
    entity_text VARCHAR(255) NOT NULL,
    normalized_text VARCHAR(255),
    confidence NUMERIC(5,2),
    bounding_box JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 4. VALIDATION RESULTS & CONFLICT DETECTION
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS validation_results (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    rule_name VARCHAR(100) NOT NULL,
    rule_category VARCHAR(50) NOT NULL, -- Numeric, Unit Consistency, Date Consistency, Duplicate, Historical Trend
    status VARCHAR(50) NOT NULL, -- Passed, Warning, Failed
    message TEXT NOT NULL,
    details JSONB,
    executed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS validation_conflicts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conflict_title VARCHAR(255) NOT NULL,
    parameter_name VARCHAR(150) NOT NULL,
    mine_unit VARCHAR(100),
    period VARCHAR(50),
    doc_a_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    doc_a_page INTEGER NOT NULL,
    doc_a_value VARCHAR(150) NOT NULL,
    doc_a_normalized NUMERIC(18,4),
    doc_b_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    doc_b_page INTEGER NOT NULL,
    doc_b_value VARCHAR(150) NOT NULL,
    doc_b_normalized NUMERIC(18,4),
    discrepancy_percentage NUMERIC(6,2),
    status VARCHAR(50) DEFAULT 'Conflict Detected', -- Conflict Detected, Accepted A, Accepted B, Human Verified, Dismissed
    resolution_notes TEXT,
    resolved_by UUID REFERENCES users(id) ON DELETE SET NULL,
    resolved_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 5. AI QUERIES, RAG & EVIDENCE CITATIONS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS queries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    query_text TEXT NOT NULL,
    answer_text TEXT NOT NULL,
    confidence NUMERIC(5,2),
    is_sufficient_evidence BOOLEAN DEFAULT TRUE,
    execution_time_ms INTEGER,
    pipeline_steps JSONB, -- {"semantic_search_ms": 42, "evidence_extraction_ms": 68, "llm_synthesis_ms": 310}
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS query_sources (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    query_id UUID NOT NULL REFERENCES queries(id) ON DELETE CASCADE,
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER NOT NULL,
    citation_label VARCHAR(100), -- [Source: Production_Report_2025.pdf, Page 18]
    table_reference VARCHAR(150),
    evidence_snippet TEXT NOT NULL,
    relevance_score NUMERIC(5,4),
    extracted_value VARCHAR(150),
    validation_status VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 6. TOPICS & WORD CLOUD (BERTopic MODELING)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL, -- Geology, Production, Quality, Safety, Environment, Equipment
    keywords JSONB NOT NULL, -- ["overburden", "stripping ratio", "dragline", "ROM"]
    document_count INTEGER DEFAULT 0,
    frequency_score NUMERIC(6,2) DEFAULT 0,
    yearly_trend JSONB DEFAULT '{}'::jsonb, -- {"2022": 45, "2023": 72, "2024": 94, "2025": 112}
    subsidiary_distribution JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 7. AUTOMATED REPORTS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_title VARCHAR(255) NOT NULL,
    report_type VARCHAR(100) NOT NULL, -- Production Report, Geological Report, Mining Summary, Coal Quality, Ministry Query
    template_name VARCHAR(100) NOT NULL,
    subsidiary VARCHAR(50),
    mine_unit VARCHAR(100),
    date_range VARCHAR(100),
    content_json JSONB NOT NULL,
    pdf_export_path VARCHAR(500),
    docx_export_path VARCHAR(500),
    citation_count INTEGER DEFAULT 0,
    generated_by UUID REFERENCES users(id) ON DELETE SET NULL,
    validation_passed BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 8. AUDIT TRAIL
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    user_name VARCHAR(150) NOT NULL,
    user_role VARCHAR(50) NOT NULL,
    action VARCHAR(150) NOT NULL, -- "Updated production value", "Resolved validation conflict", "Uploaded geological log"
    document_id UUID REFERENCES documents(id) ON DELETE SET NULL,
    document_title VARCHAR(255),
    page_number INTEGER,
    field_name VARCHAR(100),
    old_value TEXT,
    new_value TEXT,
    validation_status VARCHAR(50),
    ip_address VARCHAR(45),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- INDEXES FOR FAST ENTERPRISE SEARCH & TRACEABILITY
-- -----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_docs_status ON documents(status);
CREATE INDEX IF NOT EXISTS idx_docs_subsidiary ON documents(subsidiary);
CREATE INDEX IF NOT EXISTS idx_docs_mine ON documents(mine_unit);
CREATE INDEX IF NOT EXISTS idx_extracted_param ON extracted_data(parameter_name);
CREATE INDEX IF NOT EXISTS idx_extracted_doc_page ON extracted_data(document_id, page_number);
CREATE INDEX IF NOT EXISTS idx_extracted_val_state ON extracted_data(validation_state);
CREATE INDEX IF NOT EXISTS idx_audit_created ON audit_logs(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_audit_action ON audit_logs(action);
CREATE INDEX IF NOT EXISTS idx_conflicts_status ON validation_conflicts(status);

-- -----------------------------------------------------------------------------
-- SEED INITIAL ROLES
-- -----------------------------------------------------------------------------
INSERT INTO roles (name, description, permissions) VALUES
('Administrator', 'System wide access, user management, audit trails, pipeline config', '["all"]'::jsonb),
('Geologist', 'Access to borehole, seam, exploration reports, lithology extractions', '["documents.view", "documents.upload", "geology.edit", "validation.review", "query.ask", "reports.generate"]'::jsonb),
('Mining Engineer', 'Access to production data, overburden, dragline, mine-wise analytics', '["documents.view", "documents.upload", "production.edit", "validation.review", "query.ask", "reports.generate"]'::jsonb),
('Data Analyst', 'Analytics, trend visualization, OCR review, statistical cross-checking', '["documents.view", "analytics.view", "validation.review", "query.ask", "reports.export"]'::jsonb),
('Reporting Officer', 'Report compilation, Ministry/Parliamentary query synthesis, citations', '["documents.view", "reports.create", "reports.generate", "reports.export", "query.ask"]'::jsonb),
('Viewer', 'Read-only access to validated documents and published mining summaries', '["documents.view", "reports.view", "query.ask"]'::jsonb)
ON CONFLICT (name) DO NOTHING;
