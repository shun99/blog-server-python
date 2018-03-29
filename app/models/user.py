from app.utils.AppException import AppException
from .base import BaseModel, mongo, ObjectId
import uuid
from app.utils.string_format import objectIdToId
from app import constants


class User(BaseModel):
    @staticmethod
    def inset_one(phone, password):
        if phone is None:
            raise AppException("phone can not empty")
        if password is None:
            raise AppException("password can not empty")
        nam_count = mongo.db.users.find({constants.phone: phone}).count()
        if nam_count > 0:
            raise AppException("Phone number has been registered")
        mongo.db.users.insert({
            constants.phone: phone,
            constants.password: password,
            constants.token: uuid.uuid4().hex
        })
        data = mongo.db.users.find_one({constants.phone: phone})
        return objectIdToId(data)

    @staticmethod
    def get_des(phone):
        data = mongo.db.users.find_one({constants.phone: phone})
        if None is data:
            raise Exception("Phone number no registered")
        return objectIdToId(data)

    @staticmethod
    def verify_pwd(phone, password):
        data = mongo.db.users.find_one({constants.phone: phone})
        if None is data:
            raise AppException("Phone number no registered")
        if data[constants.password] != password:
            raise AppException("password error")
        return objectIdToId(data)

    @staticmethod
    def verify_token(user_id, token):
        data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if None is data:
            raise AppException("user no exit", 422)
        if data[constants.token] != token:
            raise AppException("token is not valid", 422)
