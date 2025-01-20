from sqlalchemy.orm import Session
from portfolio.db.models.invoices import Invoice
from portfolio.schemas.invoices import InvoiceCreate, InvoiceUpdate
from datetime import datetime

# Create a new invoice
def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(
        **invoice.model_dump(),
        last_update=datetime.now()
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


# Get a single invoice by ID
def get_invoice(db: Session, invoice_id: str):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()


# Get all invoices with pagination
def get_invoices_with_count(db: Session, page: int, page_size: int):
    skip = (page - 1) * page_size
    total = db.query(Invoice).count()
    invoices = db.query(Invoice).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "invoices": invoices,
    }


# Update an invoice
def update_invoice(db: Session, invoice_id: str, invoice: InvoiceUpdate):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not db_invoice:
        return None
    for key, value in invoice.model_dump(exclude_unset=True).items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


# Delete an invoice
def delete_invoice(db: Session, invoice_id: str):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not db_invoice:
        return None
    db.delete(db_invoice)
    db.commit()
    return db_invoice
