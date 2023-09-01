import logging

from sqlalchemy import Integer, String, JSON   
from sqlalchemy.orm import Mapped, mapped_column


from profcomff_definitions.base import Base
logger = logging.getLogger(__name__)


class SocialActivity(Base):
	id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
	system: Mapped[String] = mapped_column(String, nullable=False)
	message: Mapped[JSON] = mapped_column(JSON, nullable=False)

