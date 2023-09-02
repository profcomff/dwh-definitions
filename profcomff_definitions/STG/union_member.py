from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type_of_learning: Mapped[str] = mapped_column(String, nullable=False)
    rzd_status: Mapped[str] = mapped_column(String)
    academic_level: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    faculty: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=False)
    rzd_datetime: Mapped[str] = mapped_column(String, nullable=False)
    rzd_number: Mapped[str] = mapped_column(String, nullable=False)
    grade_level: Mapped[int] = mapped_column(Integer)
    has_student_id: Mapped[bool] = mapped_column(Boolean)
    entry_date: Mapped[str] = mapped_column(String, nullable=False)
    status_gain_date: Mapped[str] = mapped_column(String, nullable=False)
    card_id: Mapped[int] = mapped_column(Integer, nullable=False)
    card_status: Mapped[str] = mapped_column(String, nullable=False)
    card_date: Mapped[str] = mapped_column(String, nullable=False)
    card_number: Mapped[str] = mapped_column(String, nullable=False)
    card_user: Mapped[int] = mapped_column(String, nullable=False)
    card: Mapped[int] = mapped_column(String, nullable=False)
