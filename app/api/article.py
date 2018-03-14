from flask import jsonify, request
from app.models import Article
from app.api import b_article
import logging

logging.basicConfig(level=logging.INFO)


@b_article.route('/')
def get():
    return Article.get_one(request.args.get('article_id')), [('Content-Type', 'application/json;charset=utf-8')]


@b_article.route('/', methods=['POST'])
def post():
    article_obj = Article(request.json['title'],
                          request.json['des'],
                          request.json['content'],
                          request.json['articleType'])
    return article_obj.post(), [('Content-Type', 'application/json;charset=utf-8')]


@b_article.route('/', methods=['PUT'])
def put_one():
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
        return data, [('Content-Type', 'application/json;charset=utf-8')]


@b_article.errorhandler(404)
def page_not_found(e):
    logging.debug(e)
    return jsonify({"error": "404"}), 404
