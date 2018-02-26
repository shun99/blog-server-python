from flask import jsonify, request, abort
from . import article
import logging


@article.route('/<article_id>')
def get(article_id):
    return jsonify({"title": "恭喜你看到这篇文章:" + article_id})


@article.route('/', methods=['POST'])
def post():
    try:
        return jsonify({"文章": "创建成功" + request.json['article']})
    except:
        abort(404)


@article.errorhandler(404)
def page_not_found(e):
    logging.debug(e)
    return jsonify({"error": "404"}), 404
