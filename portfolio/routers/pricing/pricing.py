from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.crud.pricing import (
    create_pricing,
    get_pricing_with_count,
    get_pricing,
    update_pricing,
    delete_pricing,
)
from portfolio.schemas.pricing import PricingCreate, PricingUpdate, PricingResponse, PricingListResponse

router = APIRouter()

@router.post("/", response_model=PricingResponse)
def create(pricing: PricingCreate, db: Session = Depends(get_db)):
    """
    Create a new pricing entry.
    """
    return create_pricing(db, pricing)


@router.get("/", response_model=PricingListResponse)
def read_pricing(
    page: int = Query(1, ge=1),  # Minimum page number
    page_size: int = Query(10, ge=1, le=100),  # Maximum items per page
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of pricing entries with pagination.
    """
    return get_pricing_with_count(db, page=page, page_size=page_size)


@router.get("/{pricing_id}", response_model=PricingResponse)
def read_pricing_entry(pricing_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a pricing entry by ID.
    """
    pricing = get_pricing(db, pricing_id)
    if not pricing:
        raise HTTPException(status_code=404, detail="Pricing entry not found")
    return pricing


@router.put("/{pricing_id}", response_model=PricingResponse)
def update(pricing_id: str, pricing: PricingUpdate, db: Session = Depends(get_db)):
    """
    Update a pricing entry by ID.
    """
    updated_pricing = update_pricing(db, pricing_id, pricing)
    if not updated_pricing:
        raise HTTPException(status_code=404, detail="Pricing entry not found")
    return updated_pricing


@router.delete("/{pricing_id}")
def delete(pricing_id: str, db: Session = Depends(get_db)):
    """
    Delete a pricing entry by ID.
    """
    deleted_pricing = delete_pricing(db, pricing_id)
    if not deleted_pricing:
        raise HTTPException(status_code=404, detail="Pricing entry not found")
    return {"message": "Pricing entry deleted successfully"}
