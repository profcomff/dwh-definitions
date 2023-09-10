import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)


class Group(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class UserGroup(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    group_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class AuthMethod(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    auth_method: Mapped[str] = mapped_column(String)
    param: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class UserSession(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_name: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(Integer)
    expires: Mapped[datetime.datetime] = mapped_column(DateTime)
    token: Mapped[str] = mapped_column(String)
    last_activity: Mapped[datetime.datetime] = mapped_column(DateTime)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)


class Scope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creator_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class GroupScope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)
    scope_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class UserSessionScope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_session_id: Mapped[int] = mapped_column(Integer)
    scope_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


class UserMessageDelay(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    delay_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    user_email: Mapped[str] = mapped_column(String)
    user_ip: Mapped[str] = mapped_column(String)
