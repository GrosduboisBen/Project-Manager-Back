from sqlalchemy import Column, String, Text, Enum, DECIMAL, TIMESTAMP, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from enum import Enum as PyEnum 

class ProjectStatusEnum(PyEnum):
    PROPOSED = "proposed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
    def __str__(self):
        return self.value 
class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(ProjectStatusEnum,name="project_statuses",values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    client_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    total_price = Column(DECIMAL)
    tax_rate = Column(DECIMAL, nullable=False, default=0.0)

    invoices = relationship("Invoice", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")
    feedbacks = relationship("UserFeedback", back_populates="project")
