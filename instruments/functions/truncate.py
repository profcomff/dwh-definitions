import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from .check_existing_table import check_existing_table


def truncate(table_class: str, *args):
    """
    Clears your local database from records. (in progress)
    """
    table_class = check_existing_table(table_class)

    try:
        load_dotenv(".env")

        DB_DSN: str = os.getenv("DB_DSN", "postgresql://postgres:12345@localhost:5432/dwh")

        local_engine = create_engine(DB_DSN)
        local_session = sessionmaker(bind=local_engine)()

        # Суперкостыльная проверка подключения к бд
        local_session.execute(text('SELECT 1'))

    except (OperationalError, ArgumentError, UnicodeDecodeError):
        raise ConnectionError(
            "Could not connect to database. Perhaps your login/password/database for your postgres is incorrect. Please, check if you have .env file in instruments folder with correct database link"
        )

    # Собственно само удаление
    try:
        local_session.query(table_class).limit(1).one_or_none()
    except:
        raise ConnectionError("Table does not exist in database. Please check your migrations")
    local_session.execute(
        text(f'''TRUNCATE TABLE "{table_class.__table_args__["schema"].upper()}".{table_class.__tablename__}''')
    )
    local_session.commit()
