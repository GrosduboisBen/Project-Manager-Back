from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.projects import (
    create_project,
    get_projects_with_count,
    get_project,
    update_project,
    delete_project,
)
from portfolio.schemas.projects import ProjectCreate, ProjectUpdate, ProjectResponse, ProjectListResponse

router = APIRouter()

@router.post("/", response_model=ProjectResponse)
def create(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Create a new project.
    """
    return create_project(db, project)


@router.get("/", response_model=ProjectListResponse)
def read_projects(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of projects with pagination.
    """
    return get_projects_with_count(db, page=page, page_size=page_size)


@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(project_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a project by ID.
    """
    project = get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=ProjectResponse)
def update(project_id: str, project: ProjectUpdate, db: Session = Depends(get_db)):
    """
    Update a project by ID.
    """
    updated_project = update_project(db, project_id, project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@router.delete("/{project_id}")
def delete(project_id: str, db: Session = Depends(get_db)):
    """
    Delete a project by ID.
    """
    deleted_project = delete_project(db, project_id)
    if not deleted_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}