# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from app import models
from app.user import create_user
from app.schemas import UserCreate, UserResponse, TaskResponse, TaskUpdate, TaskCreate, LoginRequest,TokenResponse
from app.core.security import get_current_user
from app.services.auth_service import login_user
from app.services.task_service import (
    create_task as create_task_service,
    update_task as update_task_service,
    delete_task as delete_task_service,
    get_all_tasks
)
from app.services.user_service import get_all_users

router = APIRouter()

@router.post("/users", response_model=UserResponse, status_code=201)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(db, data.email, data.password)
    return {"access_token": token}


@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task_route(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return create_task_service(db, task)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return get_all_tasks(db)


@router.put("/tasks/{task_id}")
def update_task_route(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    task = update_task_service(db, task_id, task_update)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.delete("/tasks/{task_id}")
def delete_task_route(
    task_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    deleted = delete_task_service(db, task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}