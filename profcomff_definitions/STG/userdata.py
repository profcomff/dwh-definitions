from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Final

from sqlalchemy import Boolean, DateTime
from sqlalchemy import Enum as DbEnum
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ViewType(str, Enum):
    """
    Тип отображения пользоватльских данных в ответе `GET /user/{user_id}`
    ALL: {category: {param: [val1, val2, ...]}}
    LAST: {category: {param: last_modified_value}}
    MOST_TRUSTED: {category: {param: most_trusted_value}}
    """

    ALL: Final[str] = "all"
    LAST: Final[str] = "last"
    MOST_TRUSTED: Final[str] = "most_trusted"


class Category(Base):
    """
    Категория - объеденение параметров пользовательских данных.
    Если параметром может быть, например, номер студенческого и номер профсоюзного,
    то категорией, их объединяющей, может быть "студенческая информация" или "документы"
    """

    name: Mapped[str] = mapped_column(String, primary_key=True)
    read_scope: Mapped[str] = mapped_column(String)
    update_scope: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Param(Base):
    """
    Параметр - находится внутри категории,
    к нему можно задавать значение у конкретного пользователя.
    Например, параметрами может являться почта и номер телефона,
    а параметры эти могут лежать в категории "контакты"
    """

    name: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_required: Mapped[bool] = mapped_column(Boolean)
    changeable: Mapped[bool] = mapped_column(Boolean)
    type: Mapped[ViewType] = mapped_column(DbEnum(ViewType, native_enum=False))
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Source(Base):
    """
    Источник данных - субъект изменения польщовательских данных - тот, кто меняет данные
    В HTTP методах доступно только два источника - user/admin
    Субъект может менять только данные, созданные собой же.
    У источника есть уровень доверия, который влияет на вид ответа `GET /user/{user_id}`
    """

    name: Mapped[str] = mapped_column(String, primary_key=True)
    trust_level: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
    )


class Info(Base):
    """
    Значения параметров для конкретных польщзователей
    Если, например, телефон - параметр, то здесь указывается его значение для
    польщзователя(owner_id) - объекта изменения пользовательских данных
    """

    param_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_id: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer)
    value: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
