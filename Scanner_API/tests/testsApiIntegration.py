from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_audit_integration():
    response = client.post("/audit/start")

    assert response.status_code == 200
    data = response.json()

    assert "health_score" in data
    assert "devices" in data
    assert isinstance(data["devices"], list)
    assert 0 <= data["health_score"] <= 100