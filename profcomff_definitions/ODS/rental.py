from datetime import datetime
from uuid import UUID
from sqlalchemy import JSON, Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from profcomff_definitions.base import Base


class Item(Base):
    """
    Вещи в rental.api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    type_id: Mapped[int] = mapped_column(comment="Идентификатор типа вещи")
    is_available: Mapped[bool] = mapped_column(comments="Маркер доступности вещи")
    type: Mapped[str] = mapped_column(comments="Тип вещи")


class ItemType(Base):
    """
    Описание, фото типа вещи в rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comments="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comments="Идентификатор в rental-api")
    name: Mapped[str] = mapped_column(comments="Название вещи")
    image_url: Mapped[str | None] = mapped_column(comments="Ссылка на фото вещи")
    description: Mapped[str | None] = mapped_column(comments="Описание вещи")


class RentalSession(Base):
    """
    Сессия и статус для вещей rental-api
    """
    uuid: Mapped[UUID] = mapped_column(primary_key=True, comments="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comments="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comments="Идентификатор пользователя")
    item_id: Mapped[int] = mapped_column(comments="Идентификатор предмета")
    admin_open_id: Mapped[int] = mapped_column(comments="Идентификатор админа начавшего сессию")
    admin_close_id: Mapped[int | None] = mapped_column(comments="Идентификатор админа закончевшего сессию")
    reservation_ts: Mapped[datetime.datetime] = mapped_column(comments="Время начала брони")
    start_ts: Mapped[datetime.datetime] = mapped_column(comments="Timestamp начала аренды предмета, мск")
    end_ts: Mapped[datetime.datetime] = mapped_column(comments="Timestamp рассчетное время возврата предмета, мск")
    actual_return_ts: Mapped[datetime.datetime] = mapped_column(comments="Timestamp реальное время возврата предмета, мск")
    status: Mapped[str] = mapped_column(comment="Статус текущей сессии")


class Event(Base):
    """
    Логи rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comments="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comments="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comments="Идентификатор пользователя")
    admin_id: Mapped[int] = mapped_column(comments="Идентификатор админа")
    session_id: Mapped[int] = mapped_column(comments="Идентификатор сессии")
    action_type: Mapped[str] = mapped_column(comments="Тип действия")
    details: Mapped[dict] = mapped_column(comments="Описание лога")
    create_ts: Mapped[datetime.datetime] = mapped_column(comments="Timestamp лога, мск")


class Strike(Base):
    """
    Страйки пользователям в rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comments="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comments="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comments="Идентификатор пользователя")
    session_id: Mapped[int] = mapped_column(comments="Идентификатор сессии")
    admin_id: Mapped[int] = mapped_column(comments="Идентификаор админа")
    reason: Mapped[str] = mapped_column(comments="Причина страйка")
    create_ts: Mapped[datetime.datetime] = mapped_column(comments="Timestamp страйка, мск")
