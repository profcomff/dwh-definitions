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
