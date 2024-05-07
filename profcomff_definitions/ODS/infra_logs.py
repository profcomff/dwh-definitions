from datetime import UTC, datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ContainerLog(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    record: Mapped[dict] = mapped_column(sa.JSON)
    container_name: Mapped[str]
    create_ts: Mapped[datetime]
