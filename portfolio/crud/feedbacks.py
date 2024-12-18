from sqlalchemy.orm import Session
from portfolio.db.models.feedbacks import UserFeedback
from portfolio.schemas.feedbacks import FeedbackCreate, FeedbackUpdate
from datetime import datetime

# Create a new feedback
def create_feedback(db: Session, feedback: FeedbackCreate):
    """
    Create a new feedback in the database.
    """
    db_feedback = UserFeedback(
        **feedback.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


# Get a single feedback by ID
def get_feedback(db: Session, feedback_id: str):
    """
    Retrieve a single feedback by its ID.
    """
    return db.query(UserFeedback).filter(UserFeedback.id == feedback_id).first()


# Get all feedbacks with pagination
def get_feedbacks_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of feedbacks and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(UserFeedback).count()
    feedbacks = db.query(UserFeedback).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "feedbacks": feedbacks,
    }


# Update a feedback
def update_feedback(db: Session, feedback_id: str, feedback: FeedbackUpdate):
    """
    Update an existing feedback by its ID.
    """
    db_feedback = db.query(UserFeedback).filter(UserFeedback.id == feedback_id).first()
    if not db_feedback:
        return None
    for key, value in feedback.model_dump(exclude_unset=True).items():
        setattr(db_feedback, key, value)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


# Delete a feedback
def delete_feedback(db: Session, feedback_id: str):
    """
    Delete a feedback by its ID.
    """
    db_feedback = db.query(UserFeedback).filter(UserFeedback.id == feedback_id).first()
    if not db_feedback:
        return None
    db.delete(db_feedback)
    db.commit()
    return db_feedback
