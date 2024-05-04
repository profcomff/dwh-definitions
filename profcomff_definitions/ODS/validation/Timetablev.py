from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, Boolean, Column, String, DateTime, JSON, Text 
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy_utils import URLType, EmailType 
from datetime import datetime 
from sqlalchemy import Base 




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
        if (not lecturer_id):
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

class CommentEventT(Base):
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
