from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr, AnyURL, Json
from datetime import datetime


#Social
class WebhookStorageSoc(BaseModel):
    id: int = Field(primary_key=True)
    system: str 
    message: Json[Any]


class VkGroupsSoc(BaseModel):
    id: int = Field(primary_key=True)
    group_id: int 
    confirmation_token: str
    secret_key: str
    create_ts: datetime.datetime
    update_ts: datetime.datetime
