from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class RawTimetableApi(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]
    discipline_name: Mapped[str]
    discipline_id: Mapped[int]
    classroom_name: Mapped[str]
    classroom_id: Mapped[int]
    lesson_type_text: Mapped[str]
    lesson_from_dttm_ts: Mapped[datetime] = mapped_column(TIMESTAMP)
    lesson_to_dttm_ts: Mapped[datetime] = mapped_column(TIMESTAMP)
    teacher_users: Mapped[dict] = mapped_column(JSON)
    study_groups: Mapped[dict] = mapped_column(JSON)
