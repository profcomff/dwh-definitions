from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ViribusChat(Base):
    """
    Преподаватели в rating-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    thread_name: Mapped[str | None] = mapped_column(comment="Название ветки в сообществе, например Frontend")
    message_text: Mapped[str | None] = mapped_column(comment="Текст сообщения в телеграме")
    sender_telegram_login: Mapped[str | None] = mapped_column(comment="Логин пользователя в телеграме")
    message_ts: Mapped[datetime] = mapped_column(comment="Таймстемп записи в social-api")


class GitHub(Base):
    """
    Статистика GitHub
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    status: Mapped[str] = mapped_column(comment="Статус issue")
    url: Mapped[str] = mapped_column(comment="Ссылка на issue")
    issue_id: Mapped[int | None] = mapped_column(comment="Идентификатор issue")
    user_id: Mapped[int | None] = mapped_column(comment="Идентификатор пользователя открывшего issue")
    user_login: Mapped[str | None] = mapped_column(comment="Логин пользователя открывшего issue")
    issue_title: Mapped[str | None] = mapped_column(comment="Название issue")
    repository_id: Mapped[int | None] = mapped_column(comment="Идентификатор репозитория")
    sender_id: Mapped[int | None] = mapped_column(comment="Идентификатор отправителя")
    sender_login: Mapped[str | None] = mapped_column(comment="Логин отправителя")
    assignee_id: Mapped[int | None] = mapped_column(comment="Идентификатор назначенного исполнителем issue")
    assignee_login: Mapped[int | None] = mapped_column(comment="Логин назначенного исполнителем issue")
    created_at: Mapped[datetime | None] = mapped_column(comment="Временная метка создания issue")
    updated_at: Mapped[datetime | None] = mapped_column(comment="Временная метка апдейта issue")
    closed_at: Mapped[datetime | None] = mapped_column(comment="Временная метка закрытия issue")
    organization_id: Mapped[int] = mapped_column(comment="Идентификатор организации")
    organizatin_login: Mapped[str | None] = mapped_column(comment="Логин организации")
    event_ts: Mapped[datetime] = mapped_column(comment="Временная метка данного события")
