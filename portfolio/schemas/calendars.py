from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date

class AvailabilityCalendarBase(BaseModel):
    user_id: UUID
    start_date: date
    end_date: date
    status: str
    note: Optional[str]

class AvailabilityCalendarCreate(AvailabilityCalendarBase):
    pass

class AvailabilityCalendarUpdate(BaseModel):
    user_id: Optional[UUID]
    start_date: Optional[date]
    end_date: Optional[date]
    status: Optional[str]
    note: Optional[str]

class AvailabilityCalendarResponse(AvailabilityCalendarBase):
    id: UUID

    class Config:
        orm_mode = True

class AvailabilityCalendarListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    availabilities: list[AvailabilityCalendarResponse]

    class Config:
        orm_mode = True
