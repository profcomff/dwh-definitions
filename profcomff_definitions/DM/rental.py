from datetime import datetime, date, timedelta
from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class DmRentals(Base):
    """
    Данные арендных сессий
    """

    uuid: Mapped[UUID] = mapped_column(primary_key=True, comment="Техническое поле dwh")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    item_id: Mapped[int] = mapped_column(comment="Идентификатор предмета")
    admin_open_id: Mapped[int] = mapped_column(comment="Идентификатор админа начавшего сессию")
    admin_close_id: Mapped[int | None] = mapped_column(comment="Идентификатор админа закончевшего сессию")
    reservation_ts: Mapped[datetime] = mapped_column(comment="Время начала брони")
    start_ts: Mapped[datetime] = mapped_column(comment="Timestamp начала аренды предмета, мск")
    end_ts: Mapped[datetime] = mapped_column(comment="Timestamp рассчетное время возврата предмета, мск")
    actual_return_ts: Mapped[datetime] = mapped_column(comment="Timestamp реальное время возврата предмета, мск")
    status: Mapped[str] = mapped_column(comment="Статус текущей сессии")
    duration: Mapped[timedelta] = mapped_column(comment="Продолжительность аренды, в часах")
    delay: Mapped[timedelta] = mapped_column(comment="Время задержки возврата")
    overdue_flag: Mapped[bool] = mapped_column(comment="Флаг просрочки")
    conversion_flag: Mapped[bool] = mapped_column(comment="Флаг конверсии из брони в аренду")


class DmAvailability(Base):
    """
    Доступность вещей и их популярность
    """
    
    api_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор в rental-api")
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
    

class DmStrike(Base):
    """
    Страйки пользователям
    """
    
    api_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор в rental-api")
    user_id: Mapped[int] = mapped_column(comment="Идентификатор пользователя")
    session_id: Mapped[int] = mapped_column(comment="Идентификатор сессии")
    admin_id: Mapped[int] = mapped_column(comment="Идентификаор админа")
    reason: Mapped[str] = mapped_column(comment="Причина страйка")
    strike_date: Mapped[datetime] = mapped_column(comment="Timestamp начисления страйка, мск")
    overdue_flag: Mapped[bool] = mapped_column(comment="Флаг просрочки")
    strike_count: Mapped[int] = mapped_column(comment="Количество страйков у пользователя")
