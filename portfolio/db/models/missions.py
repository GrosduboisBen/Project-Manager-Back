from sqlalchemy import Column, String, DECIMAL, Date, ForeignKey, Enum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from db.base_class import Base

class Mission(Base):
    __tablename__ = "missions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    milestone_id = Column(UUID(as_uuid=True), ForeignKey("milestones.id"), nullable=True)
    technology_id = Column(UUID(as_uuid=True), ForeignKey("technologies.id"), nullable=False)
    start_date = Column(Date)
    due_date = Column(Date, nullable=False)
    estimated_delivery = Column(Date)
    status = Column(Enum("open", "in_progress", "closed", "blocked", name="mission_statuses"), nullable=False)
    estimated_cost = Column(DECIMAL)

    milestone = relationship("Milestone", back_populates="missions")
    technology = relationship("Technology", back_populates="missions")
