from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class WebhookStorage(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    system: Mapped[str] = mapped_column(sa.String)
    message: Mapped[sa.JSON] = mapped_column(sa.JSON(True))


class VkGroups(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(sa.Integer)
    confirmation_token: Mapped[str] = mapped_column(sa.String)
    secret_key: Mapped[str] = mapped_column(sa.String)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime)
