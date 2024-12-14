from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # Import centralized settings

# Database URL from settings
DATABASE_URL = settings.DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session maker for dependency injection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class for models
Base = declarative_base()

# Dependency for database session
def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
