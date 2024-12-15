from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn, field_validator

class Settings(BaseSettings):
    # DB Config
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_HOST: str = "db"
    DATABASE_PORT: int = 5432
    DATABASE_URL: PostgresDsn = Field(default=None)

    # App config
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "Project Manager ( Portfolio )"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_database_url(cls, v, values):
        """
        Generate DATABASE_URL if not correctly define
        """
        if v:
            return v
        return (
            f"postgresql+psycopg2://{values['POSTGRES_USER']}:"
            f"{values['POSTGRES_PASSWORD']}@{values['DATABASE_HOST']}:"
            f"{values['DATABASE_PORT']}/{values['POSTGRES_DB']}"
        )


    class Config:
        env_file = ".env"
settings = Settings()
