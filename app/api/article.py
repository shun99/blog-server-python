import logging

from flask import request
from webargs import fields
from webargs.flaskparser import use_args

from app.models import Article
from app.wraps.error import robust
from app.wraps.token import token_required
from .base import BaseResource

logging.basicConfig(level=logging.INFO)

article_get_args = {
    'article_id': fields.Str(require=True)
}

article_get_list_args = {
    'type': fields.Int(),
    'page': fields.Int(),
    'size': fields.Int()
}

article_post_args = {
    'title': fields.Str(require=True),
    'des': fields.Str(require=True),
    'content': fields.Str(require=True),
    'articleType': fields.List(fields.Int())
}

article_put_args = {
    'article_id': fields.Str(require=True),
    'title': fields.Str(require=True),
    'des': fields.Str(require=True),
    'content': fields.Str(require=True),
    'articleType': fields.List(fields.Int())
}


class ArticleRes(BaseResource):
    @robust
    @use_args(article_get_args)
    def get(self):
        return Article.get_one(request.args.get('article_id'))

    @robust
    @token_required
    @use_args(article_post_args)
    def post(self, args):
        article_obj = Article(args.get('title'),
                              args.get('des'),
                              args.get('content'),
                              args.get('articleType'))
        return article_obj.post()

    @robust
    @token_required
    @use_args(article_put_args)
    def put(self, args):
        data = Article.put_one(request.json['article_id'],
                               Article(
                                   args.get('title'),
                                   args.get('des'),
                                   args.get('content'),
                                   args.get('articleType'))
                               )
        return data


class ArticleListRes(BaseResource):
    @robust
    @use_args(article_get_list_args)
    def get(self, args):
        data = Article.get_list(args.get('type'),
                                args.get('page'),
                                args.get('size'))
        return data
