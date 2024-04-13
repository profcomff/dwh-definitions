from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func, EmailType
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Contacts(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    email = sa.Column(EmailType)
    phone: Mapped[int] = mapped_column(Integer, nullable=True)
    workplace: Mapped[int] = mapped_column(Integer, nullable=True)
    upload_ts: Mapped[datetime] = mapped_column(DateTime, default=func.now())
