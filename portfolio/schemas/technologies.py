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
    name: Optional[str]
    description: Optional[str]
    tag_id: Optional[UUID]
    language: Optional[str]

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
