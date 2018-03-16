from .base import BaseResource
from ..models import Label
import logging
from flask import request
from app.wraps.token import token_required
from app.wraps.error import robust

logging.basicConfig(level=logging.INFO)


class LabelRes(BaseResource):
    def get(self):
        data = Label.get_one(request.json['labelId'])
        logging.info(data)
        return data

    @robust
    @token_required
    def post(self):
        label = Label(request.json['type'],
                      request.json['name'])
        return label.post()


class LabelListRes(BaseResource):
    def get(self):
        data = Label.get_list()
        return data
