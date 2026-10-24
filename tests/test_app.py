import os

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://test:test@localhost:5432/test",
)

from app.app import app

def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {
        "message": "Python app is running"
    }

def test_db_endpoint_without_database():
    client = app.test_client()

    response = client.get("/db")

    assert response.status_code in (200, 503)
