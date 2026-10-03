from fastapi.testclient import TestClient

from app.main import PROJECT_NAME, SERVICE_NAME, VERSION, app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == SERVICE_NAME
    assert data["project"] == PROJECT_NAME
    assert data["version"] == VERSION


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == SERVICE_NAME
    assert data["version"] == VERSION


def test_demo_stub():
    response = client.post(
        "/api/v1/demo",
        json={"text": "Сделайте логотип меньше и замените цвет кнопки."},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "stub"
    assert data["extracted_edits"] == []
    assert data["source_text"] == "Сделайте логотип меньше и замените цвет кнопки."


def test_demo_rejects_empty_text():
    response = client.post(
        "/api/v1/demo",
        json={"text": ""},
    )

    assert response.status_code == 422
