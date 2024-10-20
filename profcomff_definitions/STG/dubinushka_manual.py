from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Comment(Base):
    """
    Comments from dubinushka
    Because this data is downloaded from .sql query, the order of columns is significant
    """

    flag: Mapped[int]
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_id: Mapped[int | None]
    comment_text: Mapped[str | None]
    author_name: Mapped[str | None]
    rate: Mapped[str | None]
    date: Mapped[str | None]
    dobr: Mapped[str | None]
    hal: Mapped[str | None]
    pon: Mapped[str | None]


class Lecturer(Base):
    """
    Lecturers from dubinushka
    Because this data is downloaded from .sql query, the order of columns is significant
    """

    flagprep: Mapped[int | None]
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str | None]
    subject: Mapped[str | None]
    fullrate: Mapped[int | None]
    mn_count: Mapped[str | None]
    photo: Mapped[int | None]
    dobr: Mapped[float | None]
    hal: Mapped[float | None]
    pon: Mapped[float | None]
    isdead: Mapped[int | None]
    obituary: Mapped[str | None]
