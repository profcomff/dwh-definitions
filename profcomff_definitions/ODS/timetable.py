from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    event_text: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
    time_interval_text: Mapped[str | None] = mapped_column(String, nullable=True)
    group_text: Mapped[str | None] = mapped_column(String, nullable=True)
    __mapper_args__ = {
        "primary_key": [event_text, time_interval_text, group_text]
    }  # Used only to correctly map ORM object to sql table


class OdsLinkTimetableTeacher(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    group: Mapped[str | None] = mapped_column(String, nullable=True)
    event_tr: Mapped[str | None] = mapped_column(String, nullable=True)
    teacher_id: Mapped[str | None] = mapped_column(Integer, nullable=True)


class OdsLinkTimetableLesson(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    group: Mapped[str | None] = mapped_column(String, nullable=True)
    event_tr: Mapped[str | None] = mapped_column(String, nullable=True)
    lesson_id: Mapped[str | None] = mapped_column(Integer, nullable=True)


class OdsLinkTimetableGroup(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    group: Mapped[str | None] = mapped_column(String, nullable=True)
    event_tr: Mapped[str | None] = mapped_column(String, nullable=True)
    group_id: Mapped[str | None] = mapped_column(Integer, nullable=True)


class OdsLinkTimetableCabinet(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    group: Mapped[str | None] = mapped_column(String, nullable=True)
    event_tr: Mapped[str | None] = mapped_column(String, nullable=True)
    cabinet_id: Mapped[str | None] = mapped_column(Integer, nullable=True)
