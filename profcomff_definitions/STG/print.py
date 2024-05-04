from datetime import datetime

from sqlalchemy import BIGINT, Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String, nullable=True)
    union_number: Mapped[str] = mapped_column(String, nullable=True)
    student_number: Mapped[str] = mapped_column(String, nullable=True)


class File(Base):
    id: Mapped[int] = Column(Integer, primary_key=True)
    pin: Mapped[str] = Column(String, nullable=True)
    file: Mapped[str] = Column(String, nullable=True)
    owner_id: Mapped[int] = Column(Integer, nullable=True)
    option_pages: Mapped[str] = Column(String, nullable=True)
    option_copies: Mapped[int] = Column(Integer, nullable=True)
    option_two_sided: Mapped[bool] = Column(Boolean, nullable=True)
    created_at: Mapped[datetime] = Column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = Column(DateTime, nullable=True)
    number_of_pages: Mapped[int] = Column(Integer, nullable=True)
    source: Mapped[str] = Column(String, nullable=True)


class PrintFact(Base):
    id: Mapped[int] = Column(Integer, primary_key=True)
    file_id: Mapped[int] = Column(Integer, nullable=True)
    owner_id: Mapped[int] = Column(Integer, nullable=True)
    created_at: Mapped[datetime] = Column(DateTime, nullable=True)
    sheets_used: Mapped[int] = Column(Integer, nullable=True)


class VkUser(Base):
    vk_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    surname: Mapped[int] = mapped_column(String, nullable=True)
    number: Mapped[int] = mapped_column(String, nullable=True)


class TgUser(Base):
    tg_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    surname: Mapped[int] = mapped_column(String, nullable=True)
    number: Mapped[int] = mapped_column(String, nullable=True)
