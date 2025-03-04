from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Lecturer(Base):
    """
    Преподаватели в rating-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентифиактор в rating-api")
    first_name: Mapped[str] = mapped_column(comment="Имя преподавателя")
    last_name: Mapped[str] = mapped_column(comment="Фамилия преподавателя")
    middle_name: Mapped[str] = mapped_column(comment="отчество преподавателя")
    subject: Mapped[str | None] = mapped_column(comment="Список предметов преподавателя")
    avatar_link: Mapped[str | None] = mapped_column(comment="Ссылка на аватар преподавателя")
    timetable_id: Mapped[int] = mapped_column(comment="Идертификатор в timetable-api")


class Comment(Base):
    """
    Комментарии в rating-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_uuid: Mapped[UUID] = mapped_column(comment="Идентифиактор в rating-api")
    create_ts: Mapped[datetime] = mapped_column(comment="Timestamp создания комментария, мск")
    update_ts: Mapped[datetime] = mapped_column(comment="Timestamp обновления комментария, мск")
    subject: Mapped[str | None] = mapped_column(comment="Предмет, к которому относится комментарий")
    text: Mapped[str | None] = mapped_column(comment="Текст комментария")
    mark_kindness: Mapped[int] = mapped_column(comment="Доброта преподавателя")
    mark_freebie: Mapped[int] = mapped_column(comment="Халявность преподавателя")
    mark_clarity: Mapped[int] = mapped_column(comment="Понятность преподавателя")
    lecturer_id: Mapped[int] = mapped_column(comment="Идертификатор преподавателя")
    review_status: Mapped[str] = mapped_column(comment="Статус комментария, может быть approved, pending, dismissed")


class LecturerUserComment(Base):
    """
    Связь лекторов и комметариев в rating-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентифиактор в rating-api")
    lecturer_id: Mapped[int] = mapped_column(comment="Идентифиактор преподавателя")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя в auth-api")
    create_ts: Mapped[datetime] = mapped_column(comment="Timestamp создания комментария, мск")
    update_ts: Mapped[datetime] = mapped_column(comment="Timestamp обновления комментария, мск")
