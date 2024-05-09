from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr
from datetime import datetime

class UserAuth(BaseModel):
    id: int 
    is_deleted: bool
    create_ts: datetime
    update_ts: datetime
    @model_validator(mode='before')
    def validate_card(self):
        parent_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")

        return self

class GroupAuth(BaseModel):
        id: int 
        name: str
        parent_id: int 
        create_ts: datetime
        update_ts: datetime
        is_deleted: bool 

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
    id: int 
    user_id: int
    group_id: int
    is_deleted: bool

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
    id: int 
    user_id: int 
    auth_method: str
    param: str
    value: str
    create_ts: datetime
    update_ts: datetime
    is_deleted: bool

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
    id: int 
    session_name: str
    user_id: int
    expires: datetime
    token: str
    last_activity: datetime
    create_ts: datetime

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
    id: int 
    creator_id: int
    name: str
    comment: str
    is_deleted: bool
    
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
    id: int 
    group_id: int 
    scope_id: int
    is_deleted: bool

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
    id: int 
    user_session_id: int
    scope_id: int
    is_deleted: bool

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
    id: int 
    delay_time: datetime
    user_email: EmailStr
    user_ip: str
