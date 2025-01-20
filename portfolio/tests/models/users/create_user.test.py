from sqlalchemy.orm import Session
from portfolio.crud.users import create_user
from portfolio.schemas.users import UserCreate

def test_create_user(db: Session):
    user_data = UserCreate(
        name="Test User",
        email="test@example.com",
        password="testpassword123"
    )
    user = create_user(db, user_data)
    assert user.creation_date is not None
    assert user.name == "Test User"
