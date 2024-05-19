from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableAct(Base):
    event_text: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
    time_interval_text: Mapped[str | None] = mapped_column(String, nullable=True)
    group_text: Mapped[str | None] = mapped_column(String, nullable=True)
    __mapper_args__ = {
        "primary_key": [event_text, time_interval_text, group_text]
    }  # Used only to correctly map ORM object to sql table
