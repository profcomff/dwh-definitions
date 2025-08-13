from datetime import date, datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Email(Base):
    email: Mapped[str] = mapped_column(primary_key=True, comment="Электронная почта пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class PhoneNumber(Base):
    phone_number: Mapped[str] = mapped_column(primary_key=True, comment="Номер телефона пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class VkUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True, comment="Имя пользователя ВКонтакте")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class City(Base):
    city: Mapped[str] = mapped_column(primary_key=True, comment="Название города проживания")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class BirthCity(Base):
    city: Mapped[str] = mapped_column(primary_key=True, comment="Название города рождения")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Address(Base):
    address: Mapped[str] = mapped_column(primary_key=True, comment="Адрес проживания пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class GitHubUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True, comment="Имя пользователя GitHub")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class TelegramUsername(Base):
    username: Mapped[str] = mapped_column(primary_key=True, comment="Имя пользователя Telegram")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class HomePhoneNumber(Base):
    phone_number: Mapped[str] = mapped_column(primary_key=True, comment="Домашний номер телефона")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class EducationLevel(Base):
    level: Mapped[str] = mapped_column(primary_key=True, comment="Уровень образования")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class University(Base):
    university: Mapped[str] = mapped_column(primary_key=True, comment="Название университета")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Faculty(Base):
    faculty: Mapped[str] = mapped_column(primary_key=True, comment="Название факультета")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class AcademicGroup(Base):
    group: Mapped[str] = mapped_column(primary_key=True, comment="Название академической группы")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Position(Base):
    position: Mapped[str] = mapped_column(primary_key=True, comment="Должность пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class StudentId(Base):
    student_id: Mapped[str] = mapped_column(primary_key=True, comment="Студенческий билет")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Department(Base):
    department: Mapped[str] = mapped_column(primary_key=True, comment="Название кафедры/отдела")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class EducationForm(Base):
    form: Mapped[str] = mapped_column(primary_key=True, comment="Форма обучения")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class FullName(Base):
    name: Mapped[str] = mapped_column(primary_key=True, comment="Полное имя пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Birthday(Base):
    birthday: Mapped[datetime] = mapped_column(primary_key=True, comment="Дата рождения пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Photo(Base):
    url: Mapped[str] = mapped_column(primary_key=True, comment="URL фотографии пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Sex(Base):
    gender: Mapped[str] = mapped_column(primary_key=True, comment="Пол пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Workplace(Base):
    workplace: Mapped[str] = mapped_column(primary_key=True, comment="Место работы пользователя")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class WorkplaceAddress(Base):
    address: Mapped[str] = mapped_column(primary_key=True, comment="Адрес места работы")
    user_id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор пользователя")
    source: Mapped[str] = mapped_column(comment="Источник данных")
    created: Mapped[datetime | None] = mapped_column(comment="Дата создания записи")
    modified: Mapped[datetime | None] = mapped_column(comment="Дата последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")
