from fastapi.testclient import TestClient

from visby.main import app

client = TestClient(app)


def test_create_measurement() -> None:
    data = {
        "type": "weight",
        "value": 10.0,
        "user_id": 1,
        "created_at": "2024-04-14T19:04:04.454000",
    }
    response_data = {
        "type": "weight",
        "value": 10.0,
        "user_id": 1,
        "created_at": "2024-04-14T00:00:00",
        "measurement_id": 1,
    }
    response = client.post("/api/measurements/", json=data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_create_measurement_non_existing_user_id() -> None:
    pass


def test_create_measurement_empty_created_at() -> None:
    pass


def test_read_measurements() -> None:
    expected_data = {
        "type": "weight",
        "value": 10.0,
        "user_id": 1,
        "created_at": "2024-04-14T00:00:00",
        "measurement_id": 1,
    }
    response = client.get("/api/measurements/")
    assert response.status_code == 200
    assert response.json() == [expected_data]


def test_read_measurement() -> None:
    expected_data = {
        "type": "weight",
        "value": 10.0,
        "user_id": 1,
        "created_at": "2024-04-14T00:00:00",
        "measurement_id": 1,
    }
    response = client.get("/api/measurements/?measurement_id=1")
    assert response.status_code == 200
    assert response.json() == [expected_data]


def test_delete_measurement() -> None:
    expected_data = {
        "type": "weight",
        "value": 10.0,
        "user_id": 1,
        "created_at": "2024-04-14T00:00:00",
        "measurement_id": 1,
    }
    response = client.delete("/api/measurements/1")
    assert response.status_code == 200
    assert response.json() == expected_data
