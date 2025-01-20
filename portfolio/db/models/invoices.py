from sqlalchemy import Column, String, Enum, UUID, ForeignKey, Date
from sqlalchemy.orm import relationship
from portfolio.db.base_class import Base
from datetime import datetime,timezone
import uuid

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    reference = Column(String, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    validation_status = Column(Enum("draft", "sent", "validated", "rejected", "in_edition", name="invoice_statuses"), nullable=False)
    updated_at = Column(Date)

    user = relationship("User", back_populates="invoices")
    project = relationship("Project", back_populates="invoices")
    invoice_infos = relationship("InvoiceInfo", back_populates="invoice", uselist=False)
    custom_blocks = relationship("InvoiceHasCustomBlock", back_populates="invoice")
