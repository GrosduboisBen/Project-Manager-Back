from sqlalchemy.orm import Session
from portfolio.db.models.projects import Project
from portfolio.schemas.projects import ProjectCreate, ProjectUpdate
from datetime import datetime

# Create a new project
def create_project(db: Session, project: ProjectCreate):
    """
    Create a new project in the database.
    """
    db_project = Project(
        **project.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


# Get a single project by ID
def get_project(db: Session, project_id: str):
    """
    Retrieve a single project by its ID.
    """
    return db.query(Project).filter(Project.id == project_id).first()


# Get all projects with pagination
def get_projects_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of projects and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Project).count()
    projects = db.query(Project).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "projects": projects,
    }


# Update a project
def update_project(db: Session, project_id: str, project: ProjectUpdate):
    """
    Update an existing project by its ID.
    """
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        return None
    for key, value in project.model_dump(exclude_unset=True).items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project


# Delete a project
def delete_project(db: Session, project_id: str):
    """
    Delete a project by its ID.
    """
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project
