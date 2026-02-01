from app.core.security import create_access_token

def auth():
    token = create_access_token(user_id=1)
    return {"Authorization": f"Bearer {token}"}


def test_update_task_not_found(client):
    assert client.put(
        "/tasks/999",
        headers=auth(),
        json={"title": "X"}
    ).status_code == 404


def test_delete_task_not_found(client):
    assert client.delete("/tasks/999", headers=auth()).status_code == 404
