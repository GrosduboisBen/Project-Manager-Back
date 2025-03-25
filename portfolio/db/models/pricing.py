from sqlalchemy import Column, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base
from datetime import datetime,timezone

# Add a security to avoid doublon of  user_id <=> tag_id pair of keys.
class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    price_per_day = Column(DECIMAL, nullable=False)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tags.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))

    tag = relationship("Tag", back_populates="pricing")
    user = relationship("User", back_populates="pricing")
