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
    title: Optional[str]
    description: Optional[str]
    project_id: Optional[UUID]
    milestone_id: Optional[UUID]
    technology_id: Optional[UUID]
    start_date: Optional[date]
    due_date: Optional[date]
    estimated_delivery: Optional[date]
    status: Optional[str]
    estimated_cost: Optional[float]

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
