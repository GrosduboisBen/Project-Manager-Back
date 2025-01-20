from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from portfolio.core.config import settings
# Load DATABASE_URL from settings
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()