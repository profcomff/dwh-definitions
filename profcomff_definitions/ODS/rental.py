from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Item(Base):
    """
    Вещи в rental.api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    type_id: Mapped[int] = mapped_column(comment="Идентификатор типа вещи")
    is_available: Mapped[bool] = mapped_column(comment="Маркер доступности вещи")


class ItemType(Base):
    """
    Описание, фото типа вещи в rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле в dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    name: Mapped[str] = mapped_column(comment="Название вещи")
    image_url: Mapped[str | None] = mapped_column(comment="Ссылка на фото вещи")
    description: Mapped[str | None] = mapped_column(comment="Описание вещи")


class RentalSession(Base):
    """
    Сессия и статус для вещей rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    item_id: Mapped[int] = mapped_column(comment="Идентификатор предмета")
    admin_open_id: Mapped[int] = mapped_column(comment="Идентификатор админа начавшего сессию")
    admin_close_id: Mapped[int | None] = mapped_column(comment="Идентификатор админа закончевшего сессию")
    reservation_ts: Mapped[datetime] = mapped_column(comment="Время начала брони")
    start_ts: Mapped[datetime] = mapped_column(comment="Timestamp начала аренды предмета, мск")
    end_ts: Mapped[datetime] = mapped_column(comment="Timestamp рассчетное время возврата предмета, мск")
    actual_return_ts: Mapped[datetime] = mapped_column(comment="Timestamp реальное время возврата предмета, мск")
    status: Mapped[str] = mapped_column(comment="Статус текущей сессии")


class Event(Base):
    """
    Логи rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    admin_id: Mapped[int] = mapped_column(comment="Идентификатор админа")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии")
    action_type: Mapped[str] = mapped_column(comment="Тип действия")
    details: Mapped[str] = mapped_column(comment="Описание лога")
    create_ts: Mapped[datetime] = mapped_column(comment="Timestamp лога, мск")


class Strike(Base):
    """
    Страйки пользователям в rental-api
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле dwh")
    api_id: Mapped[int] = mapped_column(comment="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии")
    admin_id: Mapped[int] = mapped_column(comment="Идентификаор админа")
    reason: Mapped[str] = mapped_column(comment="Причина страйка")
    create_ts: Mapped[datetime] = mapped_column(comment="Timestamp страйка, мск")
