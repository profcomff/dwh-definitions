from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Info(Base):
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String, nullable=True)
    is_deleted: Mapped[bool] = False