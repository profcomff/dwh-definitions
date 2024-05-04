from pydantic import BaseModel, model_validator
from pydantic import int, str, Field, EmailStr, AnyURL, Json
from datetime import datetime



class CredentialsT(BaseModel):
    id: int = Field(primary_key=True)
    group: str
    email = EmailStr
    scope: Json[Any]
    token: Json[Any]
    create_ts: datetime.datetime
    update_ts: datetime.datetime


class RoomT(BaseModel):
    id: int =  Field(primary_key=True)
    name: str
    direction: str
    building: str
    building_url: AnyURL
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
            elif (name[i].isalpha() == True):
                new_name += name[i]
        new_name = new_name.title()
        name = new_name
        
        return self

class LecturerT(BaseModel):
    id: int = Field(primary_key=True)
    first_name: str
    middle_name: str
    last_name: str
    avatar_id: str
    description: str
    is_deleted: bool

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
    id: int =Field(primary_key=True)
    name: str
    number: int
    is_deleted: bool
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
    id: int = Field(primary_key=True)
    name: str
    start_ts: datetime.datetime
    end_ts: datetime.datetime
    is_deleted: bool

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
    id: int = Field(primary_key=True)
    event_id: int
    lecturer_id: int

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
    id: int = Field(primary_key=True)
    event_id: int
    room_id: int

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
    id: int = Field(primary_key=True)
    event_id: int
    group_id: int

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
    id: int = Field(primary_key=True)
    lecturer_id: int
    link: AnyURL
    approve_status: str
    is_deleted: bool
    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        lecturer_id = self["lecturer_id"]
        if (not id):
            raise ValueError("нет айди")
        if (not lecturer_id):
            raise ValueError("нет lecturer_id")

        return self


class CommentLecturerT(BaseModel):
    id: int = Field(primary_key=True)
    lecturer_id: int
    author_name: str
    text: str
    approve_status: str
    create_ts: datetime.datetime
    update_ts: datetime.datetime
    is_deleted: bool


    @model_validator(mode='before')
    def validate_card(self):
        lecturer_id = self["lecturer_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not lecturer_id):
            raise ValueError("нет event_id")
        return self

class CommentEventT(Base):
    id: int = Field(primary_key=True)
    event_id: int
    author_name: str
    text: str
    approve_status: str
    create_ts: datetime.datetime
    update_ts: datetime.datetime
    is_deleted: bool

    @model_validator(mode='before')
    def validate_card(self):
        event_id = self["parent_id"]
        id = self["id"]
        if (not id):
            raise ValueError("нет айди")
        if (not event_id):
            raise ValueError("нет event_id")

        return self
