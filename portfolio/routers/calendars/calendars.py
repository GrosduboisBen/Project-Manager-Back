from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.calendars import (
    AvailabilityCalendarCreate,
    AvailabilityCalendarUpdate,
    AvailabilityCalendarResponse,
    AvailabilityCalendarListResponse,
)
from portfolio.crud.calendars import (
    create_availability,
    get_availability,
    get_availabilities,
    update_availability,
    delete_availability,
)

router = APIRouter()

@router.post("/", response_model=AvailabilityCalendarResponse)
def create(availability: AvailabilityCalendarCreate, db: Session = Depends(get_db)):
    """
    Create a new availability entry.
    """
    return create_availability(db, availability)


@router.get("/", response_model=AvailabilityCalendarListResponse)
def list_availabilities(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    List all availability entries with pagination.
    """
    return get_availabilities(db, page, page_size)


@router.get("/{availability_id}", response_model=AvailabilityCalendarResponse)
def read_availability(availability_id: str, db: Session = Depends(get_db)):
    """
    Get a specific availability entry by ID.
    """
    availability = get_availability(db, availability_id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability entry not found")
    return availability


@router.put("/{availability_id}", response_model=AvailabilityCalendarResponse)
def update(availability_id: str, availability: AvailabilityCalendarUpdate, db: Session = Depends(get_db)):
    """
    Update a specific availability entry by ID.
    """
    updated = update_availability(db, availability_id, availability)
    if not updated:
        raise HTTPException(status_code=404, detail="Availability entry not found")
    return updated


@router.delete("/{availability_id}")
def delete(availability_id: str, db: Session = Depends(get_db)):
    """
    Delete a specific availability entry by ID.
    """
    deleted = delete_availability(db, availability_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Availability entry not found")
    return {"message": "Availability entry deleted successfully"}
