from datetime import date, datetime, timedelta
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DmRentalsEvents(Base):
    """
    Данные арендных сессий
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
    duration: Mapped[timedelta] = mapped_column(comment="Продолжительность аренды, в часах")
    delay: Mapped[timedelta] = mapped_column(comment="Время задержки возврата")
    overdue_flag: Mapped[bool] = mapped_column(comment="Флаг просрочки")
    conversion_flag: Mapped[bool] = mapped_column(comment="Флаг конверсии из брони в аренду")
    type_id: Mapped[int] = mapped_column(comment="Идентификатор типа вещи")
    type: Mapped[str] = mapped_column(comment="Тип вещи")
    name: Mapped[str] = mapped_column(comment="Название вещи")
    image_url: Mapped[str | None] = mapped_column(comment="Ссылка на фото вещи")
    description: Mapped[str | None] = mapped_column(comment="Описание вещи")
    available_items: Mapped[int] = mapped_column(comment="Количество доступных вещей")
    total_items: Mapped[int] = mapped_column(comment="Количество вещей данного типа")
    rental_count: Mapped[int] = mapped_column(comment="Общее количество аренд данного типа")
    avg_downtime_hours: Mapped[timedelta] = mapped_column(comment="Среднее время простоя")
    avg_rent_hours: Mapped[timedelta] = mapped_column(comment="Среднее время аренды")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии")
    admin_strike_id: Mapped[int | None] = mapped_column(comment="Идентификаор админа")
    strike_reason: Mapped[str | None] = mapped_column(comment="Причина страйка")
    strike_date: Mapped[datetime | None] = mapped_column(comment="Timestamp начисления страйка, мск")
    strike_count: Mapped[int | None] = mapped_column(comment="Количество страйков у пользователя")
    activity_max_time: Mapped[int] = mapped_column(comment="Час пиковой активности")
    activity_max: Mapped[int] = mapped_column(comment="Количество активности в час пиковой нагрузки")
