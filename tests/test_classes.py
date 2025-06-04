from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("name" in c for c in data)
    assert all("available_slots" in c for c in data)
    assert all("date" in c and "time" in c for c in data)
