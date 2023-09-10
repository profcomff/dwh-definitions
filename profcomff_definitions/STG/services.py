from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Category(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)


class Button(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    order: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(Integer)
    icon: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)


class Scope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
