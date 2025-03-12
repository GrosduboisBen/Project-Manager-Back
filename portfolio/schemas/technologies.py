from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class TechnologyBase(BaseModel):
    name: str
    description: str
    tag_id: UUID
    language: str

class TechnologyCreate(TechnologyBase):
    pass

class TechnologyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    tag_id: Optional[UUID] = None
    language: Optional[str] = None

class TechnologyResponse(TechnologyBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class TechnologyListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    technologies: list[TechnologyResponse]

    class Config:
        orm_mode = True
