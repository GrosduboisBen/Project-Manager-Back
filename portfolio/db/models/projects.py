from sqlalchemy import Column, String, Text, Enum, DECIMAL, TIMESTAMP, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum("proposed", "in_progress", "over", "canceled", name="project_statuses"), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    client_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    total_price = Column(DECIMAL)
    
    milestones = relationship("Milestone", back_populates="project")
    feedbacks = relationship("UserFeedback", back_populates="project")
