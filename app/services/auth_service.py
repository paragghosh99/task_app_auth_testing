# app/services/auth_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from app.core.security import verify_password, create_access_token

def login_user(db: Session, email: str, password: str) -> str:
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return create_access_token(user.id)
