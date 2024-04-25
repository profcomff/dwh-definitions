from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

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
        is_deleted: Mapped[bool] = (mapped_column(Boolean)

        @model_validator(mode='before'))
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
                for i in range(len(a)):
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
    auth_method: Mapped[str] = mapped_column(String)
    param: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
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
    user_email = Column(EmailType)
    user_ip: Mapped[str] = mapped_column(String)
