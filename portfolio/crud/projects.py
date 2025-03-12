from sqlalchemy.orm import Session
from sqlalchemy import and_
from portfolio.db.models.projects import Project
from portfolio.schemas.projects import ProjectCreate, ProjectUpdate, ProjectStatusEnum
from datetime import datetime
from typing import Optional
from datetime import date

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

def get_project_by_handler(
        db: Session,
        handler_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        client_id: Optional[str] = None,
        title: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        total_price_min: Optional[float] = None,
        total_price_max: Optional[float] = None,
        status: Optional[ProjectStatusEnum] = None
    ):
    """
    Retrieve a single project by its ID.
    """
    filters = []
    filters.append(Project.handler_id == handler_id)
    
    if client_id:
        filters.append(Project.client_id == client_id)
    if title:
        filters.append(Project.title.ilike(f"%{title}%"))  # Partial match
    if start_date:
        filters.append(Project.start_date >= start_date)
    if end_date:
        filters.append(Project.end_date <= end_date)
    if total_price_min is not None:
        filters.append(Project.total_price >= total_price_min)
    if total_price_max is not None:
        filters.append(Project.total_price <= total_price_max)
    if status:
        filters.append(Project.status == status)

    query = db.query(Project).filter(and_(*filters))
    if page_size and page :
        projects = query.offset((page - 1) * page_size).limit(page_size).all()
    else:
        projects = query.all()
    return {
        "projects": projects
    }


# Get projects with filtering and pagination
def get_projects(
    db: Session,
    page: int,
    page_size: int,
    client_id: Optional[str] = None,
    handler_id: Optional[str] = None,
    title: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    total_price_min: Optional[float] = None,
    total_price_max: Optional[float] = None,
    status: Optional[ProjectStatusEnum] = None,
):
    filters = []
    
    if client_id:
        filters.append(Project.client_id == client_id)
    if handler_id:
        filters.append(Project.handler_id == handler_id)
    if title:
        filters.append(Project.title.ilike(f"%{title}%"))  # Partial match
    if start_date:
        filters.append(Project.start_date >= start_date)
    if end_date:
        filters.append(Project.end_date <= end_date)
    if total_price_min is not None:
        filters.append(Project.total_price >= total_price_min)
    if total_price_max is not None:
        filters.append(Project.total_price <= total_price_max)
    if status:
        filters.append(Project.status == status)

    query = db.query(Project).filter(and_(*filters))

    total = query.count()
    projects = query.offset((page - 1) * page_size).limit(page_size).all()

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
