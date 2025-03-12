from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional

class MissionBase(BaseModel):
    title: str
    description: str
    project_id: UUID
    milestone_id: Optional[UUID]
    technology_id: Optional[UUID]
    start_date: Optional[date]
    due_date: Optional[date]
    estimated_delivery: Optional[date]
    status: str  # ENUM: "open", "in_progress", "closed", "blocked"
    estimated_cost: Optional[float]

class MissionCreate(MissionBase):
    pass

class MissionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    project_id: Optional[UUID] = None
    milestone_id: Optional[UUID] = None
    technology_id: Optional[UUID] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    estimated_delivery: Optional[date] = None
    status: Optional[str] = None
    estimated_cost: Optional[float] = None

class MissionResponse(MissionBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class MissionListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    missions: list[MissionResponse]

    class Config:
        orm_mode = True
