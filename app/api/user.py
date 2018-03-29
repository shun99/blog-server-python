from webargs import fields
from webargs.flaskparser import use_args

from app.models.user import User
from app.wraps.error import robust
from .base import BaseResource
from app import constants
from app.utils.string_format import app_response

user_login_args = {
    constants.phone: fields.Str(require=True),
    constants.password: fields.Str(require=True)
}

user_register_args = {
    constants.phone: fields.Str(require=True),
    constants.password: fields.Str(require=True)
}


class AuthLoginRes(BaseResource):
    @robust
    @use_args(user_login_args)
    def post(self, args):
        data = User.verify_pwd(args.get(constants.phone), args.get(constants.password));
        return app_response(data)


class AuthRegisterRes(BaseResource):
    @robust
    @use_args(user_register_args)
    def post(self, args):
        data = User.inset_one(args.get(constants.phone), args.get(constants.password))
        return app_response(data)
