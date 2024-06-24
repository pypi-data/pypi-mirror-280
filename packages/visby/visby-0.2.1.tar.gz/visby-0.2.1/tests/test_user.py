from fastapi.testclient import TestClient

from visby.main import app

client = TestClient(app)


def test_create_user() -> None:
    user_data = {"name": "John Doe2"}
    expected_data = {
        "name": "John Doe2",
        "user_id": 2,
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == expected_data


def test_read_users() -> None:
    expected_data = [
        {
            "name": "John Doe",
            "user_id": 1,
        },
        {
            "name": "John Doe2",
            "user_id": 2,
        },
    ]
    response = client.get("/api/users/")
    assert response.status_code == 200
    assert response.json() == expected_data


def test_delete_user() -> None:
    expected_data = {
        "name": "John Doe2",
        "user_id": 2,
    }
    response = client.delete("/api/users/2")
    assert response.status_code == 200
    assert response.json() == expected_data
