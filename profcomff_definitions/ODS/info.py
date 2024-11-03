from datetime import datetime, date
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class ParamHist(Base):
    """
    SCD2 historical table based on STG_USERDATA.param
    """
    id: Mapped[int] = mapped_column(primary_key=True)
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


class InfoHist(Base):
    """
    SCD2 historical table based on STG_USERDATA.info
    """
    id: Mapped[int] = mapped_column(primary_key=True)
    param_id: Mapped[int | None]
    source_id: Mapped[int | None]
    owner_id: Mapped[int | None]
    value: Mapped[str | None]
    create_ts: Mapped[datetime | None]
    modify_ts: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]
    valid_from_dt: Mapped[date | None]
    valid_to_dt: Mapped[date | None]
