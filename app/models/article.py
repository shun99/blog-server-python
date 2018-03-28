import logging

from app.utils.AppException import AppException
from app.utils.string_format import objectIdToId
from .base import BaseModel, ObjectId, mongo

logging.basicConfig(level=logging.INFO)


class Article(BaseModel):
    def __init__(self, title='标题', des='没有描述', content='内容', type=[0]):
        BaseModel.__init__(self)
        self.title = title
        self.des = des
        self.content = content
        self.type = type

    def post(self):
        mongo.db.articles.insert(self.__dict__)
        return objectIdToId(self.__dict__)

    @staticmethod
    def get_one(article_id):
        res = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        return objectIdToId(res)

    @staticmethod
    def get_list(type, page=1, size=10):
        if type == 0:
            data_list = list(mongo.db.articles.find().skip(size * (page - 1)).limit(size))
        else:
            data_list = list(mongo.db.articles.find({'type': type}, {"_id": 1, "title": 1, "des": 1}).skip(size * (page - 1)).limit(size))
        for data in data_list:
            objectIdToId(data)
        return data_list

    @staticmethod
    def put_one(article_id, article):
        data = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        if data is None:
            raise AppException('No Article')
        else:
            if article.title:
                data['title'] = article.title
            if article.des:
                data['des'] = article.des
            if article.content:
                data['content'] = article.content
            if article.type:
                data['type'] = article.type
            del (data['_id'])
            mongo.db.articles.update_one({'_id': ObjectId(article_id)}, {'$set': data})
            data = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
            return objectIdToId(data)
