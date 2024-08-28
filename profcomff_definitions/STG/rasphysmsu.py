import typing as tp

from sqlalchemy import ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class RawHtml(Base):
    url: Mapped[str] = mapped_column(primary_key=True)
    raw_html: Mapped[str | None]


class RawHtmlOld(Base):
    url: Mapped[str] = mapped_column(primary_key=True)
    raw_html: Mapped[str | None]


class Diff(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str]
    odd: Mapped[bool]
    even: Mapped[bool]
    weekday: Mapped[int | None]
    num: Mapped[int | None]
    start: Mapped[str]
    end: Mapped[str]
    place: Mapped[tp.List[int]] = mapped_column(ARRAY(Integer))
    group: Mapped[tp.List[int]] = mapped_column(ARRAY(Integer))
    teacher: Mapped[tp.List[int]] = mapped_column(ARRAY(Integer))
    events_id: Mapped[tp.List[int]] = mapped_column(ARRAY(Integer))
