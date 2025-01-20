from sqlalchemy.orm import Session
from portfolio.db.models.tags import Tag
from portfolio.schemas.tags import TagCreate, TagUpdate
from datetime import datetime

# Create a new tag
def create_tag(db: Session, tag: TagCreate):
    """
    Create a new tag in the database.
    """
    db_tag = Tag(
        **tag.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


# Get a single tag by ID
def get_tag(db: Session, tag_id: str):
    """
    Retrieve a single tag by its ID.
    """
    return db.query(Tag).filter(Tag.id == tag_id).first()


# Get all tags with pagination
def get_tags_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of tags and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Tag).count()
    tags = db.query(Tag).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "tags": tags,
    }


# Update a tag
def update_tag(db: Session, tag_id: str, tag: TagUpdate):
    """
    Update an existing tag by its ID.
    """
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not db_tag:
        return None
    for key, value in tag.model_dump(exclude_unset=True).items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag


# Delete a tag
def delete_tag(db: Session, tag_id: str):
    """
    Delete a tag by its ID.
    """
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not db_tag:
        return None
    db.delete(db_tag)
    db.commit()
    return db_tag
