import os
from pathlib import Path
from typing import Generator

import pytest
from alembic.command import downgrade, revision, upgrade
from alembic.config import Config
from alembic.script import Script, ScriptDirectory
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


REPO_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.resolve()


@pytest.fixture
def alembic_config():
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', str(REPO_ROOT / "migrations"))
    alembic_cfg.set_main_option(
        'sqlalchemy.url', os.getenv("DB_DSN") or "postgresql://postgres:postgres@localhost:5432/postgres"
    )  # db for migration tests
    return alembic_cfg


@pytest.fixture
def revisions(alembic_config: Config) -> list[Script]:
    revisions_dir = ScriptDirectory.from_config(alembic_config)
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions


def test_migrations_stairway(alembic_config: Config, revisions: list[Script]) -> None:
    for revision in revisions:
        down_revision = revision.down_revision or "-1"
        if isinstance(down_revision, tuple):
            down_revision = down_revision[0]
        upgrade(alembic_config, revision.revision)
        downgrade(alembic_config, down_revision)
        upgrade(alembic_config, revision.revision)


### @mixx3 these tests is obsolete, TODO write generation tests for lib
# @pytest.fixture
# def generator_alembic_config():
#     alembic_cfg = Config(str(REPO_ROOT / "generation_test_alembic.ini"))
#     alembic_cfg.set_main_option('sqlalchemy.url', os.getenv("DB_DSN") or "postgresql://postgres:postgres@localhost:5432/postgres")  # db for migration tests
#     return alembic_cfg


# @pytest.fixture
# def test_do_generate_migration(generator_alembic_config: Config) -> Generator[None, None, None]:
#     upgrade(generator_alembic_config, 'head')
#     revision(generator_alembic_config, autogenerate=True, message="tests")
#     upgrade(generator_alembic_config, 'head')
#     yield
#     downgrade(generator_alembic_config, 'head-1')


@pytest.fixture()
def engine() -> Generator[Engine, None, None]:
    engine = create_engine(os.getenv("DB_DSN") or "postgresql://postgres:postgres@localhost:5432/postgres")
    yield engine
