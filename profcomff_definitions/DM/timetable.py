
import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimRoomAct(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    room_api_id: Mapped[int]
    room_name: Mapped[str | None]
    room_direction_text_type: Mapped[str | None]
    room_department: Mapped[str | None]
    source_name: Mapped[str]


class DimLecturerAct(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    lecturer_api_id: Mapped[int]
    lecturer_first_name: Mapped[str | None]
    lecturer_middle_name: Mapped[str | None]
    lecturer_last_name: Mapped[str | None]
    lecturer_avatar_id: Mapped[int | None]
    lecturer_description: Mapped[str | None]
    source_name: Mapped[str]


class DimGroupAct(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    group_api_id: Mapped[int]
    group_name_text: Mapped[str | None]
    group_number: Mapped[str | None]
    source_name: Mapped[str]


class DimEventAct(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    event_api_id: Mapped[int | None]
    event_name_text: Mapped[str | None]
    source_name: Mapped[str]
