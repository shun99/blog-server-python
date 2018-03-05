from flask import jsonify, request
from app.models import Article
from . import article
import logging

logging.basicConfig(level=logging.INFO)


@article.route('/')
def get():
    return Article.get_one(request.args.get('article_id')), [('Content-Type', 'application/json;charset=utf-8')]


@article.route('/', methods=['POST'])
def post():
    article_obj = Article(request.json['title'], request.json['des'], request.json['content'])
    return article_obj.save(), [('Content-Type', 'application/json;charset=utf-8')]


@article.errorhandler(404)
def page_not_found(e):
    logging.debug(e)
    return jsonify({"error": "404"}), 404
