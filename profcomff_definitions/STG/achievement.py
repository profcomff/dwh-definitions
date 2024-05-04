from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Achievement(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String, nullable=True)
    description: Mapped[str] = mapped_column(sa.String, nullable=True)
    picture: Mapped[str] = mapped_column(sa.String, nullable=True)
    owner_user_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)


class AchievementReceiver(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    achievement_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
