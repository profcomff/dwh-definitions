from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    """
    Таблица содержит десериализованные события с сайта ras.phys.msu
    Выделяется блок текста из общей таблицы, нужна для обновления расписания в приложении ТвойФФ
    """
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    name: Mapped[str] = mapped_column(comment="Название события")
    odd: Mapped[bool] = mapped_column(comment="Флаг: событие относится к нечетной неделе")
    even: Mapped[bool] = mapped_column(comment="Флаг: событие относится к четной неделе") 
    weekday: Mapped[int] = mapped_column(comment="Номер недели")
    num: Mapped[int] = mapped_column(comment="Номер события")
    start: Mapped[str] = mapped_column(comment="Время начала события (в строке)")
    end: Mapped[str] = mapped_column(comment="Время конца события (в строке)")
    group: Mapped[str] = mapped_column(comment="Академическая группа, к которой относится событие")


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
