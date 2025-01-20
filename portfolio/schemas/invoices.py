from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime, date

class InvoiceBase(BaseModel):
    reference: str
    user_id: UUID
    project_id: UUID
    validation_status: str
    updated_at: Optional[date]

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    reference: Optional[str]
    user_id: Optional[UUID]
    project_id: Optional[UUID]
    validation_status: Optional[str]
    updated_at: Optional[date]

class InvoiceResponse(InvoiceBase):
    id: UUID

    class Config:
        orm_mode = True
class InvoiceListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    invoices: list[InvoiceResponse]

    class Config:
        orm_mode = True