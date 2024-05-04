from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type_of_learning: Mapped[str] = mapped_column(String, nullable=True)
    rzd_status: Mapped[str] = mapped_column(String, nullable=True)
    academic_level: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=True)
    faculty: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    date_of_birth: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    image: Mapped[str] = mapped_column(String, nullable=True)
    rzd_datetime: Mapped[str] = mapped_column(String, nullable=True)
    rzd_number: Mapped[str] = mapped_column(String, nullable=True)
    grade_level: Mapped[int] = mapped_column(Integer, nullable=True)
    has_student_id: Mapped[bool] = mapped_column(Boolean, nullable=True)
    entry_date: Mapped[str] = mapped_column(String, nullable=True)
    status_gain_date: Mapped[str] = mapped_column(String, nullable=True)
    card_id: Mapped[int] = mapped_column(Integer, nullable=True)
    card_status: Mapped[str] = mapped_column(String, nullable=True)
    card_date: Mapped[str] = mapped_column(String, nullable=True)
    card_number: Mapped[str] = mapped_column(String, nullable=True)
    card_user: Mapped[int] = mapped_column(String, nullable=True)
    card: Mapped[int] = mapped_column(String, nullable=True)
