from datetime import date, datetime

from sqlalchemy.orm import Mapped

from profcomff_definitions.base import Base


class ParamHist(Base):
    """
    SCD2 historical table based on STG_USERDATA.param
    """

    id: Mapped[int]
    visible_in_user_response: Mapped[bool | None]
    name: Mapped[str | None]
    category_id: Mapped[int | None]
    is_required: Mapped[bool | None]
    changeable: Mapped[bool | None]
    type: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
    validation: Mapped[str | None]
    valid_from_dt: Mapped[date | None]
    valid_to_dt: Mapped[date | None]
    __mapper_args__ = {"primary_key": ["id", "valid_from_dt"]}  # Used only to correctly map ORM object to sql table


class InfoHist(Base):
    """
    SCD2 historical table based on STG_USERDATA.info
    """

    id: Mapped[int]
    param_id: Mapped[int | None]
    source_id: Mapped[int | None]
    owner_id: Mapped[int | None]
    value: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
    valid_from_dt: Mapped[date | None]
    valid_to_dt: Mapped[date | None]
    __mapper_args__ = {"primary_key": ["id", "valid_from_dt"]}  # Used only to correctly map ORM object to sql table
