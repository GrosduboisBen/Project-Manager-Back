from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from datetime import datetime,timezone

class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))

    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", back_populates="role")
