from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class UnionMemberPr(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    surname: Mapped[str] = mapped_column(String)
    union_number: Mapped[int] = mapped_column(Integer)
    student_number: Mapped[int] = mapped_column(Integer)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        if (not id):
            raise ValueError("нет id")
        name = self["surname"]
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
            if (name[i] == 'ё'):
                new_name[i] = 'е'
            if (name[i].isalpha() == True):
                new_name += name[i]
        new_name = new_name.title()
        name = new_name
    
        return self


class FilePr(BaseModel):
    id: Mapped[int] = Column(Integer, primary_key=True)
    pin: Mapped[str] = Column(String)
    file: Mapped[str] = Column(String)
    owner_id: Mapped[int] = Column(Integer)
    option_pages: Mapped[str] = Column(String)
    option_copies: Mapped[int] = Column(Integer)
    option_two_sided: Mapped[bool] = Column(Boolean)
    created_at: Mapped[datetime] = Column(DateTime)
    updated_at: Mapped[datetime] = Column(DateTime)
    number_of_pages: Mapped[int] = Column(Integer)
    source: Mapped[str] = Column(String)
