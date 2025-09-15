
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional
from datetime import datetime


class UserRole(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    username: str
    name: str
    surname: str
    email: EmailStr
    role: UserRole = UserRole.user
    disabled: bool = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[UserRole] = None
    email: Optional[EmailStr] = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True    

class UserLogin(BaseModel):
    username: str
    password: str