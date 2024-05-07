from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ContainerLog(Base):
    """Логи запущенных контейнеров с приложениями"""

    id: Mapped[int] = mapped_column(primary_key=True)
    record: Mapped[dict] = mapped_column(sa.JSON, comment="Данные из строки лога")
    container_name: Mapped[str] = mapped_column(comment="Название контейнера, породившего строку лога")
    create_ts: Mapped[datetime] = mapped_column(comment="Время создания записи лога")
