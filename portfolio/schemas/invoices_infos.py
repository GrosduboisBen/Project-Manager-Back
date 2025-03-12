from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class InvoiceInfoBase(BaseModel):
    invoice_id: UUID
    client_name: str
    creation_date: datetime
    expiry_date: datetime
    client_address: str
    deposit_price: float

class InvoiceInfoCreate(InvoiceInfoBase):
    pass

class InvoiceInfoUpdate(BaseModel):
    client_name: Optional[str] = None
    creation_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    client_address: Optional[str] = None
    deposit_price: Optional[float] = None

class InvoiceInfoResponse(InvoiceInfoBase):
    id: UUID

    class Config:
        orm_mode = True

class InvoiceInfoListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    invoices: list[InvoiceInfoResponse]

    class Config:
        orm_mode = True