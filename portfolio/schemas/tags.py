from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    name: Optional[str] = None

class TagResponse(TagBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class TagListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    tags: list[TagResponse]

    class Config:
        orm_mode = True
