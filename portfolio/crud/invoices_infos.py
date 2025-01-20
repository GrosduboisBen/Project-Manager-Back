from sqlalchemy.orm import Session
from portfolio.db.models.invoices_infos import InvoiceInfo
from portfolio.schemas.invoices_infos import InvoiceInfoCreate, InvoiceInfoUpdate

# Create invoice information
def create_invoice_info(db: Session, invoice_info: InvoiceInfoCreate):
    db_invoice_info = InvoiceInfo(**invoice_info.model_dump())
    db.add(db_invoice_info)
    db.commit()
    db.refresh(db_invoice_info)
    return db_invoice_info


# Get invoice information by ID
def get_invoice_info(db: Session, invoice_info_id: str):
    return db.query(InvoiceInfo).filter(InvoiceInfo.id == invoice_info_id).first()


# Update invoice information
def update_invoice_info(db: Session, invoice_info_id: str, invoice_info: InvoiceInfoUpdate):
    db_invoice_info = db.query(InvoiceInfo).filter(InvoiceInfo.id == invoice_info_id).first()
    if not db_invoice_info:
        return None
    for key, value in invoice_info.model_dump(exclude_unset=True).items():
        setattr(db_invoice_info, key, value)
    db.commit()
    db.refresh(db_invoice_info)
    return db_invoice_info


# Delete invoice information
def delete_invoice_info(db: Session, invoice_info_id: str):
    db_invoice_info = db.query(InvoiceInfo).filter(InvoiceInfo.id == invoice_info_id).first()
    if not db_invoice_info:
        return None
    db.delete(db_invoice_info)
    db.commit()
    return db_invoice_info
