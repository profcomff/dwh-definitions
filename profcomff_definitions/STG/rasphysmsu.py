from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class RawHtml(Base):
    url: Mapped[str] = mapped_column(primary_key=True)
    raw_html: Mapped[str | None]


class RawHtmlOld(Base):
    url: Mapped[str] = mapped_column(primary_key=True)
    raw_html: Mapped[str | None]
