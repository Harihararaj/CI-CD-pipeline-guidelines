from fastapi.testclient import TestClient
from src.application import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_add_numbers():
    response = client.get("/add/4/6")
    assert response.status_code == 200
    assert response.json() == {"result": 10}

def test_subtract_numbers():
    response = client.get("/subtract/10/3")
    assert response.status_code == 200
    assert response.json() == {"result": 7}