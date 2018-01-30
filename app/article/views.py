from flask import jsonify
from . import article
import logging


@article.route('/')
def find():
    return jsonify({"title": "恭喜你看到这篇文章"})


@article.errorhandler(404)
def page_not_found(e):
    logging.debug(e)
    return jsonify({"error": "404"}), 404
