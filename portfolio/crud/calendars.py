from sqlalchemy.orm import Session
from portfolio.db.models.calendars import AvailabilityCalendar
from portfolio.schemas.calendars import (
    AvailabilityCalendarCreate,
    AvailabilityCalendarUpdate,
)

# Create a new availability entry
def create_availability(db: Session, availability: AvailabilityCalendarCreate):
    db_availability = AvailabilityCalendar(**availability.model_dump())
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    return db_availability


# Get availability by ID
def get_availability(db: Session, availability_id: str):
    return db.query(AvailabilityCalendar).filter(AvailabilityCalendar.id == availability_id).first()


# Get all availability entries with pagination
def get_availabilities(db: Session, page: int, page_size: int):
    skip = (page - 1) * page_size
    total = db.query(AvailabilityCalendar).count()
    availabilities = (
        db.query(AvailabilityCalendar).offset(skip).limit(page_size).all()
    )
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "availabilities": availabilities,
    }


# Update an availability entry
def update_availability(db: Session, availability_id: str, availability: AvailabilityCalendarUpdate):
    db_availability = db.query(AvailabilityCalendar).filter(AvailabilityCalendar.id == availability_id).first()
    if not db_availability:
        return None
    for key, value in availability.model_dump(exclude_unset=True).items():
        setattr(db_availability, key, value)
    db.commit()
    db.refresh(db_availability)
    return db_availability


# Delete an availability entry
def delete_availability(db: Session, availability_id: str):
    db_availability = db.query(AvailabilityCalendar).filter(AvailabilityCalendar.id == availability_id).first()
    if not db_availability:
        return None
    db.delete(db_availability)
    db.commit()
    return db_availability
