from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class UnionMember(Base):
    id: Mapped[int] = mapped_column(primary_key=True, comment="Уникальный идентификатор пользователя")
    type_of_learning: Mapped[str | None] = mapped_column(comment="Тип обучения (дневное/вечернее, бюджет/контракт)")
    rzd_status: Mapped[str | None] = mapped_column(comment="Статус в системе РЖД")
    academic_level: Mapped[str | None] = mapped_column(comment="Уровень образования (бакалавриат/магистратура/аспирантура)")
    status: Mapped[str | None] = mapped_column(comment="Текущий статус пользователя")
    faculty: Mapped[str | None] = mapped_column(comment="Название факультета")
    first_name: Mapped[str | None] = mapped_column(comment="Имя пользователя")
    last_name: Mapped[str | None] = mapped_column(comment="Фамилия пользователя")
    middle_name: Mapped[str | None] = mapped_column(comment="Отчество пользователя")
    email: Mapped[str | None] = mapped_column(comment="Email пользователя")
    date_of_birth: Mapped[str | None] = mapped_column(comment="Дата рождения")
    phone_number: Mapped[str | None] = mapped_column(comment="Номер телефона")
    image: Mapped[str | None] = mapped_column(comment="Фото пользователя (ссылка или base64)")
    rzd_datetime: Mapped[str | None] = mapped_column(comment="Дата в системе РЖД")
    rzd_number: Mapped[str | None] = mapped_column(comment="Номер в системе РЖД")
    grade_level: Mapped[int | None] = mapped_column(comment="Курс (год обучения)")
    has_student_id: Mapped[bool | None] = mapped_column(comment="Наличие студенческого билета")
    entry_date: Mapped[str | None] = mapped_column(comment="Дата поступления")
    status_gain_date: Mapped[str | None] = mapped_column(comment="Дата получения текущего статуса")
    card_id: Mapped[int | None] = mapped_column(comment="ID карты профкома")
    card_status: Mapped[str | None] = mapped_column(comment="Статус карты профкома")
    card_date: Mapped[str | None] = mapped_column(comment="Дата выдачи карты профкома")
    card_number: Mapped[str | None] = mapped_column(comment="Номер карты профкома")
    card_user: Mapped[str | None] = mapped_column(comment="Пользователь, связанный с картой")
    student_id: Mapped[str | None] = mapped_column(comment="Номер студенческого билета")
