from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    user_id: UUID
    project_id: UUID
    feedback: str
    rating: int

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdate(BaseModel):
    user_id: Optional[UUID] = None
    project_id: Optional[UUID] = None
    feedback: Optional[str] = None
    rating: Optional[int] = None

class FeedbackResponse(FeedbackBase):
    id: UUID
    creation_date: datetime

    class Config:
        orm_mode = True

class FeedbackListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    feedbacks: list[FeedbackResponse]

    class Config:
        orm_mode = True
