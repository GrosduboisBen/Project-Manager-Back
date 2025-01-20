from sqlalchemy.orm import Session
from portfolio.db.models.milestones import Milestone
from portfolio.schemas.milestones import MilestoneCreate, MilestoneUpdate
from datetime import datetime

# Create a new milestone
def create_milestone(db: Session, milestone: MilestoneCreate):
    """
    Create a new milestone in the database.
    """
    db_milestone = Milestone(
        **milestone.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_milestone)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone


# Get a single milestone by ID
def get_milestone(db: Session, milestone_id: str):
    """
    Retrieve a single milestone by its ID.
    """
    return db.query(Milestone).filter(Milestone.id == milestone_id).first()


# Get all milestones with pagination
def get_milestones_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of milestones and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Milestone).count()
    milestones = db.query(Milestone).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "milestones": milestones,
    }


# Update a milestone
def update_milestone(db: Session, milestone_id: str, milestone: MilestoneUpdate):
    """
    Update an existing milestone by its ID.
    """
    db_milestone = db.query(Milestone).filter(Milestone.id == milestone_id).first()
    if not db_milestone:
        return None
    for key, value in milestone.model_dump(exclude_unset=True).items():
        setattr(db_milestone, key, value)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone


# Delete a milestone
def delete_milestone(db: Session, milestone_id: str):
    """
    Delete a milestone by its ID.
    """
    db_milestone = db.query(Milestone).filter(Milestone.id == milestone_id).first()
    if not db_milestone:
        return None
    db.delete(db_milestone)
    db.commit()
    return db_milestone
