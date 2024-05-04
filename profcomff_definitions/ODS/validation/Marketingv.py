


#Marketing
class UserM(BaseModel):
    id: int =  Field(primary_key=True)
    union_number: int
    user_agent: str
    auth_user_id: int
    modify_ts: datetime.datetime
    create_ts: datetime.datetime
class ActionsInfoM(BaseModel):
    id: int = Field(primary_key=True)
    user_id: int
    action: str
    path_from: str
    path_to: str
    additional_data: str
    create_ts: datetime.datetime
#Physics
class ContactsPh(BaseModel):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=True)
    email: EmailStr
    phone: int = Field(nullable=True)
    workplace: int = Field(nullable=True)
    upload_ts: datetime =Field(default=func.now())

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
