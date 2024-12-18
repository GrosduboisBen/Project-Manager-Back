from sqlalchemy import Column, String,TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from datetime import datetime,timezone

class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))

    technologies = relationship("Technology", back_populates="tag")
    pricing = relationship("Pricing", back_populates="tag")
