from datetime import date, datetime, timedelta
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DmRentalsEvents(Base):
    """
    Витрина данных арендных сессий
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле dwh")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    item_id: Mapped[int] = mapped_column(comment="Идентификатор предмета")
    admin_open_session_id: Mapped[int] = mapped_column(comment="Идентификатор админа начавшего сессию")
    admin_close_session_id: Mapped[int | None] = mapped_column(comment="Идентификатор админа закончевшего сессию")
    reservation_ts: Mapped[datetime] = mapped_column(comment="Время начала брони")
    start_ts: Mapped[datetime] = mapped_column(comment="Timestamp начала аренды предмета, мск")
    end_ts: Mapped[datetime] = mapped_column(comment="Timestamp рассчетное время возврата предмета, мск")
    actual_return_ts: Mapped[datetime] = mapped_column(comment="Timestamp реальное время возврата предмета, мск")
    status: Mapped[str] = mapped_column(comment="Статус текущей сессии")
    type_id: Mapped[int] = mapped_column(comment="Идентификатор типа вещи")
    name: Mapped[str] = mapped_column(comment="Название вещи")
    image_url: Mapped[str | None] = mapped_column(comment="Ссылка на фото вещи")
    description: Mapped[str | None] = mapped_column(comment="Описание вещи")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии")
    session_duration_minutes: Mapped[datetime | None] = mapped_column(comment="Длительность аренды в мин")
    overdue_minutes: Mapped[datetime | None] = mapped_column(comment="Просрочка времени аренды в мин")
    strikes_count: Mapped[int] = mapped_column(comment="Количество страйков за сессию")


class DmStrike(Base):
    """
    Витрина страйки
    """

    __tablename__ = "dm_strike"

    strike_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор страйка")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    user_segment: Mapped[str | None] = mapped_column(comment="Сегмент пользователя (опционально)")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии аренды")
    item_id: Mapped[int] = mapped_column(comment="Идентификатор вещи")
    item_type_id: Mapped[int] = mapped_column(comment="Идентификатор типа вещи")
    item_type_name: Mapped[str | None] = mapped_column(comment="Название типа вещи")
    item_name: Mapped[str] = mapped_column(comment="Название вещи")
    strike_reason: Mapped[str | None] = mapped_column(comment="Причина страйка")
    strike_date: Mapped[datetime] = mapped_column(comment="Дата и время начисления страйка")
    admin_id: Mapped[int] = mapped_column(comment="Идентификатор администратора, вынесшего страйк")
    admin_name: Mapped[str | None] = mapped_column(comment="Имя администратора (де-normalized)")
    total_strikes_user: Mapped[int] = mapped_column(comment="Общее количество страйков пользователя")
    total_strikes_session: Mapped[int] = mapped_column(comment="Общее количество страйков в сессии")
    rental_start_ts: Mapped[datetime] = mapped_column(comment="Начало аренды")
    rental_end_ts: Mapped[datetime] = mapped_column(comment="Планируемое окончание аренды")
    return_ts: Mapped[datetime | None] = mapped_column(comment="Фактическое время возврата")
    session_status: Mapped[str | None] = mapped_column(comment="Статус сессии аренды")
