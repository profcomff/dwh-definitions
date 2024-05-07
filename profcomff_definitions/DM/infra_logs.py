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
