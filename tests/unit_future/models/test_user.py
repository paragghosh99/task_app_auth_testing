import pytest
from pydantic import ValidationError
from app.not_used_yet.user import User

def test_valid_user_created():
    user = User(email="test@example.com")
    assert user.is_active is True


def test_invalid_email_rejected():
    with pytest.raises(ValidationError):
        User(email="not-an-email")
