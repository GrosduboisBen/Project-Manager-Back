from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.missions import (
    create_mission,
    get_missions_with_count,
    get_mission,
    update_mission,
    delete_mission,
)
from portfolio.schemas.missions import MissionCreate, MissionUpdate, MissionResponse, MissionListResponse

router = APIRouter()

@router.post("/", response_model=MissionResponse)
def create(mission: MissionCreate, db: Session = Depends(get_db)):
    """
    Create a new mission.
    """
    return create_mission(db, mission)


@router.get("/", response_model=MissionListResponse)
def read_missions(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of missions with pagination.
    """
    return get_missions_with_count(db, page=page, page_size=page_size)


@router.get("/{mission_id}", response_model=MissionResponse)
def read_mission(mission_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a mission by ID.
    """
    mission = get_mission(db, mission_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission


@router.put("/{mission_id}", response_model=MissionResponse)
def update(mission_id: str, mission: MissionUpdate, db: Session = Depends(get_db)):
    """
    Update a mission by ID.
    """
    updated_mission = update_mission(db, mission_id, mission)
    if not updated_mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return updated_mission


@router.delete("/{mission_id}")
def delete(mission_id: str, db: Session = Depends(get_db)):
    """
    Delete a mission by ID.
    """
    deleted_mission = delete_mission(db, mission_id)
    if not deleted_mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return {"message": "Mission deleted successfully"}
