import logging

from app.utils.AppException import AppException
from app.utils.string_format import objectIdToId
from .base import BaseModel, ObjectId, mongo
from app import constants

logging.basicConfig(level=logging.INFO)


class Article(BaseModel):
    def __init__(self, title='标题', des='没有描述', content='内容', type=[0], user_id=''):
        BaseModel.__init__(self)
        self.title = title
        self.des = des
        self.content = content
        self.type = type
        self.userId = user_id

    def post(self):
        if self.userId is None:
            raise AppException('userId can not empty')
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
            data_list = list(
                mongo.db.articles.find({'type': type}, {"_id": 1, "title": 1, "des": 1}).skip(size * (page - 1)).limit(
                    size + 1))
        for data in data_list:
            objectIdToId(data)
        more = len(data_list) > size
        return data_list[0:size], more

    @staticmethod
    def put_one(article_id, article):
        data = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        if data is None:
            raise AppException('No Article')
        else:
            verify_user(data[constants.article_user], article.userId)
            if article.title:
                data[constants.article_title] = article.title
            if article.des:
                data[constants.article_des] = article.des
            if article.content:
                data[constants.article_content] = article.content
            if article.type:
                data[constants.article_type] = article.type
            if article.update_time:
                data[constants.time_update] = article.update_time
            del (data['_id'])
            mongo.db.articles.update_one({'_id': ObjectId(article_id)}, {'$set': data})
            data = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
            return objectIdToId(data)


def verify_user(article_id, user_id):
    if article_id != user_id:
        raise AppException('No right')
