from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Group(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    last_active_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    owner_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(sa.Boolean, nullable=True)
    type: Mapped[str] = mapped_column(sa.String, nullable=True)


class CreateGroupRequest(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    valid_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)
    owner_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    mapped_group_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    secret_key: Mapped[str] = mapped_column(sa.String, nullable=True)


class WebhookStorage(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    system: Mapped[str] = mapped_column(sa.String, nullable=True)
    message: Mapped[sa.JSON] = mapped_column(sa.JSON(True), nullable=True)
    event_ts: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)


class VkGroup(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
    confirmation_token: Mapped[str] = mapped_column(sa.String, nullable=True)
    secret_key: Mapped[str] = mapped_column(sa.String, nullable=True)


class TelegramChannel(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)


class TelegramChat(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)


class VkChat(Base):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    peer_id: Mapped[int] = mapped_column(sa.Integer, nullable=True)
