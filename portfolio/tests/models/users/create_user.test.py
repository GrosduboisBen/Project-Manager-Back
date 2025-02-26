from sqlalchemy.orm import Session
from portfolio.crud.users import create_user
from portfolio.schemas.users import UserCreate

def test_create_user(db: Session):
    user_data = UserCreate(
        name="Test User",
        email="test@example.com",
        password="testpassword123",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        main_job="Front end developper"
    
    )
    user = create_user(db, user_data)
    assert user.creation_date is not None
    assert user.name == "Test User"
