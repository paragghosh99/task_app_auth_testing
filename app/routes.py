# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import models, schemas

router = APIRouter()

@router.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)

    try:
        db.commit()          # WRITE happens here
        db.refresh(new_task)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return new_task


@router.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    try:
        tasks = db.query(models.Task).all()   # READ happens here
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")

    return tasks


@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    # 1. Fetch
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    # 2. Not found
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # 3. Apply partial updates
    update_data = task_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    # 4. Persist
    db.commit()
    db.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}

