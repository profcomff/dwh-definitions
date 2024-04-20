from typing import Optional

from pydantic import BaseModel, Field, model_validator

#Auth
#невалидируемый класс
class UserAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)

    @model_validator(mode='before')
    def validate_card(self):
        parent_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")

        return self

class GroupAuth(BaseModel):
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        name: Mapped[str] = mapped_column(String)
        parent_id: Mapped[int] = mapped_column(Integer)
        create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
        update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
        is_deleted: Mapped[bool] = mapped_column(Boolean)
    @model_validator(mode='before')
    def validate_card(self):
        parent_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not parent_id):
            raise ValueError("нет parent_id")
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

        return self
#невалидируемый класс
class UserGroupAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    group_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        user_id = self["parent_id"]
        id = self["id"]
        group_id = self["group_id"]
        if (not id):
            raise ValueError("нет айди")
        if (not user_id):
            raise ValueError("нет uder_id")
        if (not group_id):
            raise ValueError("нет group_id")

        return self
class AuthMethodAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    auth_method: Mapped[str] = mapped_column(String) #это же пароль, его не валидируем?
    param: Mapped[str] = mapped_column(String) #тут хранится что???(список паролей из базы мб)
    value: Mapped[str] = mapped_column(String) #что традиционно называют value я не нашла и догадок не имею
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        user_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not user_id):
            raise ValueError("нет uder_id")
        return self
class UserSessionAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_name: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(Integer)
    expires: Mapped[datetime.datetime] = mapped_column(DateTime)
    token: Mapped[str] = mapped_column(String)
    last_activity: Mapped[datetime.datetime] = mapped_column(DateTime)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        user_id = self["user_id"]
        if (not id):
            raise ValueError("нет айди")
        if (not user_id):
            raise ValueError("нет uder_id")

        return self

class ScopeAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    creator_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

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

class GroupScopeAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)
    scope_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        group_id = self["group_id"]
        if (not id):
            raise ValueError("нет айди")
        if (not group_id):
            raise ValueError("нет uder_id")

        return self

class UserSessionScopeAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_session_id: Mapped[int] = mapped_column(Integer)
    scope_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
        def validate_card(self):
         id = self["id"]
         user_id = self["user_session_id"]
         if (not id):
             raise ValueError("нет айди")
         if (not user_id):
                raise ValueError("нет uder_id")

        return self

class UserMessageDelayAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    delay_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    user_email = sa.Column(EmailType)
    user_ip: Mapped[str] = mapped_column(String)
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
#Pinger
class ReceiverPi(BaseModel):
    id_: Mapped[int] = mapped_column("id", Integer, primary_key=True)
    url =  sa.Column(URLType)
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
#Print
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
        for i in range(a):'
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
#Services
class CategorySv(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)

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

class ButtonSv(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    order: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(Integer)
    icon: Mapped[str] = mapped_column(String)
    link =  sa.Column(URLType)
    type: Mapped[str] = mapped_column(String)

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

class ScopeSv(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)

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
#Timetable
class CredentialsT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group: Mapped[str] = mapped_column(String) #группа string? это номер группы, который "109"... и тд?
    email = sa.Column(EmailType)
    scope: Mapped[JSON] = mapped_column(JSON)
    token: Mapped[JSON] = mapped_column(JSON)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)


class RoomT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    direction: Mapped[str] = mapped_column(String)
    building: Mapped[str] = mapped_column(String)
    building_url = sa.Column(URLType)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

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
            elif (name[i].isalpha() == True):
                new_name += name[i]
        new_name = new_name.title()
        name = new_name

    return self

class LecturerT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    middle_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    avatar_id: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):

        id = self["id"]
        if (not id):
            raise ValueError("нет id")
        name1 = self["first_name"]
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
        name2 = self["middle_name"]
        new_trans_name2 = ""
        a2 = len(name2)
        new_name2 = ""
        for i in range(a2):
            new_trans_name2 += u''.join([_trans_table.get(c, c) for c in name2])
        name2 = new_trans_name2
        for i in range(a2):
            if (name2[i] == 'ё'):
                new_name2[i] = 'е'
            elif (name2[i].isalpha() == True):
                new_name2 += name2[i]
        new_name2 = new_name2.title()
        name2 = new_name2
        name3 = self["last_name"]
        new_trans_name3 = ""
        a3 = len(name3)
        new_name3 = ""
        for i in range(a3):
            new_trans_name3 += u''.join([_trans_table.get(c, c) for c in name3])
        name3 = new_trans_name3
        for i in range(a3):
            if (name3[i] == 'ё'):
                new_name3[i] = 'е'
            elif (name3[i].isalpha() == True):
                new_name3 += name3[i]
        new_name3 = new_name3.title()
        name3 = new_name3

    return self



class GroupT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
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


class EventT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    start_ts: Mapped[datetime] = mapped_column(DateTime)
    end_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
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


class EventsLecturersT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    lecturer_id: Mapped[int] = mapped_column(Integer)

    @model_validator(mode='before')
    def validate_card(self):
        event_id = self["event_id"]
        lecturer_id = self["lecturer_id"]

        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет event_id")
        if (not lecturer_id):
            raise ValueError("no lector no hannibal lector")


        return self


class EventsRoomsT(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    room_id: Mapped[int] = mapped_column(Integer)

    @model_validator(mode='before')
    def validate_card(self):
        event_id = self["parent_id"]
        room_id = self["room_id"]

        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет event_id")
        if (not room_id):
            raise ValueError("no room no hannibal lector")

        return self

class EventsGroupsT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    group_id: Mapped[int] = mapped_column(Integer)

    @model_validator(mode='before')
    def validate_card(self):
        event_id = self["parent_id"]
        group_id = self["group_id"]

        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет event_id")
        if (not group_id):
            raise ValueError("no group")

        return self


class PhotoT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lecturer_id: Mapped[int] = mapped_column(Integer)
    link =  sa.Column(URLType)
    approve_status: Mapped[str] = mapped_column(String)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        lecturer_id = self["lecturer_id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет lecturer_id")

        return self


class CommentLecturerT(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lecturer_id: Mapped[int] = mapped_column(Integer)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)


    @model_validator(mode='before')
    def validate_card(self):
        lecturer_id = self["lecturer_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not lecturer_id):
            raise ValueError("нет event_id")
        return self

class CommentEvent(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    approve_status: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        event_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет event_id")

        return self
#Union_Member
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
        for t not in formi:
            raise ValueError("Необученное, не учится ни на какой нормальной форме обучения")
       # тут должны быть еще rzhd_status и status_card но я не понимаю что там
#Userdata
class CategoryUd(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    read_scope: Mapped[str] = mapped_column(String)
    update_scope: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

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


class ParamUd(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer)
    is_required: Mapped[bool] = mapped_column(Boolean)
    changeable: Mapped[bool] = mapped_column(Boolean)
    type: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

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


class SourceUd(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    trust_level: Mapped[int] = mapped_column(Integer)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

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


class InfoUd(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    param_id: Mapped[int] = mapped_column(Integer)
    source_id: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer)
    value: Mapped[str] = mapped_column(String)
    create_ts: Mapped[datetime] = mapped_column(DateTime)
    modify_ts: Mapped[datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):

        id = self["id"]
        if (not id):
            raise ValueError("нет id")
    
    return self



