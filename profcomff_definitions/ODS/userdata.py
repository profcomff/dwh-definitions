from datetime import date, datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Email(Base):
    email: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class PhoneNumber(Base):
    phone_number: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class VkUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class City(Base):
    city: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class BirthCity(Base):
    city: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Address(Base):
    address: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class GitHubUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class TelegramUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class HomePhoneNumber(Base):
    phone_number: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class EducationLevel(Base):
    level: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class University(Base):
    university: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Faculty(Base):
    faculty: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class AcademicGroup(Base):
    group: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Position(Base):
    position: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class StudentId(Base):
    card_number: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Department(Base):
    department: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class EducationForm(Base):
    form: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class FullName(Base):
    name: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Birthday(Base):
    birthday: Mapped[datetime] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Photo(Base):
    url: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Sex(Base):
    gender: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class Workplace(Base):
    workplace: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]

class WorkplaceAddress(Base):
    address: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str]
    created: Mapped[datetime | None]
    modified: Mapped[datetime | None]
    is_deleted: Mapped[bool | None]