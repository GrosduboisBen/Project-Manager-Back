from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.milestones import (
    create_milestone,
    get_milestones_with_count,
    get_milestone,
    update_milestone,
    delete_milestone,
)
from portfolio.schemas.milestones import MilestoneCreate, MilestoneUpdate, MilestoneResponse, MilestoneListResponse

router = APIRouter()

@router.post("/", response_model=MilestoneResponse)
def create(milestone: MilestoneCreate, db: Session = Depends(get_db)):
    """
    Create a new milestone.
    """
    return create_milestone(db, milestone)


@router.get("/", response_model=MilestoneListResponse)
def read_milestones(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of milestones with pagination.
    """
    return get_milestones_with_count(db, page=page, page_size=page_size)


@router.get("/{milestone_id}", response_model=MilestoneResponse)
def read_milestone(milestone_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a milestone by ID.
    """
    milestone = get_milestone(db, milestone_id)
    if not milestone:
        raise HTTPException(status_code=404, detail="Milestone not found")
    return milestone


@router.put("/{milestone_id}", response_model=MilestoneResponse)
def update(milestone_id: str, milestone: MilestoneUpdate, db: Session = Depends(get_db)):
    """
    Update a milestone by ID.
    """
    updated_milestone = update_milestone(db, milestone_id, milestone)
    if not updated_milestone:
        raise HTTPException(status_code=404, detail="Milestone not found")
    return updated_milestone


@router.delete("/{milestone_id}")
def delete(milestone_id: str, db: Session = Depends(get_db)):
    """
    Delete a milestone by ID.
    """
    deleted_milestone = delete_milestone(db, milestone_id)
    if not deleted_milestone:
        raise HTTPException(status_code=404, detail="Milestone not found")
    return {"message": "Milestone deleted successfully"}
