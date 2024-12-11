from datetime import date, datetime

from sqlalchemy.orm import Mapped

from profcomff_definitions.base import Base


class User(Base):
    """
    Historical table for STG_AUTH.user
    """

    id: Mapped[int]
    is_deleted: Mapped[bool | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    valid_from_dt: Mapped[date | None]
    valid_to_dt: Mapped[date | None]
    __mapper_args__ = {"primary_key": ["id", "valid_from_dt"]}  # Used only to correctly map ORM object to sql table


class AuthMethod(Base):
    """
    Historical table for STG_AUTH.auth_method
    """

    id: Mapped[int]
    user_id: Mapped[int | None]
    auth_method: Mapped[str | None]
    param: Mapped[str | None]
    value: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    update_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
    valid_from_dt: Mapped[date | None]
    valid_to_dt: Mapped[date | None]
    __mapper_args__ = {"primary_key": ["id", "valid_from_dt"]}  # Used only to correctly map ORM object to sql table
