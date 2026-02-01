from app.user import create_user
from app.schemas import UserCreate

def test_password_is_hashed(db_session):
    user_in = UserCreate(email="hash@test.com", password="plain123")
    user = create_user(db_session, user_in)

    assert user.hashed_password != "plain123"
    assert user.email == "hash@test.com"
