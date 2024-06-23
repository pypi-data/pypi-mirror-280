from fastapi.testclient import TestClient

from visby.main import app

client = TestClient(app)


def test_create_activity() -> None:
    response = client.post("/api/users/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "user_id": 1}
    data = {
        "type": "running",
        "value": 5,
        "duration": "PT30M",
        "user_id": 1,
        "created_at": "2024-04-25T07:01:56.014Z",
    }
    response_data = {
        "type": "running",
        "value": 5.0,
        "duration": "PT30M",
        "user_id": 1,
        "created_at": "2024-04-25T00:00:00",
        "activity_id": 1,
    }
    response = client.post("/api/activities/", json=data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_create_activity_non_existing_user_id() -> None:
    pass


def test_create_activity_empty_created_at() -> None:
    pass


def test_read_activities() -> None:
    expected_data = {
        "type": "running",
        "value": 5.0,
        "duration": "PT30M",
        "user_id": 1,
        "created_at": "2024-04-25T00:00:00",
        "activity_id": 1,
    }
    response = client.get("/api/activities/")
    assert response.status_code == 200
    assert response.json() == [expected_data]


def test_read_activity() -> None:
    expected_data = {
        "type": "running",
        "value": 5.0,
        "duration": "PT30M",
        "user_id": 1,
        "created_at": "2024-04-25T00:00:00",
        "activity_id": 1,
    }
    response = client.get("/api/activities/?activity_id=1")
    assert response.status_code == 200
    assert response.json() == [expected_data]


def test_delete_activity() -> None:
    expected_data = {
        "type": "running",
        "value": 5.0,
        "duration": "PT30M",
        "user_id": 1,
        "created_at": "2024-04-25T00:00:00",
        "activity_id": 1,
    }
    response = client.delete("/api/activities/1")
    assert response.status_code == 200
    assert response.json() == expected_data
