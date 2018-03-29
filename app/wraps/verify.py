from flask import request
from functools import wraps
from app.models.user import User
from app.utils.AppException import AppException
from app import constants


def token_verify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            User.verify_token(request.headers[constants.article_user], request.headers[constants.token])
        except:
            raise AppException(data='toke不合法')
        return func(*args, **kwargs)

    return wrapper
