from .base import BaseResource
from ..models import Label
import logging
from flask import request

logging.basicConfig(level=logging.INFO)


class LabelRes(BaseResource):
    def get(self):
        data = Label.get_list()
        logging.info(data)
        return data, [('Content-Type', 'application/json;charset=utf-8')]

    def post(self):
        label = Label(request.json['type'],
                      request.json['name'])
        return label.post(), [('Content-Type', 'application/json;charset=utf-8')]
