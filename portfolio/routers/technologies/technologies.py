from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.technologies import (
    create_technology,
    get_technologies_with_count,
    get_technology,
    update_technology,
    delete_technology,
)
from portfolio.schemas.technologies import TechnologyCreate, TechnologyUpdate, TechnologyResponse, TechnologyListResponse

router = APIRouter()

@router.post("/", response_model=TechnologyResponse)
def create(technology: TechnologyCreate, db: Session = Depends(get_db)):
    """
    Create a new technology.
    """
    return create_technology(db, technology)


@router.get("/", response_model=TechnologyListResponse)
def read_technologies(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of technologies with pagination.
    """
    return get_technologies_with_count(db, page=page, page_size=page_size)


@router.get("/{technology_id}", response_model=TechnologyResponse)
def read_technology(technology_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a technology by ID.
    """
    technology = get_technology(db, technology_id)
    if not technology:
        raise HTTPException(status_code=404, detail="Technology not found")
    return technology


@router.put("/{technology_id}", response_model=TechnologyResponse)
def update(technology_id: str, technology: TechnologyUpdate, db: Session = Depends(get_db)):
    """
    Update a technology by ID.
    """
    updated_technology = update_technology(db, technology_id, technology)
    if not updated_technology:
        raise HTTPException(status_code=404, detail="Technology not found")
    return updated_technology


@router.delete("/{technology_id}")
def delete(technology_id: str, db: Session = Depends(get_db)):
    """
    Delete a technology by ID.
    """
    deleted_technology = delete_technology(db, technology_id)
    if not deleted_technology:
        raise HTTPException(status_code=404, detail="Technology not found")
    return {"message": "Technology deleted successfully"}
