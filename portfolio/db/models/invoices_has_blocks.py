from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship
from portfolio.db.base_class import Base
import uuid

class InvoiceHasCustomBlock(Base):
    __tablename__ = "invoice_has_custom_block"

    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), primary_key=True)
    custom_block_id = Column(UUID(as_uuid=True), ForeignKey("custom_blocks.id"), primary_key=True)

    invoice = relationship("Invoice", back_populates="custom_blocks")
    custom_block = relationship("CustomBlock")
