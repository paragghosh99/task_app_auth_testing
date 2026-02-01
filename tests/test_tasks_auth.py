from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings
from app.core.security import create_access_token

def auth_header(token: str):
    return {"Authorization": f"Bearer {token}"}


def test_tasks_without_token_returns_401(client):
    assert client.get("/tasks").status_code == 401


def test_tasks_with_malformed_token_returns_401(client):
    assert client.get("/tasks", headers=auth_header("abc.def.ghi")).status_code == 401


def test_tasks_with_invalid_signature_returns_401(client):
    fake_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJ1c2VyX2lkIjoxLCJleHAiOjE5OTk5OTk5OTl9."
        "invalidsignature"
    )
    assert client.get("/tasks", headers=auth_header(fake_token)).status_code == 401


def test_tasks_with_expired_token_returns_401(client):
    expired_payload = {
        "sub": "1",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=1)
    }

    expired_token = jwt.encode(
        expired_payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    assert client.get("/tasks", headers=auth_header(expired_token)).status_code == 401


def test_tasks_with_valid_token_succeeds(client):
    token = create_access_token(user_id=1)
    assert client.get("/tasks", headers=auth_header(token)).status_code == 200
