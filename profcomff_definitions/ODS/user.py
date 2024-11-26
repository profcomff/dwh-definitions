from datetime import date, datetime

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Info(Base):
    # ODS_USER.info
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True, comment="primary key")
    email: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's email from stg userdata")
    phone_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's phone_number from stg userdata"
    )
    vk_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's vk_name from stg userdata")
    city: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's city from stg userdata")
    hometown: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's hometown from stg userdata")
    location: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's current city from stg userdata")
    github_name: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's github_name from stg userdata"
    )
    telegram_name: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's telegram_name stg userdata"
    )
    home_phone_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's home_phone_number from stg userdata"
    )
    education_level: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="Bachelor/Master/Specialist from stg userdata"
    )
    university: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's university from stg userdata")
    group: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's group from stg userdata")
    faculty: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's faculty from stg userdata")
    position: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's position in university from stg userdata"
    )
    student_id_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's student_id_number from stg userdata"
    )
    department: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's department in university from stg userdata"
    )
    mode_of_study: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="full-time/correspondence education from stg userdata"
    )
    full_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's full_name from stg userdata")
    birth_date: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's birth_date from stg userdata")
    photo: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's photo(https://) from stg userdata")
    sex: Mapped[str | None] = mapped_column(String, nullable=True, comment="male/female from stg userdata")
    job: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's job from stg userdata")
    work_location: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's work_location from stg userdata"
    )
    is_deleted: Mapped[bool | None] = mapped_column(
        Boolean, nullable=True, comment="If True, user was deleted in backend. Default=False"
    )


class UnionMember(Base):
    # ODS_USER.union_member
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True, comment="primary key")
    fio: Mapped[str] = mapped_column(String, nullable=True, comment="user's full name")
    card_status: Mapped[str] = mapped_column(String, nullable=True, comment="user's status of card (current or not)")
    card_date: Mapped[str] = mapped_column(String, nullable=True, comment="user's card acrivation data")
    card_number: Mapped[str] = mapped_column(String, nullable=True, comment="user's card number")
