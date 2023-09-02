import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


class VkUser(Base):
    vk_id: Mapped[int] = mapped_column(sqlalchemy.BIGINT, primary_key=True)
    surname: Mapped[int] = mapped_column(sqlalchemy.String)
    number: Mapped[int] = mapped_column(sqlalchemy.String)
