from webargs import fields
from webargs.flaskparser import use_args

from app.models.user import User
from app.wraps.error import robust
from .base import BaseResource
from app import constants

user_login_args = {
    constants.tel: fields.Int(require=True),
    constants.pwd: fields.Str(require=True)
}

user_register_args = {
    constants.tel: fields.Int(require=True),
    constants.pwd: fields.Str(require=True)
}


class AuthLoginRes(BaseResource):
    @robust
    @use_args(user_login_args)
    def post(self, args):
        return User.vertify(args[constants.tel], args[constants.pwd])


class AuthRegisterRes(BaseResource):
    @robust
    @use_args(user_register_args)
    def post(self, args):
        data = User(tel=args[constants.tel], pwd=args[constants.pwd])
        return data.inset_one()
