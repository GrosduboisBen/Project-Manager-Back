from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Charger DATABASE_URL depuis les settings
DATABASE_URL = settings.DATABASE_URL

# Créer le moteur SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Créer une session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
