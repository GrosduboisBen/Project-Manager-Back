from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.invoices import InvoiceCreate, InvoiceUpdate, InvoiceResponse, InvoiceListResponse
from portfolio.crud.invoices import (
    create_invoice,
    get_invoices_with_count,
    get_invoice,
    update_invoice,
    delete_invoice,
)

router = APIRouter()

@router.post("/", response_model=InvoiceResponse)
def create(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    """
    Create a new invoice.
    """
    return create_invoice(db, invoice)


@router.get("/", response_model=InvoiceListResponse)
def read_invoices(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of invoices with pagination.
    """
    return get_invoices_with_count(db, page, page_size)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: str, db: Session = Depends(get_db)):
    """
    Retrieve an invoice by ID.
    """
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@router.put("/{invoice_id}", response_model=InvoiceResponse)
def update(invoice_id: str, invoice: InvoiceUpdate, db: Session = Depends(get_db)):
    """
    Update an invoice by ID.
    """
    updated_invoice = update_invoice(db, invoice_id, invoice)
    if not updated_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated_invoice


@router.delete("/{invoice_id}")
def delete(invoice_id: str, db: Session = Depends(get_db)):
    """
    Delete an invoice by ID.
    """
    deleted = delete_invoice(db, invoice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted successfully"}
