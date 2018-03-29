from app.utils.AppException import AppException
from app.utils.string_format import objectIdToId
from .base import BaseModel, mongo


class Label(BaseModel):
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def post(self):
        nam_count = mongo.db.lables.find({"name": self.name}).count()
        if nam_count > 0:
            raise AppException('label name existing')

        type_count = mongo.db.lables.find({"type": self.type}).count()
        if type_count > 0:
            raise AppException('label type existing')

        mongo.db.lables.insert(self.__dict__)
        return objectIdToId(self.__dict__)

    @staticmethod
    def get_one(label_type):
        data = mongo.db.lables.find({'type': label_type})
        return objectIdToId(data)

    @staticmethod
    def get_list():
        data_list = list(mongo.db.lables.find({}, {"name": 1, "type": 1, "_id": 0}))
        return data_list
