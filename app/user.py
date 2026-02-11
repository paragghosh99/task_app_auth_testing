from sqlalchemy.orm import Session
from app.models import User
from app.core.security import hash_password
from app.schemas import UserCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_pw = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed_pw
    )

    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    db.refresh(user)
    return user
