from sqlalchemy.orm import Mapped, mapped_column
from profcomff_definitions.base import Base

class Incident(Base):
    """Информация об ошибках по контейнерам"""
    container_name: Mapped[str] = mapped_column(comment="Имя контейнера, в котором произошла ошибочка")
    message: Mapped[str] = mapped_column(comment="Сообщение об ошибке")
    create_ts: Mapped[datetime] = mapped_column(comment="Время, когда произошла ошибка")
