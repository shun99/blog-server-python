from .base import BaseModel, mongo
from json import dumps
import uuid
from app.utils.string_format import objectIdToId


class User(BaseModel):
    def __init__(self, tel, username='', email='', sex='', pwd=''):
        BaseModel.__init__(self)
        self.username = username
        self.email = email
        self.tel = tel
        self.sex = sex
        self.pwd = pwd
        self.token = uuid.uuid4().hex

    def insert_one(self):
        nam_count = mongo.db.users.find({"tel": self.tel}).count()
        if self.tel is None:
            return dumps({"errorMsg": "tel can't empty"})
        if self.phone is None:
            return dumps({"errorMsg": "phone can't empty"})
        if nam_count > 0:
            return dumps({"errorMsg": "Phone number has been registered"})
        return objectIdToId(mongo.db.users.insert(self.__dict__))

    @staticmethod
    def get(tel, pwd):
        data = mongo.db.users.find_one({"tel": tel, "pwd": pwd})
        if data is None:
            return dumps({"errorMsg": "登入失败"})
        return objectIdToId(data)
