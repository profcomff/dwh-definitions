import inspect

from sqlalchemy import create_engine, text
from sqlalchemy.exc import ArgumentError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

import profcomff_definitions
from profcomff_definitions.instruments.settings import get_settings


def upload_sample(table_class: str, limit: int, *args):
    """
    Uploads a sample of the given string of length from specified table.
    """
    # Получаем все классы таблиц/проверяем на дубли
    classes = inspect.getmembers(profcomff_definitions, inspect.isclass)
    matches = []
    for existing_class in classes:
        if existing_class[0] == table_class:
            matches.append(existing_class[1])
    if len(matches) == 0:
        raise ModuleNotFoundError("No matching class found for table " + table_class)
    if len(matches) > 1:
        print("Multiple matching classes found for table " + table_class)
        print("Please choose wich class should be imported")
        for i in range(len(matches)):
            print(f"{i})", matches[i])
        choice = int(input())
        if choice not in range(len(matches)):
            raise ValueError("Invalid choice")
        table_class = matches[choice]
    else:
        table_class = matches[0]

    try:
        settings = get_settings()
        local_engine = create_engine(settings.DB_DSN)
        remote_engine = create_engine(settings.DB_REMOTE)

        local_session = sessionmaker(bind=local_engine)()
        remote_session = sessionmaker(bind=remote_engine)()

        # Суперкостыльная проверка подключения к бд
        local_session.execute(text('SELECT 1'))
        remote_session.execute(text('SELECT 1'))

    except (OperationalError, ArgumentError, UnicodeDecodeError):
        raise ConnectionError(
            "Could not connect to database. Perhaps your login/password/database for your postgres is incorrect. Please, check if you have .env file in instruments folder with correct database link"
        )

    # Собственно сама загрузка
    samples = remote_session.query(table_class).order_by(func.random()).limit(limit).all()
    for sample in samples:
        local_sampe = local_session.merge(sample)
        local_session.add(local_sampe)
        local_session.commit()
