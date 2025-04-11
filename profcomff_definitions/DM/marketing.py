from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class FrontendActionsServices(Base):
    """
    Фронтендовые события
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_from: Mapped[str | None] = mapped_column(comment="Откуда совершен переход")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    user_agent: Mapped[str | None] = mapped_column(comment="Информация об операционной системе и браузере")
    is_bot: Mapped[bool] = mapped_column(comment="Флаг бот или нет")
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания")
    service_name: Mapped[str] = mapped_column(comment="Назввание сервиса, куда пользователь перешел")
