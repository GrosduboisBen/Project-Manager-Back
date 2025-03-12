from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date


class CustomBlockBase(BaseModel):
    title: str
    content: str

class CustomBlockCreate(CustomBlockBase):
    pass

class CustomBlockUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class CustomBlockResponse(CustomBlockBase):
    id: UUID

    class Config:
        orm_mode = True

class CustomBlockListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    customBlocks: list[CustomBlockResponse]

    class Config:
        orm_mode = True