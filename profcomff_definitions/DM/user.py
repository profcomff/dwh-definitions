from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMemberJoin(Base):
    """Таблица соответствия пользователей приложения и членов профсоюза"""

    user_id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's email from ods user info")
    phone_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's phone_number from ods user info"
    )
    vk_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's vk_name from ods user info")
    city: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's city from ods uder info")
    hometown: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's hometown from ods user info")
    location: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's current city from ods user info"
    )
    github_name: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's github_name from ods user info"
    )
    telegram_name: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's telegram_name from ods user info"
    )
    home_phone_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's home_phone_number from ods user info"
    )
    education_level: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="Bachelor/Master/Specialist from ods user info"
    )
    university: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's university from ods user info"
    )
    group: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's group from ods user info")
    faculty: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's faculty from ods user info")
    position: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's position in university from ods user info"
    )
    student_id_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's student_id_number from ods user info"
    )
    department: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's department in university from ods user info"
    )
    mode_of_study: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="full-time/correspondence education from ods user info"
    )
    full_name: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's full_name from ods user info")
    birth_date: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's birth_date from ods user info"
    )
    photo: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's photo(https://) from ods user info"
    )
    sex: Mapped[str | None] = mapped_column(String, nullable=True, comment="male/female from ods user info")
    job: Mapped[str | None] = mapped_column(String, nullable=True, comment="user's job from ods user info")
    work_location: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="user's work_location from ods uder info"
    )
    card_status: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="card_status - user's card status (current or not) from ODS.user.info"
    )
    card_date: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="card date - date of user's card activation from ODS.user.info"
    )
    card_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="card number - number of user's card from ODS.user.info"
    )


class UnionMemberCard(Base):
    user_id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    card_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    card_number: Mapped[str | None] = mapped_column(
        String, nullable=True, comment="card number - number of user's card from ODS.user.info"
    )
