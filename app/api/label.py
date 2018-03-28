import logging

from webargs import fields
from webargs.flaskparser import use_args

from app.wraps.error import robust
from app.wraps.token import token_required
from .base import BaseResource
from ..models import Label

logging.basicConfig(level=logging.INFO)

label_get_args = {
    'labelId': fields.Str(require=True)
}

label_post_args = {
    'type': fields.Int(require=True),
    'name': fields.Str(require=True)
}


class LabelRes(BaseResource):
    @robust
    @use_args(label_get_args)
    def get(self, args):
        data = Label.get_one(args.get('labelId'))
        logging.info(data)
        return data

    @robust
    @token_required
    @use_args(label_get_args)
    def post(self, args):
        label = Label(args.get('type'),
                      args.get('name'))
        return label.post()


class LabelListRes(BaseResource):
    @robust
    def get(self):
        data = Label.get_list()
        return data
