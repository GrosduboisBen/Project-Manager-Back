from sqlalchemy import Column, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from db.base_class import Base

class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    price_per_day = Column(DECIMAL, nullable=False)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.id"), nullable=False)

    tag = relationship("Tag", back_populates="pricing")
