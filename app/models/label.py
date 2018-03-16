from .base import BaseModel, mongo
from app.utils.string_format import objectIdToId
from json import dumps


class Label(BaseModel):
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def post(self):
        nam_count = mongo.db.lables.find({"name": self.name}).count()
        if nam_count > 0:
            return dumps({"errorMsg": "label name existing"})

        type_count = mongo.db.lables.find({"type": self.type}).count()
        if type_count > 0:
            return dumps({"errorMsg": "label type existing"})

        mongo.db.lables.insert(self.__dict__)
        return objectIdToId(self.__dict__)

    @staticmethod
    def get_one(label_type):
        data = dumps(mongo.db.lables.find({'type': label_type}))
        return data

    @staticmethod
    def get_list():
        data = dumps(mongo.db.lables.find({}, {"name": 1, "type": 1, "_id": 0}))
        return data
