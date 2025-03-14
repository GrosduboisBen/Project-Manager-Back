from sqlalchemy import Column, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from portfolio.db.base_class import Base
import uuid
from datetime import datetime,timezone

class Technology(Base):
    __tablename__ = "technologies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    language = Column(String, nullable=False)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.id"))
    creation_date = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))

    tag = relationship("Tag", back_populates="technologies")
    missions = relationship("Mission", back_populates="technology")
