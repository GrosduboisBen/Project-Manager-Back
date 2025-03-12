from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    description: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RoleResponse(RoleBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class RoleListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    roles: list[RoleResponse]

    class Config:
        orm_mode = True
