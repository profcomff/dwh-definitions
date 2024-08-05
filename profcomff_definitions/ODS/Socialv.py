from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy_utils import URLType



#Social
class WebhookStorageSoc(BaseModel):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    system: Mapped[str] = mapped_column(sa.String)
    message: Mapped[sa.JSON] = mapped_column(sa.JSON(True))


class VkGroupsSoc(BaseModel):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(sa.Integer)
    confirmation_token: Mapped[str] = mapped_column(sa.String)
    secret_key: Mapped[str] = mapped_column(sa.String)
    create_ts: Mapped[datetime] = mapped_column(sa.DateTime)
    update_ts: Mapped[datetime] = mapped_column(sa.DateTime)
