from flask import request
from functools import wraps
from app.models.user import User
from app.utils.AppException import AppException


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            User.verify_token(request.headers['userId'], request.headers['token'])
        except:
            raise AppException(data='toke不合法')
        return func(*args, **kwargs)

    return wrapper
