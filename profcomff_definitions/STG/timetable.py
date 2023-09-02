"""Database common classes and methods
"""
from __future__ import annotations

from datetime import datetime
from enum import Enum

from sqlalchemy import JSON, Boolean, DateTime
from sqlalchemy import Enum as DbEnum
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Credentials(Base):
    """User credentials"""

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    scope: Mapped[JSON] = mapped_column(JSON)
    token: Mapped[JSON] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)


class Direction(str, Enum):
    NORTH: str = "North"
    SOUTH: str = "South"


class Room(Base):
    name: Mapped[str] = mapped_column(String, primary_key=True)
    direction: Mapped[Direction] = mapped_column(DbEnum(Direction, native_enum=False))
    building: Mapped[str] = mapped_column(String)
    building_url: Mapped[str] = mapped_column(String)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Lecturer(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    middle_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    avatar_id: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Group(Base):
    name: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class Event(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    start_ts: Mapped[datetime] = mapped_column(DateTime)
    end_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class EventsLecturers(Base):
    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lecturer_id: Mapped[int] = mapped_column(Integer)


class EventsRooms(Base):
    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[int] = mapped_column(Integer)


class EventsGroups(Base):
    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)


class ApproveStatuses(str, Enum):
    APPROVED: str = "Approved"
    DECLINED: str = "Declined"
    PENDING: str = "Pending"


class Photo(Base):
    lecturer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    link: Mapped[str] = mapped_column(String)
    approve_status: Mapped[ApproveStatuses] = mapped_column(DbEnum(ApproveStatuses, native_enum=False))
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class CommentLecturer(Base):
    lecturer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[ApproveStatuses] = mapped_column(DbEnum(ApproveStatuses, native_enum=False))
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class CommentEvent(Base):
    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[ApproveStatuses] = mapped_column(DbEnum(ApproveStatuses, native_enum=False))
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
