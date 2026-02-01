# app/services/db_utils.py

from fastapi import HTTPException
from sqlalchemy.orm import Session

def commit_or_500(db: Session):
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
