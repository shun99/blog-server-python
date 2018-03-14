from .base import BaseModel, ObjectId, mongo, JSONEncoder
import logging

logging.basicConfig(level=logging.INFO)


class Article(BaseModel):
    def __init__(self, title='标题', des='没有描述', content='内容', sort=[0]):
        BaseModel.__init__(self)
        self.title = title
        self.des = des
        self.content = content
        self.sort = sort

    def post(self):
        mongo.db.articles.insert(self.__dict__)
        return JSONEncoder().encode(self.__dict__)

    @staticmethod
    def get_one(article_id):
        res = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        logging.debug(res)
        return JSONEncoder().encode(res)

    @staticmethod
    def put_one(article_id, article):
        # title = None, des = None, content = None
        data = mongo.db.articles.find_one({'_id': ObjectId(article_id)})
        if data is None:
            raise Exception('No Article')
        else:
            if article.title is None:
                data.title = article.title
            if article.des is None:
                data.des = article.des
            if article.content is None:
                data.content = article.content
            data = mongo.db.articles.update_one({'_id': ObjectId(article_id)}, {data})
        return JSONEncoder().encode(data)
