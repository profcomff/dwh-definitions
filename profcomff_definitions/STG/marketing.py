from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    union_number: Mapped[str | None]
    user_agent: Mapped[str | None]
    auth_user_id: Mapped[int | None]
    modify_ts: Mapped[datetime | None]
    create_ts: Mapped[datetime | None]


class ActionsInfo(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None]
    action: Mapped[str | None]
    path_from: Mapped[str | None]
    path_to: Mapped[str | None]
    additional_data: Mapped[str | None]
    create_ts: Mapped[datetime | None]
