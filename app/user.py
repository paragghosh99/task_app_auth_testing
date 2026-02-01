from sqlalchemy.orm import Session
from app.models import User
from app.core.security import hash_password
from app.schemas import UserCreate
from app.services.db_utils import commit_or_500


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_pw = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed_pw
    )

    db.add(user)
    commit_or_500(db)
    db.refresh(user)
    return user
