from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from profcomff_definitions.base import Base


class Item(Base):
    api_id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int]
    is_available: Mapped[bool]
    type: Mapped[str]


class ItemType(Base):
    api_id: Mapped[int]
    name: Mapped[str]
    image_url: Mapped[str | None]
    description: Mapped[str | None]


class RentalSession(Base):
    api_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    item_id: Mapped[int]
    admin_open_id: Mapped[int]
    admin_close_id: Mapped[int | None]
    reservation_ts: Mapped[datetime.datetime]
    start_ts: Mapped[datetime.datetime]
    end_ts: Mapped[datetime.datetime]
    actual_return_ts: Mapped[datetime.datetime]
    status: Mapped[str]


class Event(Base):
    api_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    admin_id: Mapped[int]
    session_id: Mapped[int]
    action_type: Mapped[str]
    details: Mapped[dict]
    create_ts: Mapped[datetime.datetime]


class Strike(Base):
    api_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    session_id: Mapped[int]
    admin_id: Mapped[int]
    reason: Mapped[str]
    create_ts: Mapped[datetime.datetime]
