from .base import BaseModel, mongo, ObjectId
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

    @staticmethod
    def get_one(tel):
        data = mongo.db.users.find_one({"tel": tel})
        if None is data:
            raise Exception("Phone number no registered")
        return objectIdToId(data)


class Auth(BaseModel):
    def inset_one(self):
        nam_count = mongo.db.users.find({"tel": self.tel}).count()
        if self.tel is None:
            raise Exception("tel can not empty")
        if self.phone is None:
            raise Exception("phone can not empty")
        if nam_count > 0:
            raise Exception("Phone number has been registered")
        return objectIdToId(mongo.db.users.insert(self.__dict__))

    @staticmethod
    def get_one(tel, pwd):
        data = mongo.db.users.find_one({"tel": tel})
        if None is data:
            raise Exception("Phone number no registered")
        if data['pwd'] != pwd:
            raise Exception("pwd error")
        return objectIdToId(data)

    @staticmethod
    def verify_token(user_id, token):
        data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if None is data:
            raise Exception("user no exit", 422)
        if data['token'] != token:
            raise Exception("token is not valid", 422)
