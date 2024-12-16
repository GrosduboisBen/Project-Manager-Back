from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Load DATABASE_URL from settings
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
