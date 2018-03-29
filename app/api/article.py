import logging

from webargs import fields
from webargs.flaskparser import use_args
from flask import request

from app.models import Article
from app.wraps.error import robust
from app.wraps.verify import token_verify
from .base import BaseResource
from app import constants
from app.utils.string_format import app_response

logging.basicConfig(level=logging.INFO)

article_get_args = {
    constants.article_id: fields.Str(require=True)
}

article_get_list_args = {
    constants.article_type: fields.Int(),
    constants.page: fields.Int(),
    constants.size: fields.Int()
}

article_post_args = {
    constants.article_title: fields.Str(require=True),
    constants.article_des: fields.Str(require=True),
    constants.article_content: fields.Str(require=True),
    constants.article_type: fields.List(fields.Int())
}

article_put_args = {
    constants.article_id: fields.Str(require=True),
    constants.article_title: fields.Str(),
    constants.article_des: fields.Str(),
    constants.article_content: fields.Str(),
    constants.article_type: fields.List(fields.Int())
}


class ArticleRes(BaseResource):
    @robust
    @use_args(article_get_args)
    def get(self, args):
        return app_response(Article.get_one(args.get(constants.article_id)))

    @robust
    @token_verify
    @use_args(article_post_args)
    def post(self, args):
        article_obj = Article(args.get(constants.article_title),
                              args.get(constants.article_des),
                              args.get(constants.article_content),
                              args.get(constants.article_type),
                              request.headers[constants.article_user])
        return app_response(article_obj.post())

    @robust
    @token_verify
    @use_args(article_put_args)
    def put(self, args):
        data = Article.put_one(args[constants.article_id],
                               Article(
                                   args.get(constants.article_type),
                                   args.get(constants.article_des),
                                   args.get(constants.article_content),
                                   args.get(constants.article_type),
                                   request.headers[constants.article_user])
                               )
        return app_response(data)


class ArticleListRes(BaseResource):
    @use_args(article_get_list_args)
    def get(self, args):
        data = Article.get_list(args.get(constants.article_type),
                                args.get(constants.page),
                                args.get(constants.size))
        return app_response(data[0], haveMore=data[1])
