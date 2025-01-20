from sqlalchemy import Column, Date, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base

class AvailabilityCalendar(Base):
    __tablename__ = "availability_calendar"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    availability_date = Column(Date, nullable=False)
    status = Column(Enum("available", "busy", name="availability_statuses"), nullable=False)
    note = Column(Text)

    user = relationship("User", back_populates="availability_calendar")

