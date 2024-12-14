import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Load environment variables from .env
from dotenv import load_dotenv
from app.db.models import Base  # Import your models
load_dotenv()

# Alembic Config object
config = context.config

# Configure logging
fileConfig(config.config_file_name)

# Get the DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")

# Update the sqlalchemy.url in the config dynamically
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Target metadata for autogenerate
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
