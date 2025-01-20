from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
import uuid
from portfolio.db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))
    last_login_date = Column(TIMESTAMP, nullable=True)
    active = Column(Boolean, default=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=True)
    
    role = relationship("Role", back_populates="users")  # If Role has users relationship
    availability_calendar = relationship("AvailabilityCalendar", back_populates="user")
    feedbacks = relationship("UserFeedback", back_populates="user")
    pricing = relationship("Pricing", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")

