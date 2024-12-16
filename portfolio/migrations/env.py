import os
import sys

# Add root folder to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from portfolio.core.config import settings
from portfolio.db.base_class import Base
from db import *
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Logs config
config = context.config
fileConfig(config.config_file_name)

# Métadonnées des modèles SQLAlchemy
target_metadata = Base.metadata

# Explicit DB Url for containers
database_url = str(settings.DATABASE_URL)  # Force value as string
config.set_main_option("sqlalchemy.url", database_url)

def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
