from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Lecturer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    subject: Mapped[str | None]
    avatar_link: Mapped[str | None]
    timetable_id: Mapped[int]


class Comment(Base):
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    create_ts: Mapped[datetime]
    update_ts: Mapped[datetime]
    subject: Mapped[str | None]
    text: Mapped[str | None]
    mark_kindness: Mapped[int]
    mark_freebie: Mapped[int]
    mark_clarity: Mapped[int]
    lecturer_id: Mapped[int]
    review_status: Mapped[str]


class LecturerUserComment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_id: Mapped[int]
    user_id: Mapped[int]
    create_ts: Mapped[datetime]
    update_ts: Mapped[datetime]
