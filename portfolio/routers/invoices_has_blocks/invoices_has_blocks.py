from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.invoices_has_blocks import InvoiceHasCustomBlockCreate
from portfolio.crud.invoice_has_blocks import (
    create_invoice_custom_block,
    delete_invoice_custom_block,
)

router = APIRouter()

@router.post("/")
def create(association: InvoiceHasCustomBlockCreate, db: Session = Depends(get_db)):
    """
    Create an association between an invoice and a custom block.
    """
    return create_invoice_custom_block(db, association)


@router.delete("/{invoice_id}/{custom_block_id}")
def delete(invoice_id: str, custom_block_id: str, db: Session = Depends(get_db)):
    """
    Delete an association between an invoice and a custom block.
    """
    deleted = delete_invoice_custom_block(db, invoice_id, custom_block_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Association not found")
    return {"message": "Association deleted successfully"}
