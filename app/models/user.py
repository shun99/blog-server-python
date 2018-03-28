from app.utils.AppException import AppException
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

    def inset_one(self):
        nam_count = mongo.db.users.find({"tel": self.tel}).count()
        if self.tel is None:
            raise AppException("tel can not empty")
        if self.phone is None:
            raise AppException("phone can not empty")
        if nam_count > 0:
            raise AppException("Phone number has been registered")
        return objectIdToId(mongo.db.users.insert(self.__dict__))

    @staticmethod
    def get_des(tel):
        data = mongo.db.users.find_one({"tel": tel})
        if None is data:
            raise Exception("Phone number no registered")
        return objectIdToId(data)

    @staticmethod
    def verify_pwd(tel, pwd):
        data = mongo.db.users.find_one({"tel": tel})
        if None is data:
            raise AppException("Phone number no registered")
        if data['pwd'] != pwd:
            raise AppException("pwd error")
        return objectIdToId(data)

    @staticmethod
    def verify_token(user_id, token):
        data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if None is data:
            raise AppException("user no exit", 422)
        if data['token'] != token:
            raise AppException("token is not valid", 422)
