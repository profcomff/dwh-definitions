from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Integer, String, Text
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


class Room(Base):
    name: Mapped[str] = mapped_column(String, primary_key=True)
    direction: Mapped[str] = mapped_column(String)
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


class Photo(Base):
    lecturer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    link: Mapped[str] = mapped_column(String)
    approve_status: Mapped[str] = mapped_column(String)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class CommentLecturer(Base):
    lecturer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class CommentEvent(Base):
    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
