import logging

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from profcomff_definitions.base import Base


logger = logging.getLogger(__name__)


class Test(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
