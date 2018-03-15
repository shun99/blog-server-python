from . import b_label
from ..models import Label
import logging
from flask import request

logging.basicConfig(level=logging.INFO)


@b_label.route('/list', methods=['GET'])
def get_list():
    data = Label.get_list()
    logging.info(data)
    return data, [('Content-Type', 'application/json;charset=utf-8')]


@b_label.route('/', methods=['POST'])
def post():
    label = Label(request.json['type'],
                  request.json['name'])
    return label.post(), [('Content-Type', 'application/json;charset=utf-8')]
