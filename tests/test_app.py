from fastapi.testclient import TestClient

from app.main import PROJECT_NAME, app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["project"] == PROJECT_NAME


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_demo_stub():
    response = client.post(
        "/api/v1/demo",
        json={"text": "Сделайте логотип меньше и замените цвет кнопки."},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "stub"
    assert data["extracted_edits"] == []
