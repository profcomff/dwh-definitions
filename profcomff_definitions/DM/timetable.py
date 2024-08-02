from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimRoomAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    room_api_id: Mapped[int]
    room_name: Mapped[str | None]
    room_direction_text_type: Mapped[str | None]
    room_is_deleted: Mapped[bool]
    room_department: Mapped[str | None]
    source_name: Mapped[str | None]


class DimLecturerAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_api_id: Mapped[int]
    lecturer_first_name: Mapped[str | None]
    lecturer_middle_name: Mapped[str | None]
    lecturer_last_name: Mapped[str | None]
    lecturer_avatar_id: Mapped[int | None]
    lecturer_description: Mapped[str | None]
    source_name: Mapped[str | None]


class DimGroupAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_api_id: Mapped[int]
    group_name_text: Mapped[str | None]
    group_number: Mapped[int | None]
    source_name: Mapped[str | None]


class DimEventAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_name_text: Mapped[str | None]
    source_name: Mapped[str | None]
