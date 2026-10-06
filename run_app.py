"""
OreSight: AI-Powered Geological, Mining & Reporting Intelligence Platform
Zero-Dependency Unified Server & Application Runner
Compatible with Python 3.10+ and Flask (pre-installed).

Serves:
1. All REST APIs (/api/...) identically to the FastAPI architecture
2. The complete, responsive, enterprise OreSight UI with live traceability,
   interactive 3-pane document viewer, conflict resolution, RAG AI query,
   topic explorer, automated report generation, and system analytics.
"""

import sys
import os
import json
from flask import Flask, request, jsonify, send_from_directory, render_template_string

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend.app.services.document_service import document_service
from backend.app.ai.rag_engine import rag_engine
from backend.app.ai.topic_model import topic_engine
from backend.app.validation.engine import validation_engine
from backend.app.services.mock_data import DEMO_USERS

app = Flask(__name__, static_folder='static')

# -----------------------------------------------------------------------------
# REST API ENDPOINTS
# -----------------------------------------------------------------------------

@app.route('/api/auth/login', methods=['POST'])
def api_login():
    data = request.get_json(silent=True) or {}
    emp_id = data.get('employee_id', '').strip().lower()
    user = next((u for u in DEMO_USERS if u['employee_id'].lower() == emp_id), DEMO_USERS[0])
    return jsonify({
        "status": "success",
        "user": user,
        "token": f"oresight-jwt-{user['employee_id']}",
        "message": f"Welcome back, {user['full_name']} ({user['role']})"
    })

@app.route('/api/auth/users', methods=['GET'])
def api_users():
    return jsonify(DEMO_USERS)

@app.route('/api/documents', methods=['GET'])
def api_documents():
    subsidiary = request.args.get('subsidiary')
    status = request.args.get('status')
    return jsonify(document_service.get_documents(subsidiary, status))

@app.route('/api/documents/<doc_id>', methods=['GET'])
def api_document(doc_id):
    doc = document_service.get_document_by_id(doc_id)
    if not doc:
        return jsonify({"error": "Document not found"}), 404
    return jsonify(doc)

@app.route('/api/documents/upload', methods=['POST'])
def api_upload():
    # Handle form or JSON
    data = request.form if request.form else (request.get_json(silent=True) or {})
    file_name = data.get('file_name', 'Uploaded_Geological_Report.pdf')
    file_type = data.get('file_type', 'PDF')
    file_size = data.get('file_size', '3.8 MB')
    subsidiary = data.get('subsidiary', 'SECL')
    mine_unit = data.get('mine_unit', 'Gevra OC')
    department = data.get('department', 'Mining Operations')
    category = data.get('category', 'Annual Production Report')

    new_doc = document_service.add_document(
        file_name=file_name,
        file_type=file_type,
        file_size=file_size,
        subsidiary=subsidiary,
        mine_unit=mine_unit,
        department=department,
        category=category
    )
    return jsonify(new_doc)

