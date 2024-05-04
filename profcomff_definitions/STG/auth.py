import datetime

from sqlalchemy import Boolean, DateTime, Double, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)


class Group(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    parent_id: Mapped[int] = mapped_column(Integer, nullable=True)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class UserGroup(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    group_id: Mapped[int] = mapped_column(Integer, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class AuthMethod(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    auth_method: Mapped[str] = mapped_column(String, nullable=True)
    param: Mapped[str] = mapped_column(String, nullable=True)
    value: Mapped[str] = mapped_column(String, nullable=True)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class UserSession(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_name: Mapped[str] = mapped_column(String, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    expires: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    token: Mapped[str] = mapped_column(String, nullable=True)
    last_activity: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)


class Scope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creator_id: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    comment: Mapped[str] = mapped_column(String, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class GroupScope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer, nullable=True)
    scope_id: Mapped[int] = mapped_column(Integer, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class UserSessionScope(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_session_id: Mapped[int] = mapped_column(Integer, nullable=True)
    scope_id: Mapped[int] = mapped_column(Integer, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=True)


class UserMessageDelay(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    delay_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    user_email: Mapped[str] = mapped_column(String, nullable=True)
    user_ip: Mapped[str] = mapped_column(String, nullable=True)


class DynamicOption(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    value_integer: Mapped[int] = mapped_column(Integer, nullable=True)
    value_string: Mapped[str] = mapped_column(String, nullable=True)
    value_double: Mapped[float] = mapped_column(Double, nullable=True)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
