from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Achievement(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    description: Mapped[str | None]
    picture: Mapped[str | None]
    owner_user_id: Mapped[int | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]


class AchievementReciever(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None]
    achievement_id: Mapped[int | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
