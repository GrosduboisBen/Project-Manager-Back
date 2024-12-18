from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: str
    status: str  # ENUM: "sent", "in_progress", "over", "canceled"
    start_date: Optional[date]
    end_date: Optional[date]
    total_price: Optional[float]

class ProjectCreate(ProjectBase):
    client_id: UUID

class ProjectUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    total_price: Optional[float]
    client_id: Optional[UUID]

class ProjectResponse(ProjectBase):
    id: UUID
    creation_date: datetime
    client_id: UUID

    class Config:
        orm_mode = True

class ProjectListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    projects: list[ProjectResponse]

    class Config:
        orm_mode = True
