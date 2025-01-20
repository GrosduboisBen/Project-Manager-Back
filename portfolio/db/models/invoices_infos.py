from sqlalchemy import Column, String, UUID, ForeignKey, Date
from sqlalchemy.orm import relationship
from portfolio.db.base_class import Base
import uuid

class InvoiceInfo(Base):
    __tablename__ = "invoice_infos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"), nullable=False)
    client_name = Column(String, nullable=False)
    creation_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=False)
    client_address = Column(String, nullable=False)
    deposit_price = Column(String, nullable=False)

    invoice = relationship("Invoice", back_populates="invoice_infos")
