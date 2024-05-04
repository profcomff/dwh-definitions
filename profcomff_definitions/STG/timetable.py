from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Credentials(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group: Mapped[str | None]
    email: Mapped[str | None]
    scope: Mapped[str | None]
    token: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]


class Room(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    direction: Mapped[str | None]
    building: Mapped[str | None]
    building_url: Mapped[str | None]
    is_deleted: Mapped[bool | None]


class Lecturer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str | None]
    middle_name: Mapped[str | None]
    last_name: Mapped[str | None]
    avatar_id: Mapped[int | None]
    description: Mapped[str | None]
    is_deleted: Mapped[bool | None]


class Group(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    number: Mapped[str | None]
    is_deleted: Mapped[bool | None]


class Event(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    start_ts: Mapped[datetime | None]
    end_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class EventsLecturers(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int | None]
    lecturer_id: Mapped[int | None]


class EventsRooms(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int | None]
    room_id: Mapped[int | None]


class EventsGroups(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int | None]
    group_id: Mapped[int | None]


class Photo(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_id: Mapped[int | None]
    link: Mapped[str | None]
    approve_status: Mapped[str | None]
    is_deleted: Mapped[bool | None]


class CommentLecturer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_id: Mapped[int | None]
    author_name: Mapped[str | None]
    text: Mapped[str | None]
    approve_status: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class CommentEvent(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int | None]
    author_name: Mapped[str | None]
    text: Mapped[str | None]
    approve_status: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
