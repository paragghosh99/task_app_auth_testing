from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    email: EmailStr
    is_active: bool = Field(default=True)
