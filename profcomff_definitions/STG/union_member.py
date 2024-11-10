from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type_of_learning: Mapped[str | None]
    rzd_status: Mapped[str | None]
    academic_level: Mapped[str | None]
    status: Mapped[str | None]
    faculty: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    middle_name: Mapped[str | None]
    email: Mapped[str | None]
    date_of_birth: Mapped[str | None]
    phone_number: Mapped[str | None]
    image: Mapped[str | None]
    rzd_datetime: Mapped[str | None]
    rzd_number: Mapped[str | None]
    grade_level: Mapped[int | None]
    has_student_id: Mapped[bool | None]
    entry_date: Mapped[str | None]
    status_gain_date: Mapped[str | None]
    card_id: Mapped[int | None]
    card_status: Mapped[str | None]
    card_date: Mapped[str | None]
    card_number: Mapped[str | None]
    card_user: Mapped[str | None]
    card: Mapped[str | None]
