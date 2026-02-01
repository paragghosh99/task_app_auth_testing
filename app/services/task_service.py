# app/services/task_service.py

from sqlalchemy.orm import Session
from app import models
from app.schemas import TaskCreate, TaskUpdate
from app.services.db_utils import commit_or_500

def create_task(db: Session, task_in: TaskCreate) -> models.Task:
    task = models.Task(
        title=task_in.title,
        description=task_in.description
    )
    db.add(task)
    commit_or_500(db)
    db.refresh(task)
    return task


def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return None

    update_data = task_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    commit_or_500(db)
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return False

    db.delete(task)
    commit_or_500(db)
    return True


def get_all_tasks(db: Session):
    return db.query(models.Task).all()
