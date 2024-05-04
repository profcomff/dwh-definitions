from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Receiver(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String, nullable=True)
    method: Mapped[str] = mapped_column(String, nullable=True)
    receiver_body: Mapped[dict] = mapped_column(JSON, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Alert(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    data = mapped_column(JSON, nullable=True)
    filter = mapped_column(String, nullable=True)
    create_ts = mapped_column(DateTime, nullable=True)


class Fetcher(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    type_: Mapped[str] = mapped_column("type", String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    fetch_data: Mapped[str] = mapped_column(String, nullable=True)
    delay_ok: Mapped[int] = mapped_column(Integer, nullable=True)
    delay_fail: Mapped[int] = mapped_column(Integer, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Metric(Base):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    name: Mapped[str] = mapped_column("name", String, nullable=True)
    ok: Mapped[bool] = mapped_column("ok", Boolean, nullable=True)
    time_delta: Mapped[float] = mapped_column(Float, nullable=True)
