from sqlalchemy.orm import Session
from app import models

def get_all_users(db: Session):
    return db.query(models.User).all()
