from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db.base_class import Base
from sqlalchemy.orm import relationship
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)
    last_login_date = Column(TIMESTAMP)
    active = Column(Boolean, default=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)

    role = relationship("Role", back_populates="users")
    feedbacks = relationship("UserFeedback", back_populates="user")
    availability_calendar = relationship("AvailabilityCalendar", back_populates="user")
