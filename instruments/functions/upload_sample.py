import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from .check_existing_table import check_existing_table


def upload_sample(table_class: str, limit: int, *args):
    """
    Uploads a sample of the given string of length from specified table.
    """
    table_class = check_existing_table(table_class)

    try:
        load_dotenv(".env")

        DB_DSN: str = os.getenv("DB_DSN", "postgresql://postgres:12345@localhost:5432/dwh")
        DB_ONLINE: str = os.getenv("DB_ONLINE", "")

        local_engine = create_engine(DB_DSN)
        remote_engine = create_engine(DB_ONLINE)

        local_session = sessionmaker(bind=local_engine)()
        remote_session = sessionmaker(bind=remote_engine)()

        # Суперкостыльная проверка подключения к бд
        local_session.execute(text('SELECT 1'))
        remote_session.execute(text('SELECT 1'))

    except (OperationalError, ArgumentError, UnicodeDecodeError) as e:
        logging.error(
            "Could not connect to database. Perhaps your login/password/database for your postgres is incorrect. Please, check if you have .env file in root folder with correct database link"
        )
        raise ConnectionError(e)

    # Собственно сама загрузка
    try:
        samples = remote_session.query(table_class).order_by(func.random()).limit(limit).all()
    except Exception as e:
        logging.error("Table does not exist in remote database. Please check migrations in remote database")
        raise ConnectionError(e)
    try:
        for sample in samples:
            local_sampe = local_session.merge(sample)
            local_session.add(local_sampe)
            local_session.commit()
    except Exception as e:
        logging.error("Table does not exist in local database. Please check your migrations")
        raise ConnectionError(e)