@app.route('/api/documents/<doc_id>/process', methods=['POST'])
def api_process(doc_id):
    try:
        updated = document_service.process_document(doc_id)
        return jsonify({
            "status": "success",
            "message": f"6-Stage Pipeline processed {updated['file_name']}",
            "document": updated
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/documents/<doc_id>/extractions', methods=['GET'])
def api_doc_extractions(doc_id):
    return jsonify(document_service.get_extractions(doc_id))

@app.route('/api/validation/extractions', methods=['GET'])
def api_all_extractions():
    doc_id = request.args.get('doc_id')
    return jsonify(document_service.get_extractions(doc_id))

@app.route('/api/validation/conflicts', methods=['GET'])
def api_conflicts():
    return jsonify(document_service.get_conflicts())

@app.route('/api/validation/resolve', methods=['POST'])
def api_resolve_conflict():
    data = request.get_json(silent=True) or {}
    conflict_id = data.get('conflict_id')
    action = data.get('action', 'ACCEPT_A')
    resolved_by = data.get('resolved_by', 'Dr. Rajesh Sharma')
    notes = data.get('notes')
    try:
        updated = document_service.resolve_conflict(conflict_id, action, resolved_by, notes)
        return jsonify({"status": "success", "conflict": updated})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/validation/run', methods=['POST'])
def api_run_validation():
    extractions = document_service.get_extractions()
    conflicts = validation_engine.detect_conflicts(extractions)
    return jsonify({
        "status": "success",
        "message": f"Cross-document validation sweep executed across {len(extractions)} extracted data points.",
        "conflicts_detected": len(conflicts),
        "total_active_conflicts": len(document_service.get_conflicts())
    })

@app.route('/api/query', methods=['POST'])
def api_query():
    data = request.get_json(silent=True) or {}
    user_query = data.get('query', '')
    res = rag_engine.query(user_query)
    return jsonify(res)

@app.route('/api/query/suggestions', methods=['GET'])
def api_query_suggestions():
    return jsonify([
        "What was the annual coal production in 2025 across SECL mines?",
        "Compare production between 2024 and 2025 for Gevra and Kusmunda.",
        "Which mines showed production decline or stripping ratio anomaly?",
        "What are the recurring geological topics in the Jharia basin reports?",
        "Show documents containing information about coal quality Grade G11-G13.",
        "What are the major findings in the latest geological survey?"
    ])

@app.route('/api/reports', methods=['GET'])
def api_reports():
    return jsonify(document_service.get_reports())

@app.route('/api/reports/<report_id>', methods=['GET'])
def api_get_report(report_id):
    reps = document_service.get_reports()
    for r in reps:
        if r["id"] == report_id:
            return jsonify(r)
    return jsonify({"error": "Report not found"}), 404

@app.route('/api/reports/generate', methods=['POST'])
def api_generate_report():
    data = request.get_json(silent=True) or {}
    report_type = data.get('report_type', 'Ministry/Parliamentary Query Response')
    template = data.get('template', 'CMPDI Official Briefing Template')
    subsidiary = data.get('subsidiary', 'SECL')
    mine_unit = data.get('mine_unit', 'Gevra Mega OC')
    date_range = data.get('date_range', 'FY 2024-25 to 2025-26')
    data_sources = data.get('data_sources', ['Production_Report_2025.pdf', 'Geological_Survey_2025.pdf'])

    new_rep = document_service.generate_report(
        report_type=report_type,
        template=template,
        subsidiary=subsidiary,
        mine_unit=mine_unit,
        date_range=date_range,
        data_sources=data_sources
    )
    return jsonify(new_rep)

@app.route('/api/reports/templates/all', methods=['GET'])
def api_report_templates():
    return jsonify([
        {"id": "t1", "name": "Ministry/Parliamentary Query Response", "category": "Liaison & Policy"},
        {"id": "t2", "name": "Annual Production & Offtake Summary", "category": "Operations"},
        {"id": "t3", "name": "Geological Seam & Borehole Assessment", "category": "Exploration"},
        {"id": "t4", "name": "Coal Quality & Equilibrated GCV Matrix", "category": "Quality Assurance"},
        {"id": "t5", "name": "Monthly Pithead Stripping Ratio & HEMM Review", "category": "Engineering"}
    ])

@app.route('/api/topics', methods=['GET'])
def api_topics():
    return jsonify(topic_engine.get_all_topics())

@app.route('/api/topics/wordcloud', methods=['GET'])
def api_wordcloud():
    return jsonify(topic_engine.get_word_cloud())

@app.route('/api/topics/<int:topic_id>', methods=['GET'])
def api_topic_detail(topic_id):
    return jsonify(topic_engine.get_topic_by_id(topic_id))

@app.route('/api/analytics', methods=['GET'])
def api_analytics():
    from backend.app.services.analytics_service import get_analytics_data
    return jsonify(get_analytics_data())

@app.route('/api/audit', methods=['GET'])
def api_audit():
    q = request.args.get('q')
    return jsonify(document_service.get_audit_logs(q))

@app.route('/api/system/health', methods=['GET'])
def api_health():
    from backend.app.services.analytics_service import get_health_data
    return jsonify(get_health_data())

# -----------------------------------------------------------------------------
# STATIC FILE & SPA SERVING
# -----------------------------------------------------------------------------
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(os.path.join('static', path)):
        return send_from_directory('static', path)
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"\n=======================================================")
    print(f" OreSight Mining Intelligence Platform (SIH26023)")
    print(f" Central Mine Planning & Design Institute (CMPDI) / CIL")
    print(f" 'Every Number is Traceable'")
    print(f" Server running at: http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host='0.0.0.0', port=port, debug=False)
