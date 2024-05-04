from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Contacts(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    email: Mapped[str | None]
    phone: Mapped[str | None]
    workplace: Mapped[str | None]
    upload_ts: Mapped[datetime | None]
