from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DimCabnetAct(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(nullable=False)
    cabinet_direction_text_type: Mapped[str | None]
    is_deleted: Mapped[bool]
    department: Mapped[str | None]
