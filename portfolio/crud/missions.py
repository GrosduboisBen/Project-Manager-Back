from sqlalchemy.orm import Session
from portfolio.db.models.missions import Mission
from portfolio.schemas.missions import MissionCreate, MissionUpdate
from datetime import datetime

# Create a new mission
def create_mission(db: Session, mission: MissionCreate):
    """
    Create a new mission in the database.
    """
    db_mission = Mission(
        **mission.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


# Get a single mission by ID
def get_mission(db: Session, mission_id: str):
    """
    Retrieve a single mission by its ID.
    """
    return db.query(Mission).filter(Mission.id == mission_id).first()


# Get all missions with pagination
def get_missions_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of missions and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Mission).count()
    missions = db.query(Mission).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "missions": missions,
    }


# Update a mission
def update_mission(db: Session, mission_id: str, mission: MissionUpdate):
    """
    Update an existing mission by its ID.
    """
    db_mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not db_mission:
        return None
    for key, value in mission.model_dump(exclude_unset=True).items():
        setattr(db_mission, key, value)
    db.commit()
    db.refresh(db_mission)
    return db_mission


# Delete a mission
def delete_mission(db: Session, mission_id: str):
    """
    Delete a mission by its ID.
    """
    db_mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not db_mission:
        return None
    db.delete(db_mission)
    db.commit()
    return db_mission
