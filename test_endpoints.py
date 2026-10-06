import urllib.request
import json

base = 'http://127.0.0.1:8000'

# 1. Test Root (SPA HTML)
with urllib.request.urlopen(f'{base}/') as response:
    html = response.read().decode('utf-8')
    assert 'OreSight' in html
    print(f'1. UI Root: OK (Length: {len(html)} bytes)')

# 2. Test Documents API
with urllib.request.urlopen(f'{base}/api/documents') as response:
    docs = json.loads(response.read().decode('utf-8'))
    print(f'2. Documents API: OK ({len(docs)} documents returned)')

# 3. Test Conflicts API
with urllib.request.urlopen(f'{base}/api/validation/conflicts') as response:
    confs = json.loads(response.read().decode('utf-8'))
    print(f'3. Conflicts API: OK ({len(confs)} conflicts returned)')

# 4. Test Health API
with urllib.request.urlopen(f'{base}/api/system/health') as response:
    health = json.loads(response.read().decode('utf-8'))
    print(f'4. System Health: OK (Status: {health["status"]}, Services: {len(health["services"])})')

# 5. Test AI Query API
req = urllib.request.Request(
    f'{base}/api/query',
    data=json.dumps({'query': 'What was the annual coal production in 2025 across SECL mines?'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
with urllib.request.urlopen(req) as response:
    res = json.loads(response.read().decode('utf-8'))
    print(f'5. AI Query RAG: OK ({len(res["sources"])} evidence citations, Confidence: {res["confidence"]}%)')

# 6. Test Reports API
with urllib.request.urlopen(f'{base}/api/reports') as response:
    reps = json.loads(response.read().decode('utf-8'))
    print(f'6. Reports API: OK ({len(reps)} reports returned)')

# 7. Test Analytics API
with urllib.request.urlopen(f'{base}/api/analytics') as response:
    ana = json.loads(response.read().decode('utf-8'))
    print(f'7. Analytics API: OK (KPI Accuracy: {ana["kpis"]["extraction_accuracy_pct"]}%)')

print('\n>>> ALL 7 SYSTEM TESTS PASSED SUCCESSFULLY! <<<')
