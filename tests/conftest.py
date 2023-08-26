import pytest
import dotenv
from alembic.config import Config
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from alembic import command
from pathlib import Path
import os

REPO_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.resolve()
dotenv.load_dotenv("../.env")
DB_DSN = os.getenv("TEST_DB")


@pytest.fixture(scope='session')
def migration() -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', str(REPO_ROOT / "migrations"))
    alembic_cfg.set_main_option('sqlalchemy.url', "postgresql://postgres:12345@localhost:5432/test")
    command.revision(alembic_cfg, autogenerate=True, message="tests")
    command.upgrade(alembic_cfg, 'head')
    yield migration
    command.downgrade(alembic_cfg, '-1')


@pytest.fixture()
def engine() -> Engine:
    engine = create_engine("postgresql://postgres:12345@localhost:5432/test")
    yield engine
