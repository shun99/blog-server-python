import logging

from webargs import fields
from webargs.flaskparser import use_args

from app.wraps.error import robust
from app.wraps.token import token_required
from .base import BaseResource
from ..models import Label
from app import constants
from app.utils.string_format import app_response

logging.basicConfig(level=logging.INFO)

label_get_args = {
    constants.label_id: fields.Str(require=True)
}

label_post_args = {
    constants.label_type: fields.Int(require=True),
    constants.label_name: fields.Str(require=True)
}


class LabelRes(BaseResource):
    @robust
    @use_args(label_get_args)
    def get(self, args):
        data = Label.get_one(args.get(constants.label_id))
        logging.info(data)
        return app_response(data)

    @robust
    @token_required
    @use_args(label_get_args)
    def post(self, args):
        label = Label(args.get(constants.label_type),
                      args.get(constants.label_name))
        return app_response(label.post())


class LabelListRes(BaseResource):
    @robust
    def get(self):
        data = Label.get_list()
        return app_response(data)
