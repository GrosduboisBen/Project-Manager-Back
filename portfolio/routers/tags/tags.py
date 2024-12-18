from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.tags import (
    create_tag,
    get_tags_with_count,
    get_tag,
    update_tag,
    delete_tag,
)
from portfolio.schemas.tags import TagCreate, TagUpdate, TagResponse, TagListResponse

router = APIRouter()

@router.post("/", response_model=TagResponse)
def create(tag: TagCreate, db: Session = Depends(get_db)):
    """
    Create a new tag.
    """
    return create_tag(db, tag)


@router.get("/", response_model=TagListResponse)
def read_tags(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of tags with pagination.
    """
    return get_tags_with_count(db, page=page, page_size=page_size)


@router.get("/{tag_id}", response_model=TagResponse)
def read_tag(tag_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a tag by ID.
    """
    tag = get_tag(db, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.put("/{tag_id}", response_model=TagResponse)
def update(tag_id: str, tag: TagUpdate, db: Session = Depends(get_db)):
    """
    Update a tag by ID.
    """
    updated_tag = update_tag(db, tag_id, tag)
    if not updated_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return updated_tag


@router.delete("/{tag_id}")
def delete(tag_id: str, db: Session = Depends(get_db)):
    """
    Delete a tag by ID.
    """
    deleted_tag = delete_tag(db, tag_id)
    if not deleted_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return {"message": "Tag deleted successfully"}
