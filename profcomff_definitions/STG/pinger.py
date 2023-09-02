"""Классы хранения настроек нотификаций
"""
from datetime import datetime
from enum import Enum

import sqlalchemy
from sqlalchemy import JSON, Boolean, DateTime
from sqlalchemy import Enum as DbEnum
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Method(str, Enum):
    POST: str = "post"
    GET: str = "get"


class Receiver(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String)
    method: Mapped[Method] = mapped_column(DbEnum(Method, native_enum=False))
    receiver_body: Mapped[dict] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)


class Alert(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    data = mapped_column(JSON)
    filter = mapped_column(String)
    create_ts = mapped_column(DateTime)


class FetcherType(str, Enum):
    GET = "get"
    POST = "post"
    PING = "ping"


class Fetcher(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    type_: Mapped[FetcherType] = mapped_column("type", sqlalchemy.Enum(FetcherType, native_enum=False))
    address: Mapped[str] = mapped_column(String)
    fetch_data: Mapped[str] = mapped_column(String)
    delay_ok: Mapped[int] = mapped_column(Integer)
    delay_fail: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime] = mapped_column(DateTime)


class Metric(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    name: Mapped[str] = mapped_column("name", String)
    ok: Mapped[bool] = mapped_column("ok", Boolean)
    time_delta: Mapped[float] = mapped_column(Float)
