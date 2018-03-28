from webargs import fields
from webargs.flaskparser import use_args

from app.models.user import Auth
from app.wraps.error import robust
from .base import BaseResource

user_login_args = {
    'tel': fields.Int(require=True),
    'pwd': fields.Str(require=True)
}

user_register_args = {
    'tel': fields.Int(require=True),
    'pwd': fields.Str(require=True)
}


class AuthLoginRes(BaseResource):
    @robust
    @use_args(user_login_args)
    def post(self, args):
        return Auth.get_one(args.get('tel'), args.get('pwd'))


class AuthRegisterRes(BaseResource):
    @robust
    @use_args(user_register_args)
    def post(self, args):
        data = Auth(tel=args.get('tel'), pwd=args.get('pwd'))
        return data.inset_one()
