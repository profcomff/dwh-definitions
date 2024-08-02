from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, TIMESTAMP
from profcomff_definitions.base import Base

class RawTimetableApi(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]
    discipline_name: Mapped[str]
    discipline_id: Mapped[int]
    classroom_name: Mapped[str]
    classroom_id: Mapped[int]
    lesson_type_text: Mapped[str]
    lesson_from_dttm_ts: Mapped[TIMESTAMP]
    lesson_to_dttm_ts: Mapped[TIMESTAMP]
    teacher_users: Mapped[JSON]
    study_groups: Mapped[JSON]