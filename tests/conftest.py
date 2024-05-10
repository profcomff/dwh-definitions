import os
from pathlib import Path
from typing import Generator

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from alembic.command import downgrade, upgrade
from alembic.script import Script, ScriptDirectory
from sqlalchemy.engine import Engine


REPO_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.resolve()


@pytest.fixture
def alembic_config():
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', str(REPO_ROOT / "migrations"))
    alembic_cfg.set_main_option('sqlalchemy.url', "postgresql://postgres:postgres@localhost:5432/postgres")
    return alembic_cfg


@pytest.fixture
def revisions(alembic_config: Config) -> list[Script]:
    revisions_dir = ScriptDirectory.from_config(alembic_config)
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions



def test_migrations_stairway(alembic_config: Config, revisions: list[Script]) -> None:
    for revision in revisions:
        upgrade(alembic_config, revision.revision)
        downgrade(alembic_config, revision.down_revision or "-1")
        upgrade(alembic_config, revision.revision)


@pytest.fixture()
def engine() -> Generator[Engine, None, None]:
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
    yield engine


@pytest.fixture()
def migration(alembic_config: Config) -> Generator[None, None, None]:
    command.upgrade(alembic_config, 'head')
    command.revision(alembic_config, autogenerate=True, message="tests")
    command.upgrade(alembic_config, 'head')
    yield
    command.downgrade(alembic_config, 'head-1')
