from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    active: Optional[bool] = None

class UserResponse(UserBase):
    id: UUID
    creation_date: datetime
    last_login_date: Optional[datetime]
    active: bool
    role_id: Optional[UUID]

class UserListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    users: List[UserResponse]

    class Config:
        orm_mode = True
