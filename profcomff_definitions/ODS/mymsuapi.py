from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class OdsTimetableApiFlattened(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]
    discipline_name: Mapped[str]
    discipline_id: Mapped[int]
    classroom_name: Mapped[str]
    classroom_id: Mapped[int]
    lesson_type_text: Mapped[str]
    lesson_from_dttm_ts: Mapped[datetime]
    lesson_to_dttm_ts: Mapped[datetime]
    teacher_full_name: Mapped[str]
    study_group_id: Mapped[int]
    study_group_name: Mapped[str]
