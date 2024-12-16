from sqlalchemy.orm import Session
from portfolio.db.models.users import User
from portfolio.schemas.users import UserCreate, UserUpdate
from datetime import datetime,timezone

# Create a new user
def create_user(db: Session, user: UserCreate):
    """
    Create a new user with the provided data.
    Automatically set creation_date to the current time.
    """
    db_user = User(
        **user.model_dump(),
        creation_date=datetime.now(timezone.utc)  # Ensure creation_date is set
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

# Get all users with pagination
def get_users_with_count(db: Session, page: int, page_size: int):
    skip = (page - 1) * page_size
    total = db.query(User).count()
    users = db.query(User).offset(skip).limit(page_size).all()
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "users": users,
    }

# Update a user
def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
