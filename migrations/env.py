from __future__ import with_statement
from app.dao.models import BaseModel
from app.config.db_config import DBConfig
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Add your model's module to the sys.path
# This allows Alembic to find the models
sys.path.append(os.path.join(os.path.dirname(__file__), "app"))


# construct the SQLAlchemy database URL
DATABASE_URL = f"postgresql://{DBConfig.PG_USERNAME}:{
    DBConfig.PG_PASSWORD}@{DBConfig.PG_HOST}:{DBConfig.PG_PORT}/{DBConfig.PG_NAME}"

# update the Alembic config with the constructed SQLAlchemy URL
config = context.config
config.set_section_option("alembic", "sqlalchemy.url", DATABASE_URL)

# Import your SQLAlchemy BaseModel and metadata here

# This will be the metadata object that Alembic uses for autogeneration
target_metadata = BaseModel.metadata  # Use your actual metadata object

# Alembic's configuration object, used for database URL, etc.
config = context.config

# Set up logging
fileConfig(config.config_file_name)

# Configure the database engine


def run_migrations_online():
    # Pull the database URL from the Alembic config
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Pass the metadata to the context.configure method
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,  # This is where you pass the metadata
            compare_type=True,  # Optionally, this will compare column types as well
        )

        # Run migrations
        with context.begin_transaction():
            context.run_migrations()


# Run the migration online
run_migrations_online()
