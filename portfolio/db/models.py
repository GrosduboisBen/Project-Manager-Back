from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Enum, Text, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from portfolio.db.base_class import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum("admin", "developer", "manager", "client", name="user_roles"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    last_login_at = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)

    # Relationships
    projects = relationship(
        "Project", back_populates="client", foreign_keys="Project.client_id"
    )  # Projects associated with this client (if user is a client)
    managed_projects = relationship(
        "Project", back_populates="admin", foreign_keys="Project.admin_id"
    )  # Projects managed by this user (if user is an admin)


class Project(Base):
    __tablename__ = "projects"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum("proposed", "in_progress", "completed", "cancelled", name="project_statuses"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    admin_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))  # Project manager/admin
    client_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))  # Client associated with the project

    # Relationships
    admin = relationship("User", back_populates="managed_projects", foreign_keys=[admin_id])
    client = relationship("User", back_populates="projects", foreign_keys=[client_id])
    missions = relationship("Mission", back_populates="project")


class Mission(Base):
    __tablename__ = "missions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(JSON, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum("open", "assigned", "completed", name="mission_statuses"), nullable=False)

    project = relationship("Project", back_populates="missions")
