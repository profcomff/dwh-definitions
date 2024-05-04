from datetime import datetime

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str | None]
    union_number: Mapped[str | None]
    student_number: Mapped[str | None]


class File(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    pin: Mapped[str | None]
    file: Mapped[str | None]
    owner_id: Mapped[int | None]
    option_pages: Mapped[str | None]
    option_copies: Mapped[int | None]
    option_two_sided: Mapped[bool | None]
    created_at: Mapped[datetime | None]
    updated_at: Mapped[datetime | None]
    number_of_pages: Mapped[int | None]
    source: Mapped[str | None]


class PrintFact(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int | None]
    owner_id: Mapped[int | None]
    created_at: Mapped[datetime | None]
    sheets_used: Mapped[int | None]


class VkUser(Base):
    vk_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    surname: Mapped[str | None]
    number: Mapped[str | None]


class TgUser(Base):
    tg_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    surname: Mapped[str | None]
    number: Mapped[str | None]
