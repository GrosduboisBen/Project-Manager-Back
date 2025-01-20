from pydantic import BaseModel
from uuid import UUID

class InvoiceHasCustomBlockBase(BaseModel):
    invoice_id: UUID
    custom_block_id: UUID

class InvoiceHasCustomBlockCreate(InvoiceHasCustomBlockBase):
    pass

class InvoiceHasCustomBlockResponse(InvoiceHasCustomBlockBase):
    class Config:
        orm_mode = True

class InvoiceHasCustomBlockListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    invoiceHasCustomBlocks: list[InvoiceHasCustomBlockResponse]

    class Config:
        orm_mode = True