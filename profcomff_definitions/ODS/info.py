from datetime import datetime, date
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Info(Base):
    user_id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String, nullable=True)
    vk_name: Mapped[str | None] = mapped_column(String, nullable=True)
    city: Mapped[str | None] = mapped_column(String, nullable=True)
    hometown: Mapped[str | None] = mapped_column(String, nullable=True)
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    github_name: Mapped[str | None] = mapped_column(String, nullable=True)
    telegram_name: Mapped[str | None] = mapped_column(String, nullable=True)
    home_phone_number: Mapped[str | None] = mapped_column(String, nullable=True)
    education_level: Mapped[str | None] = mapped_column(String, nullable=True)
    university: Mapped[str | None] = mapped_column(String, nullable=True)
    group: Mapped[str | None] = mapped_column(String, nullable=True)
    faculty: Mapped[str | None] = mapped_column(String, nullable=True)
    position: Mapped[str | None] = mapped_column(String, nullable=True)
    student_id_number: Mapped[str | None] = mapped_column(String, nullable=True)
    department: Mapped[str | None] = mapped_column(String, nullable=True)
    mode_of_study: Mapped[str | None] = mapped_column(String, nullable=True)
    full_name: Mapped[str | None] = mapped_column(String, nullable=True)
    birth_date: Mapped[str | None] = mapped_column(String, nullable=True)
    photo: Mapped[str | None] = mapped_column(String, nullable=True)
    sex: Mapped[str | None] = mapped_column(String, nullable=True)
    job: Mapped[str | None] = mapped_column(String, nullable=True)
    work_location: Mapped[str | None] = mapped_column(String, nullable=True)


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
