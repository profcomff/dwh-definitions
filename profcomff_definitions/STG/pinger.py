"""Классы хранения настроек нотификаций
"""
from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Receiver(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String)
    method: Mapped[str] = mapped_column(String)
    receiver_body: Mapped[dict] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)


class Alert(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    data = mapped_column(JSON)
    filter = mapped_column(String)
    create_ts = mapped_column(DateTime)


class Fetcher(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    type_: Mapped[str] = mapped_column("type", String)
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
