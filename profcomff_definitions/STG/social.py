from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Group(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    last_active_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    owner_id: Mapped[int] = mapped_column(sa.Integer)
    is_deleted: Mapped[bool] = mapped_column(sa.Boolean)
    type: Mapped[str] = mapped_column(sa.String)


class CreateGroupRequest(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    valid_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    owner_id: Mapped[int] = mapped_column(sa.Integer)
    mapped_group_id: Mapped[int] = mapped_column(sa.Integer)
    secret_key: Mapped[str] = mapped_column(sa.String)


class WebhookStorage(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    system: Mapped[str] = mapped_column(sa.String)
    message: Mapped[sa.JSON] = mapped_column(sa.JSON(True))
    event_ts: Mapped[datetime] = mapped_column(sa.DateTime)


class VkGroup(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(sa.Integer)
    confirmation_token: Mapped[str] = mapped_column(sa.String)
    secret_key: Mapped[str] = mapped_column(sa.String)


class TelegramChannel(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(sa.Integer)


class TelegramChat(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(sa.Integer)


class VkChat(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    peer_id: Mapped[int] = mapped_column(sa.Integer)
