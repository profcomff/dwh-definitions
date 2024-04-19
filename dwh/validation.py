from typing import Optional

from pydantic import BaseModel, Field, model_validator


class UserAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean)
    create_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_ts: Mapped[datetime.datetime] = mapped_column(DateTime)
    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        is_deleted = self["is_deleted"]
        if (not id):
            raise ValueError("айдишника нет")
        if (isdigit(id)!=True):
            id = ''.join(c if c.isdigit() else '' for c in line)


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
        id = self["id"]
        name = self["name"]
        parent_id = self["parent_id"]
        if (not parent_id):
            raise ValueError("айдишника не")
        if (isdigit(parent_id) != True):
            parent_id = ''.join(c if c.isdigit() else '' for c in line)
        if (not id):
            raise ValueError("айдишника не")
        if (isdigit(id) != True):
            id = ''.join(c if c.isdigit() else '' for c in line)
        k = 0
        for i in range(len(name)):
            if not (name[i]).isalpha():
                if (name[i] == ' ') and ((i != 0) or (i != len(name))):
                    k = k + 1
                    if k > 1:
                    name = name.replace(name[i],'')
                else:
                    name = name.replace(name[i], '')
            if (name[i] == 'ё'):
              name = name.replace(name[i], 'е')
            name = name.title()


        return self
class UserGroupAuth(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    group_id: Mapped[int] = mapped_column(Integer)
    is_deleted: Mapped[bool] = mapped_column(Boolean)

    @model_validator(mode='before')
    def validate_card(self):
        id = self["id"]
        user_id = self["user_id"]
        group_id = self["group_id"]

        if (not id):
            raise ValueError("айдишника нет")
        if (isdigit(id) != True):
            id = ''.join(c if c.isdigit() else '' for c in id)
        if (not user_id):
            raise ValueError("айдишника нет, привед медвед")
        if (isdigit(user_id) != True):
            user_id = ''.join(c if c.isdigit() else '' for c in user_id)

