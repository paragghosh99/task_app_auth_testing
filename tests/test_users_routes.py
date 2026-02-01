def test_register_user(client, db_session):
    response = client.post("/users", json={
        "email": "unique_user@test.com",
        "password": "secret123"
    })

    assert response.status_code == 201
    assert response.json()["email"] == "unique_user@test.com"


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
