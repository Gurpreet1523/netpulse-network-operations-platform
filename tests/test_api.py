from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_devices_returns_seeded_devices():
    response = client.get("/api/v1/devices")
    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 2
    assert all("id" in device and "management_ip" in device for device in body)


def test_get_existing_device():
    response = client.get("/api/v1/devices/dev-router-001")
    assert response.status_code == 200
    assert response.json()["device_type"] == "router"


def test_unknown_device_returns_404():
    response = client.get("/api/v1/devices/not-a-real-device")
    assert response.status_code == 404
    assert response.json()["detail"] == "Device not found"


def test_create_device_rejects_duplicate_management_ip():
    response = client.post("/api/v1/devices", json={
        "name": "duplicate-router",
        "management_ip": "192.0.2.10",
        "device_type": "router",
        "site": "lab-west"
    })
    assert response.status_code == 409


def test_create_device_rejects_invalid_ip():
    response = client.post("/api/v1/devices", json={
        "name": "invalid-router",
        "management_ip": "not-an-ip",
        "device_type": "router",
        "site": "lab-west"
    })
    assert response.status_code == 422


def test_interfaces_for_existing_device():
    response = client.get("/api/v1/devices/dev-router-001/interfaces")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_interfaces_for_unknown_device_returns_404():
    response = client.get("/api/v1/devices/unknown/interfaces")
    assert response.status_code == 404
