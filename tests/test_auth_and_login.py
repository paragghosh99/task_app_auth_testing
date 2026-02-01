from app.core.security import hash_password
from app import models

def test_login_invalid_email(client, db_session):
    response = client.post("/login", json={
        "email": "nope@test.com",
        "password": "whatever"
    })
    assert response.status_code == 401


def test_login_invalid_password(client, db_session):
    user = models.User(
        email="user@test.com",
        hashed_password=hash_password("correct")
    )
    db_session.add(user)
    db_session.commit()

    response = client.post("/login", json={
        "email": "user@test.com",
        "password": "wrong"
    })
    assert response.status_code == 401


def test_login_success(client, db_session):
    user = models.User(
        email="user@test.com",
        hashed_password=hash_password("correct")
    )
    db_session.add(user)
    db_session.commit()

    response = client.post("/login", json={
        "email": "user@test.com",
        "password": "correct"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
