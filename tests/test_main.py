from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_basic():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "number" in data
    assert isinstance(data["number"], int)

def test_add_one():
    before = client.get("/").json()["number"]
    client.post("/add")
    after = client.get("/").json()["number"]
    assert after == before + 1




