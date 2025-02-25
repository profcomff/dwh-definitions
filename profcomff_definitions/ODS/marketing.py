from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class FrontendActions(Base):
    """
    Фронтендовые события user_id > 0
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_from: Mapped[str | None] = mapped_column(comment="Откуда совершен переход")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    user_agent: Mapped[str | None] = mapped_column(comment="Информация об операционной системе и браузере")
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания")


class PrinterActions(Base):
    """
    Действия принтера user_id = -1
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_from: Mapped[str | None] = mapped_column(comment="Откуда совершен переход")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    status: Mapped[str] = mapped_column(comment="Статус действия")
    app_version: Mapped[str] = mapped_column(comment="Версия приложения")
    terminal_user_id: Mapped[int]
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания")


class PrinterBotsActions(Base):
    """
    Действия ботов принтера в вк и тг user_id = -2
    """

    id: Mapped[int] = mapped_column(primary_key=True)
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
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания")


class RatingActions(Base):
    """
    События в рейтинге
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(comment="Совершенное действие")
    path_to: Mapped[str | None] = mapped_column(comment="Назначение перехода")
    response_status_code: Mapped[int]
    user_id: Mapped[int]
    query: Mapped[str]
    create_ts: Mapped[datetime] = mapped_column(comment="Таймстемп создания")
