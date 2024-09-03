from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr, AnyURL, Json
from datetime import datetime


class UnionMemberPr(BaseModel):
    id: int 
    surname: str
    union_number: int
    student_number: int
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
    id: int
    pin: str
    file: str
    owner_id: int
    option_pages: str
    option_copies: int
    option_two_sided: bool
    created_at: datetime
    updated_at: datetime
    number_of_pages: int
    source: str
