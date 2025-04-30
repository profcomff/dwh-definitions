from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Item(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type_id: Mapped[int]
    is_available: Mapped[bool]


class ItemType(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    image_url: Mapped[str | None]
    description: Mapped[str | None]


class RentalSession(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    item_id: Mapped[int]
    admin_open_id: Mapped[int]
    admin_close_id: Mapped[int | None]
    reservation_ts: Mapped[datetime]
    start_ts: Mapped[datetime]
    end_ts: Mapped[datetime]
    actual_return_ts: Mapped[datetime]
    status: Mapped[str]


class Event(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    admin_id: Mapped[int]
    session_id: Mapped[int]
    action_type: Mapped[str]
    details: Mapped[str]
    create_ts: Mapped[datetime]


class Strike(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    admin_id: Mapped[int]
    reason: Mapped[str]
    create_ts: Mapped[datetime]
    session_id: Mapped[int]
