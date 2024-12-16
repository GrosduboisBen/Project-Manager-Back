from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import List

# Schéma de base pour les utilisateurs
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schéma pour créer un utilisateur
class UserCreate(UserBase):
    password: str

# Schéma pour mettre à jour un utilisateur
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    active: bool | None = None

# Schéma pour renvoyer un utilisateur
class UserResponse(UserBase):
    id: UUID
    creation_date: datetime
    last_login_date: datetime | None
    active: bool
    role_id: UUID

    class Config:
        orm_mode = True

# Schéma pour une liste d'utilisateurs avec pagination
class UserListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    users: List[UserResponse]

    class Config:
        orm_mode = True
