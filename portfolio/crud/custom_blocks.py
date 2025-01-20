from sqlalchemy.orm import Session
from portfolio.db.models.custom_blocks import CustomBlock
from portfolio.schemas.custom_blocks import CustomBlockCreate, CustomBlockUpdate

# Create a custom block
def create_custom_block(db: Session, custom_block: CustomBlockCreate):
    db_custom_block = CustomBlock(**custom_block.model_dump())
    db.add(db_custom_block)
    db.commit()
    db.refresh(db_custom_block)
    return db_custom_block


# Get a custom block by ID
def get_custom_block(db: Session, custom_block_id: str):
    return db.query(CustomBlock).filter(CustomBlock.id == custom_block_id).first()


# Update a custom block
def update_custom_block(db: Session, custom_block_id: str, custom_block: CustomBlockUpdate):
    db_custom_block = db.query(CustomBlock).filter(CustomBlock.id == custom_block_id).first()
    if not db_custom_block:
        return None
    for key, value in custom_block.model_dump(exclude_unset=True).items():
        setattr(db_custom_block, key, value)
    db.commit()
    db.refresh(db_custom_block)
    return db_custom_block


# Delete a custom block
def delete_custom_block(db: Session, custom_block_id: str):
    db_custom_block = db.query(CustomBlock).filter(CustomBlock.id == custom_block_id).first()
    if not db_custom_block:
        return None
    db.delete(db_custom_block)
    db.commit()
    return db_custom_block
