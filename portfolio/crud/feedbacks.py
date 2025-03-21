from sqlalchemy.orm import Session
from portfolio.db.models.feedbacks import UserFeedback
from portfolio.schemas.feedbacks import FeedbackCreate, FeedbackUpdate, FeedBackCustomResponse
from portfolio.db.models.users import User
from portfolio.db.models.projects import Project
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

def get_user_feedbacks(db: Session, handler_id: str):
    """
    Retrieve custom feedbacks see `FeedBackCustomResponse`.
    """
    feedback_list: list[FeedBackCustomResponse] = []
    projects = db.query(Project).filter(Project.handler_id == handler_id).all()
    if projects.__len__() > 0:
        for project in projects:
            project_feedback = db.query(UserFeedback).filter(UserFeedback.project_id == project.id).first()
            if project_feedback is not None:
                feedback_user = db.query(User).filter(User.id == project_feedback.user_id).first()
                feedback_list.append(
                    {
                        'id':project_feedback.id,
                        'creation_date':project_feedback.creation_date,
                        'handler_id':handler_id,
                        'user_name':feedback_user.name,
                        'project_name':project.title,
                        'user_id':project_feedback.user_id,
                        'project_id':project.id,
                        'feedback':project_feedback.feedback,
                        'rating':project_feedback.rating,
                    }
                )
            else:
                continue 
    return feedback_list


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
