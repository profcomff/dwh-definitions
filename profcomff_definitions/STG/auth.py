from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    is_deleted: Mapped[bool | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]


class Group(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    parent_id: Mapped[int | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class UserGroup(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None]
    group_id: Mapped[int | None]
    is_deleted: Mapped[bool | None]


class AuthMethod(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None]
    auth_method: Mapped[str | None]
    param: Mapped[str | None]
    value: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]


class UserSession(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    session_name: Mapped[str | None]
    user_id: Mapped[int | None]
    expires: Mapped[datetime | None]
    token: Mapped[str | None]
    last_activity: Mapped[datetime | None]
    create_ts: Mapped[datetime | None]


class Scope(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int | None]
    name: Mapped[str | None]
    comment: Mapped[str | None]
    is_deleted: Mapped[bool | None]


class GroupScope(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int | None]
    scope_id: Mapped[int | None]
    is_deleted: Mapped[bool | None]


class UserSessionScope(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_session_id: Mapped[int | None]
    scope_id: Mapped[int | None]
    is_deleted: Mapped[bool | None]


class UserMessageDelay(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    delay_time: Mapped[datetime | None]
    user_email: Mapped[str | None]
    user_ip: Mapped[str | None]


class DynamicOption(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    create_ts: Mapped[datetime | None]
    value_integer: Mapped[int | None]
    value_string: Mapped[str | None]
    value_double: Mapped[float | None]
    update_ts: Mapped[datetime | None]
    name: Mapped[str | None]
