from sqlalchemy.orm import Session
from portfolio.db.models.pricing import Pricing
from portfolio.db.models.tags import Tag
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


# Get a single pricing entry by ID
def get_pricing(db: Session, pricing_id: str):
    """
    Retrieve a single pricing entry by its ID.
    """
    return db.query(Pricing).filter(Pricing.id == pricing_id).first()

# Get an user custom pricing informations by user ID
def get_user_pricing(db: Session, user_id: str):
    """
    Retrieve a list of pricing informations.
    """
    # Full return list, according to UserPricing Model.
    custom_list = []

    # User pricing full list.
    user_pricing_list = db.query(Pricing).filter(Pricing.user_id == user_id).all()
    
    if user_pricing_list.__len__() > 0:
        for pricing in user_pricing_list:
            full_tag = db.query(Tag).filter(Tag.id == pricing.tag_id).first()
            custom_list.append(
                {
                    'user_id': user_id,
                    'tag_id': pricing.tag_id,
                    'tag_name': full_tag.name,
                    'price_per_day': pricing.price_per_day
                }
            )
    return custom_list



# Get all pricing entries with pagination
def get_pricing_with_count(db: Session, page: int, page_size: int):
    """
    Retrieve a paginated list of pricing entries and the total count.
    """
    skip = (page - 1) * page_size
    total = db.query(Pricing).count()
    pricing = db.query(Pricing).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "pricing": pricing,
    }


# Update a pricing entry
def update_pricing(db: Session, pricing_id: str, pricing: PricingUpdate):
    """
    Update an existing pricing entry by its ID.
    """
    db_pricing = db.query(Pricing).filter(Pricing.id == pricing_id).first()
    if not db_pricing:
        return None
    for key, value in pricing.model_dump(exclude_unset=True).items():
        setattr(db_pricing, key, value)
    db.commit()
    db.refresh(db_pricing)
    return db_pricing


# Delete a pricing entry
def delete_pricing(db: Session, pricing_id: str):
    """
    Delete a pricing entry by its ID.
    """
    db_pricing = db.query(Pricing).filter(Pricing.id == pricing_id).first()
    if not db_pricing:
        return None
    db.delete(db_pricing)
    db.commit()
    return db_pricing
