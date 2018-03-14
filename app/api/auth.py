from flask import abort, jsonify

from app.api import b_auth


@b_auth.route('/', methods=['GET'])
@b_auth.route('/login', methods=['POST'])
def login():
    # abort(404)
    return jsonify({"title": "登入成功"})


@b_auth.errorhandler(404)
def page_not_found(e):
    return jsonify({"title": "登入失败"}), 404
