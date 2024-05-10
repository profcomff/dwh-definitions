from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimRoomAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    api_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str | None]
    cabinet_direction_text_type: Mapped[str | None]
    is_deleted: Mapped[bool]
    department: Mapped[str | None]
