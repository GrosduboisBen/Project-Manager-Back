from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class PricingBase(BaseModel):
    tag_id: UUID
    user_id: UUID  # New field
    price_per_day: float

class PricingCreate(PricingBase):
    pass

class PricingUpdate(BaseModel):
    tag_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    price_per_day: Optional[float] = None

class PricingResponse(PricingBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class PricingListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    pricing: list[PricingResponse]

    class Config:
        orm_mode = True
