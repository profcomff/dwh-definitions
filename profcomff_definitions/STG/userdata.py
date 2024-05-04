from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    read_scope: Mapped[str | None]
    update_scope: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class Param(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    category_id: Mapped[int | None]
    is_required: Mapped[bool | None]
    changeable: Mapped[bool | None]
    type: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class Source(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    trust_level: Mapped[int | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class Info(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    param_id: Mapped[int | None]
    source_id: Mapped[int | None]
    owner_id: Mapped[int | None]
    value: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
