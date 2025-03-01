from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class FrontendActions(Base):
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


class PrinterActions(Base):
    """
    Действия принтера
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_from: Mapped[str | None] = mapped_column(comment="Откуда совершен переход")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    status: Mapped[str] = mapped_column(comment="Статус действия")
    app_version: Mapped[str] = mapped_column(comment="Версия приложения")
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания (московское время)")


class PrinterBotsActions(Base):
    """
    Действия ботов принтера в вк и тг
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_from: Mapped[str | None] = mapped_column(comment="Откуда совершен переход")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    status: Mapped[str] = mapped_column(comment="Статус действия")
    user_id: Mapped[int] = mapped_column(comment="Айди юзера в соответствующей соцсети(tg/vk)")
    surname: Mapped[str] = mapped_column(comment='Фамилия юзера')
    number: Mapped[int] = mapped_column(comment="Номер")
    pin: Mapped[int | None]
    status_code: Mapped[int | None] = mapped_column(comment="Код ошибки")
    description: Mapped[str | None] = mapped_column(comment="Описание ошибки")
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания (московское время)")


class RatingActions(Base):
    """
    События в рейтинге
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    response_status_code: Mapped[int]
    user_id: Mapped[int]
    query: Mapped[str] = mapped_column(comment="Переданные параметры запроса")
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания (московское время)")
