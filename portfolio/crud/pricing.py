from sqlalchemy.orm import Session
from portfolio.db.models.pricing import Pricing
from portfolio.schemas.pricing import PricingCreate, PricingUpdate
from datetime import datetime

# Create a new pricing entry
def create_pricing(db: Session, pricing: PricingCreate):
    db_pricing = Pricing(
        **pricing.model_dump(),
        creation_date=datetime.now()
    )
    db.add(db_pricing)
    db.commit()
    db.refresh(db_pricing)
    return db_pricing
