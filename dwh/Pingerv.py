from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime, func, Float, JSON
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime



#Pinger
class ReceiverPi(BaseModel):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    url = sa.Column(URLType)
    method: Mapped[str] = mapped_column(String)
    receiver_body: Mapped[dict] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)


class AlertPi(BaseModel):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    data = mapped_column(JSON)
    filter = mapped_column(String)
    create_ts = mapped_column(DateTime)


class FetcherPi(BaseModel):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    type_: Mapped[str] = mapped_column("type", String)
    address: Mapped[str] = mapped_column(String)
    fetch_data: Mapped[str] = mapped_column(String)
    delay_ok: Mapped[int] = mapped_column(Integer)
    delay_fail: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime] = mapped_column(DateTime)


class MetricPi(BaseModel):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    name: Mapped[str] = mapped_column("name", String)
    ok: Mapped[bool] = mapped_column("ok", Boolean)
    time_delta: Mapped[float] = mapped_column(Float)

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
