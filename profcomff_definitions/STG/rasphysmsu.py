from sqlalchemy import VARCHAR, Text
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class RawHtml(Base):
    url: Mapped[str] = mapped_column(VARCHAR(256), default=None)
    raw_html: Mapped[str] = mapped_column(Text, default=None)

    __mapper_args__ = {"primary_key": [url, raw_html]}  # Used only to correctly map ORM object to sql table


class RawHtmlOld(Base):
    url: Mapped[str] = mapped_column(VARCHAR(256), default=None)
    raw_html: Mapped[str] = mapped_column(Text, default=None)
    __mapper_args__ = {"primary_key": [url, raw_html]}  # Used only to correctly map ORM object to sql table