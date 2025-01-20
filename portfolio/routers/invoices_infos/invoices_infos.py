from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.invoices_infos import InvoiceInfoCreate, InvoiceInfoUpdate, InvoiceInfoResponse
from portfolio.crud.invoices_infos import (
    create_invoice_info,
    get_invoice_info,
    update_invoice_info,
    delete_invoice_info,
)

router = APIRouter()

@router.post("/", response_model=InvoiceInfoResponse)
def create(info: InvoiceInfoCreate, db: Session = Depends(get_db)):
    """
    Create a new invoice info.
    """
    return create_invoice_info(db, info)


@router.get("/{info_id}", response_model=InvoiceInfoResponse)
def read(info_id: str, db: Session = Depends(get_db)):
    """
    Retrieve invoice info by ID.
    """
    info = get_invoice_info(db, info_id)
    if not info:
        raise HTTPException(status_code=404, detail="Invoice info not found")
    return info


@router.put("/{info_id}", response_model=InvoiceInfoResponse)
def update(info_id: str, info: InvoiceInfoUpdate, db: Session = Depends(get_db)):
    """
    Update invoice info by ID.
    """
    updated_info = update_invoice_info(db, info_id, info)
    if not updated_info:
        raise HTTPException(status_code=404, detail="Invoice info not found")
    return updated_info


@router.delete("/{info_id}")
def delete(info_id: str, db: Session = Depends(get_db)):
    """
    Delete invoice info by ID.
    """
    deleted = delete_invoice_info(db, info_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice info not found")
    return {"message": "Invoice info deleted successfully"}
