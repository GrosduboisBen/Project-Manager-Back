from sqlalchemy import Column, String, UUID
from portfolio.db.base_class import Base
import uuid


class CustomBlock(Base):
    __tablename__ = "custom_blocks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
