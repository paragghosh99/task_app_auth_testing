from app.core.security import create_access_token

def auth():
    token = create_access_token(user_id=1)
    return {"Authorization": f"Bearer {token}"}


def test_create_task_success(client):
    response = client.post(
        "/tasks",
        headers=auth(),
        json={"title": "Task 1", "description": "Desc"}
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Task 1"


def test_get_tasks_returns_data(client):
    response = client.get("/tasks", headers=auth())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
