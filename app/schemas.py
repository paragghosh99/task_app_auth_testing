from pydantic import BaseModel
from typing import Optional

# What client sends
class TaskCreate(BaseModel):
    title: str
    description: str

# What client receives
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool

    class Config:
        from_attributes = True

# UPDATE needs optional fields
# Optional fields → enables partial updates
# Presence ≠ overwrite unless explicitly sent
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
