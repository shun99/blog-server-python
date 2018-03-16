from .base import BaseResource
from flask import jsonify, request
from app.models import Article
import logging

logging.basicConfig(level=logging.INFO)


class ArticleRes(BaseResource):
    def get(self):
        return Article.get_one(request.args.get('article_id'))

    def post(self):
        article_obj = Article(request.json['title'],
                              request.json['des'],
                              request.json['content'],
                              request.json['articleType'])
        return article_obj.post()

    def put(self):
        try:
            data = Article.put_one(request.json['article_id'],
                                   Article(
                                       request.json['title'],
                                       request.json['des'],
                                       request.json['content'])
                                   )
        except 'No Article':
            return jsonify({"msg": "文章不存在"})
        else:
            return data
