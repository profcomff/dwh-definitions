from datetime import datetime

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Group(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int | None]

    name: Mapped[str | None]
    description: Mapped[str | None]
    invite_link: Mapped[str | None]
    hidden: Mapped[bool | None]

    update_ts: Mapped[datetime | None]
    create_ts: Mapped[datetime | None]
    last_active_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
    type: Mapped[str | None]


class CreateGroupRequest(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    valid_ts: Mapped[datetime | None]
    create_ts: Mapped[datetime | None]
    owner_id: Mapped[int | None]
    mapped_group_id: Mapped[int | None]
    secret_key: Mapped[str | None]


class WebhookStorage(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    system: Mapped[str | None]
    message: Mapped[str | None]
    event_ts: Mapped[datetime | None]


class VkGroup(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int | None]
    confirmation_token: Mapped[str | None]
    secret_key: Mapped[str | None]


class TelegramChannel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    channel_id: Mapped[int | None] = mapped_column(BIGINT)


class TelegramChat(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int | None] = mapped_column(BIGINT)


class VkChat(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    peer_id: Mapped[int | None]
