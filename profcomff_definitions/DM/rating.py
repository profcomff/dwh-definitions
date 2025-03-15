from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DmLecturerCommentAct(Base):
    """
    Snapshot table that shows sizes for all tables in DWH
    """

    comment_api_uuid: Mapped[UUID] = mapped_column(comment="Идентифиактор в rating-api")
    lecturer_api_id: Mapped[int] = mapped_column(comment="Идентифиактор в rating-api")
    lecturer_full_name: Mapped[str | None] = mapped_column(comment="ФИО преподавателя")
    lecturer_first_name: Mapped[str | None] = mapped_column(comment="Имя преподавателя")
    lecturer_last_name: Mapped[str | None] = mapped_column(comment="Фамилия преподавателя")
    lecturer_middle_name: Mapped[str | None] = mapped_column(comment="ОТчество преподавателя")
    timetable_id: Mapped[int | None] = mapped_column(comment="Идертификатор в timetable-api")
    has_timetable_id: Mapped[bool] = mapped_column(comment="Флаг: есть ли преподаватель в расписании")
    lecturer_subject: Mapped[str | None] = mapped_column(comment="Предмет, относящийся к преподавателю")
    comment_subject: Mapped[str | None] = mapped_column(comment="Оцениваемый предмет")
    comment_shortened_text: Mapped[str | None] = mapped_column(comment="Первые 80 символов текста комментария")
    comment_full_text: Mapped[str | None] = mapped_column(comment="Полный текст комментария")
    comment_create_ts: Mapped[datetime | None] = mapped_column(
        comment="Timestamp создания комментария, мск", index=True
    )
    comment_update_ts: Mapped[datetime | None] = mapped_column(comment="Timestamp обновления комментария, мск")
    comment_mark_kindness: Mapped[int] = mapped_column(comment="Оценка доброты")
    comment_mark_freebie: Mapped[int] = mapped_column(comment="Оценка халявности")
    comment_mark_clarity: Mapped[int] = mapped_column(comment="Оценка понятности")
    comment_review_status: Mapped[str] = mapped_column(comment="Статус комментария")
    user_id: Mapped[int | None] = mapped_column(comment="Идентификатор пользователя из auth-api", index=True)
    user_full_name: Mapped[str | None] = mapped_column(comment="Имя пользователя")
    user_email: Mapped[str | None] = mapped_column(comment="Список электронных почт пользователя")
    __mapper_args__ = {"primary_key": ["comment_api_uuid", "lecturer_api_id"]}
