import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


REPO_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.resolve()


@pytest.fixture(scope='session')
def migration() -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', str(REPO_ROOT / "migrations"))
    alembic_cfg.set_main_option('sqlalchemy.url', "postgresql://postgres:postgres@localhost:5432/postgres")
    command.revision(alembic_cfg, autogenerate=True, message="tests")
    command.upgrade(alembic_cfg, 'head')
    yield migration
    command.downgrade(alembic_cfg, '-1')


@pytest.fixture()
def engine() -> Engine:
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
    yield engine
