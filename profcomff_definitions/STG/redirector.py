from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Link(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    url_from: Mapped[str] = mapped_column(unique=True)
    url_to: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]


class RedirectFact(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    link_id: Mapped[int | None]
    method: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user_agent: Mapped[str]
    browser_family: Mapped[str | None]
    browser_version: Mapped[str | None]
    os_family: Mapped[str | None]
    os_version: Mapped[str | None]
    device_family: Mapped[str | None]
    device_brand: Mapped[str | None]
    device_model: Mapped[str | None]
