from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from portfolio.database import get_db
from portfolio.schemas.invoices_has_blocks import InvoiceHasCustomBlockCreate
from portfolio.crud.invoice_has_blocks import (
    create_invoice_custom_block,
    delete_invoice_custom_block,
    get_custom_blocks_by_invoice,
    get_invoices_by_custom_block,
)

from portfolio.schemas.custom_blocks import CustomBlockListResponse
from portfolio.schemas.invoices import InvoiceListResponse

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

@router.get("/invoices/{invoice_id}/custom_blocks", response_model=CustomBlockListResponse)
def get_custom_blocks(invoice_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all custom blocks associated with a specific invoice.
    """
    custom_blocks = get_custom_blocks_by_invoice(db, invoice_id)
    if not custom_blocks:
        raise HTTPException(status_code=404, detail="No custom blocks found for this invoice")
    return custom_blocks


@router.get("/custom_blocks/{custom_block_id}/invoices", response_model=InvoiceListResponse)
def get_invoices(custom_block_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all invoices associated with a specific custom block.
    """
    invoices = get_invoices_by_custom_block(db, custom_block_id)
    if not invoices:
        raise HTTPException(status_code=404, detail="No invoices found for this custom block")
    return invoices
