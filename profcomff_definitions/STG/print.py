from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    __tablename__ = 'union_member'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String)
    union_number: Mapped[str] = mapped_column(String)
    student_number: Mapped[str] = mapped_column(String)


class File(Base):
    __tablename__ = 'file'

    id: Mapped[int] = Column(Integer, primary_key=True)
    pin: Mapped[str] = Column(String)
    file: Mapped[str] = Column(String)
    owner_id: Mapped[int] = Column(Integer)
    option_pages: Mapped[str] = Column(String)
    option_copies: Mapped[int] = Column(Integer)
    option_two_sided: Mapped[bool] = Column(Boolean)
    created_at: Mapped[datetime] = Column(DateTime)
    updated_at: Mapped[datetime] = Column(DateTime)
    number_of_pages: Mapped[int] = Column(Integer)
    source: Mapped[str] = Column(String)


class PrintFact(Base):
    __tablename__ = 'print_fact'

    id: Mapped[int] = Column(Integer, primary_key=True)
    file_id: Mapped[int] = Column(Integer)
    owner_id: Mapped[int] = Column(Integer)
    created_at: Mapped[datetime] = Column(DateTime)
    sheets_used: Mapped[int] = Column(Integer)
