from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base, encrypted, sensitive


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор категории")
    name: Mapped[str | None] = mapped_column(comment="Название категории")
    read_scope: Mapped[str | None] = mapped_column(comment="Область видимости для чтения")
    update_scope: Mapped[str | None] = mapped_column(comment="Область видимости для обновления")
    create_ts: Mapped[datetime | None] = mapped_column(comment="Время создания записи")
    modify_ts: Mapped[datetime | None] = mapped_column(comment="Время последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Param(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор параметра")
    visible_in_user_response: Mapped[bool | None] = mapped_column(comment="Видимость параметра в ответе пользователю")
    name: Mapped[str | None] = mapped_column(comment="Название параметра")
    category_id: Mapped[int | None] = mapped_column(comment="Идентификатор категории")
    is_required: Mapped[bool | None] = mapped_column(comment="Является ли параметр обязательным")
    changeable: Mapped[bool | None] = mapped_column(comment="Может ли параметр быть изменен")
    type: Mapped[str | None] = mapped_column(comment="Тип данных параметра")
    create_ts: Mapped[datetime | None] = mapped_column(comment="Время создания записи")
    modify_ts: Mapped[datetime | None] = mapped_column(comment="Время последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")
    is_public: Mapped[bool | None] = mapped_column(comment="Является ли параметр публичным")
    validation: Mapped[str | None] = mapped_column(comment="Правила валидации параметра")


class Source(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор источника данных")
    name: Mapped[str | None] = mapped_column(comment="Название источника данных")
    trust_level: Mapped[int | None] = mapped_column(comment="Уровень доверия к источнику")
    create_ts: Mapped[datetime | None] = mapped_column(comment="Время создания записи")
    modify_ts: Mapped[datetime | None] = mapped_column(comment="Время последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


class Info(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор информационной записи")
    param_id: Mapped[int | None] = mapped_column(comment="Идентификатор параметра")
    source_id: Mapped[int | None] = mapped_column(comment="Идентификатор источника данных")
    owner_id: Mapped[int | None] = mapped_column(comment="Идентификатор владельца данных")
    value: Mapped[str | None] = mapped_column(comment="Значение параметра")
    create_ts: Mapped[datetime | None] = mapped_column(comment="Время создания записи")
    modify_ts: Mapped[datetime | None] = mapped_column(comment="Время последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")


@sensitive
class InfoKeys(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор ключа шифрования")
    key: Mapped[str] = mapped_column(comment="Симметричный ключ шифрования")


@encrypted("id", "InfoKeys")
class EncryptedInfo(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Идентификатор зашифрованной записи")
    param_id: Mapped[int | None] = mapped_column(comment="Идентификатор параметра")
    source_id: Mapped[int | None] = mapped_column(comment="Идентификатор источника данных")
    owner_id: Mapped[int | None] = mapped_column(comment="Идентификатор владельца данных")
    value: Mapped[bytes | None] = mapped_column(comment="Зашифрованное значение параметра")
    create_ts: Mapped[datetime | None] = mapped_column(comment="Время создания записи")
    modify_ts: Mapped[datetime | None] = mapped_column(comment="Время последнего изменения записи")
    is_deleted: Mapped[bool | None] = mapped_column(comment="Флаг удаления записи")
