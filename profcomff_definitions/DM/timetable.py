import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimRoomAct(Base):
    """
    Справочник аудиторий
    """

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    timetable_alias: Mapped[str] = mapped_column(
        String,
        comment="Техническое поле для построения пайплайна сборки расписания",
        nullable=True,
    )
    room_api_id: Mapped[int]
    room_name: Mapped[str | None]
    room_direction_text_type: Mapped[str | None]
    room_department: Mapped[str | None]
    source_name: Mapped[str]


class DimLecturerAct(Base):
    """
    Справочник преподавателей
    """

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    timetable_alias: Mapped[str] = mapped_column(
        String,
        comment="Техническое поле для построения пайплайна сборки расписания",
        nullable=True,
    )
    lecturer_api_id: Mapped[int]
    lecturer_first_name: Mapped[str | None]
    lecturer_middle_name: Mapped[str | None]
    lecturer_last_name: Mapped[str | None]
    lecturer_avatar_id: Mapped[int | None]
    lecturer_description: Mapped[str | None]
    source_name: Mapped[str]


class DimGroupAct(Base):
    """
    Справочник групп
    """

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    timetable_alias: Mapped[str] = mapped_column(
        String,
        comment="Техническое поле для построения пайплайна сборки расписания",
        nullable=True,
    )
    group_api_id: Mapped[int]
    group_name_text: Mapped[str | None]
    group_number: Mapped[str | None]
    source_name: Mapped[str]


class DimEventAct(Base):
    """
    Справочник событий в расписании
    """

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    timetable_alias: Mapped[str] = mapped_column(
        String,
        comment="Техническое поле для построения пайплайна сборки расписания",
        nullable=True,
    )
    event_api_id: Mapped[int | None]
    event_name_text: Mapped[str | None]
    source_name: Mapped[str]


class DmTimetableAct(Base):
    """
    Витрина событий расписания.
    Строится на справочниках групп, предметов, преподавателей и аудиторий.
    Гранулярность витрины - event_id - идентична гранулярности источника ODS_TIMETABLE.ods_timetable_act
    """

    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID, comment="Идентификатор события, из таблицы ODS_TIMETABLE.ods_timetable_act", primary_key=True
    )
    name: Mapped[str] = mapped_column(comment="Название события")
    odd: Mapped[bool] = mapped_column(comment="Флаг: событие относится к нечетной неделе")
    even: Mapped[bool] = mapped_column(comment="Флаг: событие относится к четной неделе")
    weekday: Mapped[int] = mapped_column(comment="Номер недели")
    num: Mapped[int] = mapped_column(comment="Номер события")
    start: Mapped[str] = mapped_column(comment="Время начала события (в строке)")
    end: Mapped[str] = mapped_column(comment="Время конца события (в строке)")
    group: Mapped[str] = mapped_column(comment="Академическая группа, к которой относится событие")
    event_name: Mapped[str | None] = mapped_column(comment="Название события из справочника. Заполняется всегда")
    group_name: Mapped[str | None] = mapped_column(
        comment="Название группы из справочника. Заполняется если в событии есть информация о группе"
    )
    lecturer_name: Mapped[str | None] = mapped_column(
        comment="Имя преподавателя из справочника. Заполняется если в событии есть информация о преподавателе"
    )
    room_name: Mapped[str | None] = mapped_column(
        comment="Название аудитори из справочника. Заполняется если в событии есть информация об аудитории"
    )
    event_api_id: Mapped[int | None] = mapped_column(comment="Идентификатор события из справочника. Заполняется всегда")
    group_api_id: Mapped[int | None] = mapped_column(
        comment="Идентификатор группы из справочника. Заполняется если в событии есть информация о группе"
    )
    lecturer_api_id: Mapped[int | None] = mapped_column(
        comment="Идентификатор преподавателя из справочника. Заполняется если в событии есть информация о преподавателе"
    )
    room_api_id: Mapped[int | None] = mapped_column(
        comment="Идентификатор аудитори из справочника. Заполняется если в событии есть информация об аудитории"
    )
