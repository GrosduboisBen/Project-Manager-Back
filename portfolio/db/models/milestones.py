from sqlalchemy import Column, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from datetime import datetime,timezone

class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    creation_date = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc))

    project = relationship("Project", back_populates="milestones")
    missions = relationship("Mission", back_populates="milestone")
