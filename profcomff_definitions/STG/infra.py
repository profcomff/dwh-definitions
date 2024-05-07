from datetime import UTC, datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ContainerLog(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    record: Mapped[str | None]
    container_name: Mapped[str | None]
    create_ts: Mapped[datetime | None] = mapped_column(
        server_default=sa.text("now()"), default=lambda: datetime.now(UTC)
    )
