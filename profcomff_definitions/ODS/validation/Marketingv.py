from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime


#Marketing
class UserM(BaseModel):
    id = Column(sa.Integer, primary_key=True)
    union_number = Column(sa.Integer)
    user_agent = Column(sa.String)
    auth_user_id = Column(sa.Integer)
    modify_ts = Column(sa.DateTime)
    create_ts = Column(sa.DateTime)
class ActionsInfoM(BaseModel):
    id = Column(sa.Integer, primary_key=True)
    user_id = Column(sa.Integer)
    action = Column(sa.String)
    path_from = Column(sa.String)
    path_to = Column(sa.String)
    additional_data = Column(sa.String)
    create_ts = Column(sa.DateTime)
#Physics
class ContactsPh(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    email = sa.Column(EmailType)
    phone: Mapped[int] = mapped_column(Integer, nullable=True)
    workplace: Mapped[int] = mapped_column(Integer, nullable=True)
    upload_ts: Mapped[datetime] = mapped_column(DateTime, default=func.now())

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
