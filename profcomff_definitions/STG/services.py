from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    order: Mapped[int | None]
    name: Mapped[str | None]
    type: Mapped[str | None]


class Button(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    order: Mapped[int | None]
    category_id: Mapped[int | None]
    icon: Mapped[str | None]
    link: Mapped[str | None]
    type: Mapped[str | None]


class Scope(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    category_id: Mapped[int | None]
    button_id: Mapped[int | None]
    is_required: Mapped[bool | None]
