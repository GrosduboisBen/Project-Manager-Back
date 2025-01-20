from sqlalchemy.orm import Session
from portfolio.db.models.technologies import Technology
from portfolio.schemas.technologies import TechnologyCreate, TechnologyUpdate
from datetime import datetime

# Create a new technology
def create_technology(db: Session, technology: TechnologyCreate):
    """
    Create a new technology in the database.
    """
    db_technology = Technology(
        **technology.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_technology)
    db.commit()
    db.refresh(db_technology)
    return db_technology


# Get a single technology by ID
def get_technology(db: Session, technology_id: str):
    """
    Retrieve a single technology by its ID.
    """
    return db.query(Technology).filter(Technology.id == technology_id).first()


# Get all technologies with pagination
def get_technologies_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of technologies and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Technology).count()
    technologies = db.query(Technology).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "technologies": technologies,
    }


# Update a technology
def update_technology(db: Session, technology_id: str, technology: TechnologyUpdate):
    """
    Update an existing technology by its ID.
    """
    db_technology = db.query(Technology).filter(Technology.id == technology_id).first()
    if not db_technology:
        return None
    for key, value in technology.model_dump(exclude_unset=True).items():
        setattr(db_technology, key, value)
    db.commit()
    db.refresh(db_technology)
    return db_technology


# Delete a technology
def delete_technology(db: Session, technology_id: str):
    """
    Delete a technology by its ID.
    """
    db_technology = db.query(Technology).filter(Technology.id == technology_id).first()
    if not db_technology:
        return None
    db.delete(db_technology)
    db.commit()
    return db_technology
