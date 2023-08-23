import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

import migrations.schema
import profcomff_definitions
from profcomff_definitions.base import Base


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def process_revision_directives(context, revision, directives):
    # Upgrade sort
    script = directives[0].upgrade_ops_list[0].ops
    names = [obj.__class__.__name__ for obj in script]
    indexes = [i for i, ltr in enumerate(names) if ltr == "CreateTableSchemaOp"]
    i = 0
    for index in indexes:
        tmp = script[i]
        script[i] = script[index]
        script[index] = tmp
        i += 1

    # Downgrade sort
    script = directives[0].downgrade_ops_list[0].ops
    names = [obj.__class__.__name__ for obj in script]
    indexes = [i for i, ltr in enumerate(names) if ltr == "DropTableSchemaOp"]
    i = -1
    for index in indexes:
        tmp = script[i]
        script[i] = script[index]
        script[index] = tmp
        i -= 1


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = os.getenv('DB_DSN', 'postgresql://postgres:12345@localhost:5432/postgres')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        version_table_schema='public',
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv('DB_DSN', 'postgresql://postgres:12345@localhost:5432/postgres')
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema='public',
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
