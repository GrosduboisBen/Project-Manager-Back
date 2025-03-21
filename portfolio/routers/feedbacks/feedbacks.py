from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.feedbacks import (
    create_feedback,
    get_feedbacks_with_count,
    get_feedback,
    update_feedback,
    delete_feedback,
    get_user_feedbacks
)
from portfolio.schemas.feedbacks import FeedbackCreate, FeedbackUpdate, FeedbackResponse, FeedbackListResponse,FeedBackCustomResponse

router = APIRouter()

@router.post("/", response_model=FeedbackResponse)
def create(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    """
    Create a new feedback.
    """
    return create_feedback(db, feedback)


@router.get("/", response_model=FeedbackListResponse)
def read_feedbacks(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of feedbacks with pagination.
    """
    return get_feedbacks_with_count(db, page=page, page_size=page_size)


@router.get("/{feedback_id}", response_model=FeedbackResponse)
def read_feedback(feedback_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a feedback by ID.
    """
    feedback = get_feedback(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@router.get("/handler/{handler_id}", response_model=list[FeedBackCustomResponse])
def read_feedbacks(handler_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all feedbacks for a given user by its ID.
    """
    feedbacks = get_user_feedbacks(db, handler_id)
    if not feedbacks:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedbacks


@router.put("/{feedback_id}", response_model=FeedbackResponse)
def update(feedback_id: str, feedback: FeedbackUpdate, db: Session = Depends(get_db)):
    """
    Update a feedback by ID.
    """
    updated_feedback = update_feedback(db, feedback_id, feedback)
    if not updated_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated_feedback


@router.delete("/{feedback_id}")
def delete(feedback_id: str, db: Session = Depends(get_db)):
    """
    Delete a feedback by ID.
    """
    deleted_feedback = delete_feedback(db, feedback_id)
    if not deleted_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return {"message": "Feedback deleted successfully"}
