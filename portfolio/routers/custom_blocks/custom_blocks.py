from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.custom_blocks import CustomBlockCreate, CustomBlockUpdate, CustomBlockResponse
from portfolio.crud.custom_blocks import (
    create_custom_block,
    get_custom_block,
    update_custom_block,
    delete_custom_block,
)

router = APIRouter()

@router.post("/", response_model=CustomBlockResponse)
def create(block: CustomBlockCreate, db: Session = Depends(get_db)):
    """
    Create a new custom block.
    """
    return create_custom_block(db, block)


@router.get("/{block_id}", response_model=CustomBlockResponse)
def read(block_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a custom block by ID.
    """
    block = get_custom_block(db, block_id)
    if not block:
        raise HTTPException(status_code=404, detail="Custom block not found")
    return block


@router.put("/{block_id}", response_model=CustomBlockResponse)
def update(block_id: str, block: CustomBlockUpdate, db: Session = Depends(get_db)):
    """
    Update a custom block by ID.
    """
    updated_block = update_custom_block(db, block_id, block)
    if not updated_block:
        raise HTTPException(status_code=404, detail="Custom block not found")
    return updated_block


@router.delete("/{block_id}")
def delete(block_id: str, db: Session = Depends(get_db)):
    """
    Delete a custom block by ID.
    """
    deleted = delete_custom_block(db, block_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Custom block not found")
    return {"message": "Custom block deleted successfully"}
