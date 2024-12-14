import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    """
    Таблица содержит десериализованные события с сайта ras.phys.msu
    Выделяется блок текста из общей таблицы, нужна для обновления расписания в приложении ТвойФФ
    """

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(comment="Название события")
    odd: Mapped[bool] = mapped_column(comment="Флаг: событие относится к нечетной неделе")
    even: Mapped[bool] = mapped_column(comment="Флаг: событие относится к четной неделе")
    weekday: Mapped[int] = mapped_column(comment="Номер недели")
    num: Mapped[int] = mapped_column(comment="Номер события")
    start: Mapped[str] = mapped_column(comment="Время начала события (в строке)")
    end: Mapped[str] = mapped_column(comment="Время конца события (в строке)")
    group: Mapped[str] = mapped_column(comment="Академическая группа, к которой относится событие")


class OdsLinkTimetableTeacher(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Идентификатор события, полученного в результате парсинга ras.phys.msu",
        nullable=True,
    )
    teacher_id: Mapped[uuid.UUID | None] = mapped_column(UUID, nullable=True)


class OdsLinkTimetableLesson(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Идентификатор события, полученного в результате парсинга ras.phys.msu",
        nullable=True,
    )
    lesson_id: Mapped[uuid.UUID | None] = mapped_column(UUID, nullable=True)


class OdsLinkTimetableGroup(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Идентификатор события, полученного в результате парсинга ras.phys.msu",
        nullable=True,
    )
    group_id: Mapped[uuid.UUID | None] = mapped_column(UUID, nullable=True)


class OdsLinkTimetableRoom(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Идентификатор события, полученного в результате парсинга ras.phys.msu",
        nullable=True,
    )
    room_id: Mapped[uuid.UUID | None] = mapped_column(UUID, nullable=True)


class OdsManualTimetableConstraints(Base):
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Идентификатор события, полученного в результате парсинга ras.phys.msu",
        primary_key=True,
    )
    empty_room_flg: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Флаг: в событии не указан кабинет",
        nullable=True,
    )
    empty_lecturer_flg: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Флаг: в событии не указан преподаватель",
        nullable=True,
    )
    empty_group_flg: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Флаг: в событии не указана группа",
        nullable=True,
    )
    empty_group_flg: Mapped[uuid.UUID] = mapped_column(
        UUID,
        comment="Флаг: в событии не указан премет",
        nullable=True,
    )
