from sqlalchemy.orm import Session
from portfolio.db.models.users import User
from portfolio.schemas.users import UserCreate, UserUpdate

# Create users
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by Id
def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

# Get users ( paginated )
def get_users_with_count(db: Session, page: int, page_size: int):
    # Calculate skip from page and page_size
    skip = (page - 1) * page_size

    # Query the total number of users
    total = db.query(User).count()

    # Query paginated users
    users = db.query(User).offset(skip).limit(page_size).all()

    return {
        "total": total,          # Total number of users
        "page": page,            # Current page
        "page_size": page_size,  # Number of users per page
        "users": users           # List of users
    }

# Update user
def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete user
def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
