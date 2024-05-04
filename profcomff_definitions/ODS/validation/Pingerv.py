from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr, AnyURL, Json
from datetime import datetime


#Pinger
class ReceiverPi(BaseModel):
    id_: int = Field(description = "id", primary_key=True)
    url: AnyURL
    method: str
    receiver_body: Json[Any]
    create_ts: datetime.datetime


class AlertPi(BaseModel):
    id_: int = Field(description = "id", primary_key=True)
    data: Json[Any]
    filter: str
    create_ts: datetime.datetime


class FetcherPi(BaseModel):
    id_: int = (description = "id", primary_key=True)
    type_: str = Field(description = "type")
    address: str
    fetch_data: str
    delay_ok: int
    delay_fail: int
    create_ts: datetime.datetime

class MetricPi(BaseModel):
    id_: int = Field(description = "id", primary_key=True)
    name: str = Field(description = "name")
    ok: bool = Field(description = "ok")
    time_delta: float
    @model_validator(mode='before')
    def validate_card(self):

        id = self["id"]
        if (not id):
            raise ValueError("нет id")
        name = self["name"]
        k = 0
        new_trans_name = ""
        a = len(name)
        new_name = ""
        _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
        _trans_table = dict(zip(_eng_chars, _rus_chars))
        for i in range(a):
            new_trans_name += u''.join([_trans_table.get(c, c) for c in name])
        name = new_trans_name
        for i in range(a):
            if (name[i].isalpha() != True):
                if (name[i] == ' ') and (i != 0) and (i != a):
                    k = k + 1
                    if k == 1:
                        new_name += ' '
            if (name[i] == 'ё'):
                new_name[i] = 'е'
            if (name[i].isalpha() == True):
                new_name += name[i]
        new_name = new_name.title()
        name = new_name

        return self
