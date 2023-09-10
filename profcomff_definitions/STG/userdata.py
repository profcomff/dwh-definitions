from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Category(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    read_scope: Mapped[str] = mapped_column(String)
    update_scope: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Param(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
    is_required: Mapped[bool] = mapped_column(Boolean)
    changeable: Mapped[bool] = mapped_column(Boolean)
    type: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Source(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    trust_level: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
    )


class Info(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    param_id: Mapped[int] = mapped_column(Integer)
    source_id: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer)
    value: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
