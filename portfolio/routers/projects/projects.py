from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.projects import (
    create_project,
    get_projects,
    get_project,
    update_project,
    delete_project,
)
from portfolio.schemas.projects import ProjectCreate, ProjectUpdate, ProjectResponse, ProjectListResponse,ProjectStatusEnum
from typing import Optional
from datetime import date

router = APIRouter()

@router.post("/", response_model=ProjectResponse)
def create(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Create a new project.
    """
    return create_project(db, project)


@router.get("/", response_model=ProjectListResponse)
def list_projects(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    client_id: Optional[str] = None,
    handler_id: Optional[str] = None,
    title: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    total_price_min: Optional[float] = None,
    total_price_max: Optional[float] = None,
    status: Optional[ProjectStatusEnum] = None,
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of projects with optional filters.
    """
    return get_projects(
        db,
        page=page,
        page_size=page_size,
        client_id=client_id,
        handler_id=handler_id,
        title=title,
        start_date=start_date,
        end_date=end_date,
        total_price_min=total_price_min,
        total_price_max=total_price_max,
        status=status,
    )


@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(project_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a project by ID.
    """
    project = get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/{handler_id}", response_model=ProjectResponse)
def read_project(handler_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a project by handler ID.
    """
    project = get_project(db, handler_id)
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
