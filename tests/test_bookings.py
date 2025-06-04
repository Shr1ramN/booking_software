from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_book_class_success():
    # Make sure class_id exists in DB
    response = client.post("/book/", json={
        "class_id": 1,
        "client_name": "Shriram",
        "client_email": "shriram@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["client_email"] == "shriram@example.com"
    assert "id" in data

def test_book_class_invalid_email():
    response = client.post("/book/", json={
        "class_id": 1,
        "client_name": "Shriram",
        "client_email": "not-an-email"
    })
    assert response.status_code == 422
