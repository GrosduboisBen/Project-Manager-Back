from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class PermissionBase(BaseModel):
    role_id: UUID
    name: str
    description: str

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(BaseModel):
    role_id: Optional[UUID]
    name: Optional[str]
    description: Optional[str]

class PermissionResponse(PermissionBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class PermissionListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    permissions: list[PermissionResponse]

    class Config:
        orm_mode = True
