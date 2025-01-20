from sqlalchemy.orm import Session
from portfolio.db.models.invoices_has_blocks import InvoiceHasCustomBlock
from portfolio.schemas.invoices_has_blocks import InvoiceHasCustomBlockCreate
from portfolio.db.models.custom_blocks import CustomBlock
from portfolio.db.models.invoices import Invoice


# Create an association between an invoice and a custom block
def create_invoice_custom_block(db: Session, association: InvoiceHasCustomBlockCreate):
    db_association = InvoiceHasCustomBlock(**association.model_dump())
    db.add(db_association)
    db.commit()
    return db_association


# Delete an association between an invoice and a custom block
def delete_invoice_custom_block(db: Session, invoice_id: str, custom_block_id: str):
    db_association = db.query(InvoiceHasCustomBlock).filter(
        InvoiceHasCustomBlock.invoice_id == invoice_id,
        InvoiceHasCustomBlock.custom_block_id == custom_block_id
    ).first()
    if not db_association:
        return None
    db.delete(db_association)
    db.commit()
    return db_association

def get_custom_blocks_by_invoice(db: Session, invoice_id: str):
    """
    Retrieve all custom blocks associated with a given invoice.
    """
    return (
        db.query(CustomBlock)
        .join(InvoiceHasCustomBlock, InvoiceHasCustomBlock.custom_block_id == CustomBlock.id)
        .filter(InvoiceHasCustomBlock.invoice_id == invoice_id)
        .all()
    )


def get_invoices_by_custom_block(db: Session, custom_block_id: str):
    """
    Retrieve all invoices associated with a given custom block.
    """
    return (
        db.query(Invoice)
        .join(InvoiceHasCustomBlock, InvoiceHasCustomBlock.invoice_id == Invoice.id)
        .filter(InvoiceHasCustomBlock.custom_block_id == custom_block_id)
        .all()
    )