from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime, JSON, Text
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy_utils import URLType, EmailType
from datetime import datetime
from sqlalchemy import Base


class UnionMemberUnimember(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type_of_learning: Mapped[str] = mapped_column(String, nullable=False)
    rzd_status: Mapped[str] = mapped_column(String)
    academic_level: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False) #что лежит в статусе я просто не поняла
    faculty: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email = sa.Column(EmailType)
    date_of_birth: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[int] = mapped_column(Integer, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=False) #картинки ихихихихихих я схожу с ума помогите
    rzd_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    rzd_number: Mapped[int] = mapped_column(Integer, nullable=False)
    grade_level: Mapped[int] = mapped_column(Integer)
    has_student_id: Mapped[bool] = mapped_column(Boolean)
    entry_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status_gain_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    card_id: Mapped[int] = mapped_column(Integer, nullable=False)
    card_status: Mapped[str] = mapped_column(String, nullable=False) #какие статусы могут быть у карты?
    card_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    card_number: Mapped[int] = mapped_column(Integer, nullable=False)
    card_user: Mapped[str] = mapped_column(String, nullable=False)
    card: Mapped[int] = mapped_column(Integer, nullable=False)

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
