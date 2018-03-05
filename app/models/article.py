from .base import BaseModel, mongo, JSONEncoder, ObjectId
import logging

logging.basicConfig(level=logging.INFO)


class Article(BaseModel):
    def __init__(self, title, des, content):
        BaseModel.__init__(self)
        self.title = title
        self.des = des
        self.content = content

    def save(self):
        mongo.db.articles.insert(self.__dict__)
        return JSONEncoder().encode(self.__dict__)

    @staticmethod
    def get_one(article_id):
        res = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        logging.debug(res)
        return JSONEncoder().encode(res)
