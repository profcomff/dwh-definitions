from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr, AnyURL, Json, Optional
from datetime import datetime



class UnionMemberUnimember(BaseModel):
    id: int 
    type_of_learning: Optional[str] = Field(nullable=False)
    rzd_status: str
    academic_level: Optional[str] = Field(nullable=False)
    status: Optional[str] =Field(nullable=False) 
    faculty: Optional[str] = Field(nullable=False)
    first_name: Optional[str] = Field(nullable=False)
    last_name: Optional[str] = Field(nullable=False)
    email: EmailStr
    date_of_birth: Optional[str] = Field(nullable=False)
    phone_number: Optional[int] = Field(nullable=False)
    image: Optional[str] = Field(nullable=False)
    rzd_datetime: Optional[datetime] = Field(nullable = False)
    rzd_number: Optional[int] = Field(nullable=False)
    grade_level: int
    has_student_id: bool
    entry_date: Optional[datetime] = Field(nullable=False)
    status_gain_date: Optional[datetime] = Field(nullable=False)
    card_id: Optional[int] = Field(nullable=False)
    card_status: Optional[str] = Field(nullable=False)
    card_date: Optional[datetime] = Field(nullable=False)
    card_number: Optional[int] = Field(nullable=False)
    card_user: Optional[str] = Field(nullable=False)
    card: Optional[int] = Field(nullable=False)

    @model_validator(mode='before')
    def validate_card(self):

        id = self["id"]
        if (not id):
            raise ValueError("нет id")
        type_of_learning = self["type_of_learning"]
        rzd_status = self["rzd_status"]
        academic_level = self["academic_level"]
        faculty = self["faculty"]
        name1= self["firstname"]
        name3 = self["last_name"]
        date_of_birth = self["date_of_birth"]
        card_status = self["card_status"]
        name = self["card_user"]
        new_trans_name1 = ""
        a1 = len(name1)
        new_name1 = ""
        _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
        _trans_table = dict(zip(_eng_chars, _rus_chars))
        for i in range(a1):
            new_trans_name1 += u''.join([_trans_table.get(c, c) for c in name1])
        name1 = new_trans_name1
        for i in range(a1):
            if (name1[i] == 'ё'):
                new_name1[i] = 'е'
            elif (name1[i].isalpha() == True):
                new_name1 += name1[i]
        new_name1 = new_name1.title()
        name1 = new_name1
        new_trans_name3 = ""
        a3 = len(name3)
        new_name3 = ""
        _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
        _trans_table = dict(zip(_eng_chars, _rus_chars))
        for i in range(a3):
            new_trans_name3 += u''.join([_trans_table.get(c, c) for c in name3])
        name3 = new_trans_name3
        for i in range(a3):
            if (name3[i] == 'ё'):
                new_name3[i] = 'е'
            elif (name3[i].isalpha() == True):
                new_name3 += name1[i]
        new_name3 = new_name3.title()
        name3 = new_name3
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
            elif (name[i].isalpha() == True):
                new_name += name[i]
        new_name = new_name.title()
        name = new_name
        t = ""
        t_trans = ""
        a4 = len(type_of_learning)
        _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
        _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
        _trans_table = dict(zip(_eng_chars, _rus_chars))
        for i in range(a4):
            t_trans += u''.join([_trans_table.get(c, c) for c in type_of_learning])
        type_of_learning = t_trans
        for i in range(a4):
            if (type_of_learning[i] == 'ё'):
                new_name1[i] = 'е'
            elif (type_of_learning[i].isalpha() == True):
                t += type_of_learning[i]
        t = t.title()
        type_of_learning = t
        formi = ['Дневная', 'Очная','Заочная','Вечерняя','Ночная', 'Закончил']
        if t not in formi:
            raise ValueError("Необученное, не учится ни на какой нормальной форме обучения")
        
        return self 
