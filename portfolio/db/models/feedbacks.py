from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base

class UserFeedback(Base):
    __tablename__ = "user_feedback"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    feedback = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False)

    user = relationship("User", back_populates="feedbacks")
    project = relationship("Project", back_populates="feedbacks")
