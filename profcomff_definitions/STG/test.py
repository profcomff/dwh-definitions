from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class Test(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]
