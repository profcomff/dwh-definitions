from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


# DWH_USER.info
class Info(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True, comment="primary key")
    email: Mapped[str | None] = mapped_column(String, nullable=True, comment="email from stg userdata")
    auth_email: Mapped[str] = mapped_column(String, nullable=False, comment="email used for authentication")
    phone_number: Mapped[str | None] = mapped_column(String, nullable=True, comment="phone_number from stg userdata")
    vk_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="vk_name from stg userdata")
    city: Mapped[str | None] = mapped_column(String, nullable=True, comment="city from stg userdata")
    hometown: Mapped[str | None] = mapped_column(String, nullable=True, comment="hometown from stg userdata")
    location: Mapped[str | None] = mapped_column(String, nullable=True, comment="current city from stg userdata")
    github_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="github_name from stg userdata")
    telegram_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="telegram_name stg userdata")
    home_phone_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="home_phone_number from stg userdata"
    )
    education_level: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="Bachelor/Master/Specialist from stg userdata"
    )
    university: Mapped[str | None] = mapped_column(String, nullable=True, comment="university from stg userdata")
    group: Mapped[str | None] = mapped_column(String, nullable=True, comment="group from stg userdata")
    faculty: Mapped[str | None] = mapped_column(String, nullable=True, comment="faculty from stg userdata")
    position: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="position in university from stg userdata"
    )
    student_id_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="student_id_number from stg userdata"
    )
    department: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="department in university from stg userdata"
    )
    mode_of_study: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="full-time/correspondence education from stg userdata"
    )
    full_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="full_name from stg userdata")
    birth_date: Mapped[str | None] = mapped_column(String, nullable=True, comment="birth_date from stg userdata")
    photo: Mapped[str | None] = mapped_column(String, nullable=True, comment="photo (URL) from stg userdata")
    sex: Mapped[str | None] = mapped_column(String, nullable=True, comment="male/female from stg userdata")
    job: Mapped[str | None] = mapped_column(String, nullable=True, comment="job from stg userdata")
    work_location: Mapped[str | None] = mapped_column(String, nullable=True, comment="work_location from stg userdata")
    is_deleted: Mapped[bool | None] = mapped_column(
        Boolean, nullable=True, comment="If True, user was deleted in backend. Default=False"
    )
