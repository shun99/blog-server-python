from .base import BaseModel


class User(BaseModel):
    def __init__(self, username, email, tel, sex):
        BaseModel.__init__(self)
        self.username = username
        self.email = email
        self.tel = tel
        self.sex = sex
