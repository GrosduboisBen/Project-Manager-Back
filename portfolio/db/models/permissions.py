from sqlalchemy import Column, String, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from datetime import datetime,timezone

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    creation_date = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))

    role = relationship("Role", back_populates="permissions")