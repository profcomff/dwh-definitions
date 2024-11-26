from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    """
    Сырая информация спаршенная из html страниц расписания, хранит данные о времени, дне недели и периодичности пары(каждая неделя или через неделю)
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    odd: Mapped[bool]
    even: Mapped[bool]
    weekday: Mapped[int]
    num: Mapped[int]
    start: Mapped[str]
    end: Mapped[str]
    group: Mapped[str]


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
