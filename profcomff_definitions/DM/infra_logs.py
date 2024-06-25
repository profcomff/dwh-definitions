from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ContainerLogCube(Base):
    """Куб типов логов контейнера"""

    id: Mapped[int] = mapped_column(primary_key=True)
    container_name: Mapped[str] = mapped_column(comment="Название контейнера")
    create_date: Mapped[str] = mapped_column(comment="Дата лога")
    debug_cnt: Mapped[int] = mapped_column(comment="Количество записей с типом DEBUG")
    warn_cnt: Mapped[int] = mapped_column(comment="Количество записей с типом WARN")
    info_cnt: Mapped[int] = mapped_column(comment="Количество записей с типом INFO")
    error_cnt: Mapped[int] = mapped_column(comment="Количество записей с типом ERROR")
    critical_cnt: Mapped[int] = mapped_column(comment="Количество записей с типом CRITICAL")
    other_cnt: Mapped[int] = mapped_column(comment="Количество записей с другими типами")


class IncidentHint(Base):
    """Информация об ошибках по контейнерам"""

    id: Mapped[int] = mapped_column(primary_key=True)
    msk_record_loaded_dttm: Mapped[datetime] = mapped_column(comment="Поле нарезки лога")
    container_name: Mapped[str] = mapped_column(comment="Имя контейнера, в котором произошла ошибочка")
    message: Mapped[str] = mapped_column(comment="Сообщение об ошибке")
    create_ts: Mapped[datetime] = mapped_column(comment="Время, когда произошла ошибка")
