from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Database variables
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str = Field(default=None)

    # Application configuration
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "Portfolio"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Reconstruire DATABASE_URL si non défini directement
        if not self.DATABASE_URL:
            self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db:5432/{self.POSTGRES_DB}"

# Instanciation des paramètres
settings = Settings()
