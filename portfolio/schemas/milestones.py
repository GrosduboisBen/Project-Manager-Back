from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class MilestoneBase(BaseModel):
    project_id: UUID
    title: str
    description: str

class MilestoneCreate(MilestoneBase):
    pass

class MilestoneUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    project_id: Optional[UUID] = None

class MilestoneResponse(MilestoneBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class MilestoneListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    milestones: list[MilestoneResponse]

    class Config:
        orm_mode = True
