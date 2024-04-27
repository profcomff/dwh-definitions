from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Achievement(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String)
    description: Mapped[str] = mapped_column(sa.String)
    picture: Mapped[str] = mapped_column(sa.String)
    owner_user_id: Mapped[int] = mapped_column(sa.Integer)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime)


class AchievementReceiver(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(sa.Integer)
    achievement_id: Mapped[int] = mapped_column(sa.Integer)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime)
