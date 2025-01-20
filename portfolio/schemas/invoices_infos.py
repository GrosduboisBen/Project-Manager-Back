from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date

class InvoiceInfoBase(BaseModel):
    invoice_id: UUID
    client_name: str
    creation_date: date
    expiry_date: date
    client_address: str
    deposit_price: float

class InvoiceInfoCreate(InvoiceInfoBase):
    pass

class InvoiceInfoUpdate(BaseModel):
    client_name: Optional[str]
    creation_date: Optional[date]
    expiry_date: Optional[date]
    client_address: Optional[str]
    deposit_price: Optional[float]

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