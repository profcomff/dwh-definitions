from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimRoomAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    api_id: Mapped[int]
    name: Mapped[str | None]
    room_direction_text_type: Mapped[str | None]
    is_deleted: Mapped[bool]
    department: Mapped[str | None]


class DimLecturerAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    api_id: Mapped[int]
    first_name: Mapped[str | None]
    middle_name: Mapped[str | None]
    last_name: Mapped[str | None]
    avatar_id: Mapped[int | None]
    description: Mapped[str | None]


class DimGroupAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    api_id: Mapped[int]
    name: Mapped[str | None]
    number: Mapped[int | None]


class DimClassAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
