from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    event_text: Mapped[str] = mapped_column(String, nullable=True)
    time_interval_text: Mapped[str] = mapped_column(String, nullable=True)
    group_text: Mapped[str] = mapped_column(String, nullable=True)

    group: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    scope: Mapped[JSON] = mapped_column(JSON)
    token: Mapped[JSON] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
