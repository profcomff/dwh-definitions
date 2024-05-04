from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Receiver(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str | None]
    method: Mapped[str | None]
    receiver_body: Mapped[str | None]
    create_ts: Mapped[datetime | None]


class Alert(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str | None]
    filter: Mapped[str | None]
    create_ts: Mapped[datetime | None]


class Fetcher(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str | None]
    address: Mapped[str | None]
    fetch_data: Mapped[str | None]
    delay_ok: Mapped[int | None]
    delay_fail: Mapped[int | None]
    create_ts: Mapped[datetime | None]


class Metric(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    ok: Mapped[bool | None]
    time_delta: Mapped[float | None]
