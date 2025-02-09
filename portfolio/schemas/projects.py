from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional
from portfolio.db.models.projects import ProjectStatusEnum


class ProjectBase(BaseModel):
    title: str
    description: str
    status: ProjectStatusEnum
    start_date: Optional[date]
    end_date: Optional[date]
    total_price: Optional[float]
    tax_rate: Optional[float]

class ProjectCreate(ProjectBase):
    client_id: UUID

class ProjectUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[ProjectStatusEnum]
    start_date: Optional[date]
    end_date: Optional[date]
    total_price: Optional[float]
    client_id: Optional[UUID]
    tax_rate: Optional[float]


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
