from flask import request
from functools import wraps
from app.models.user import Auth


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        Auth.verify_token(request.headers['userId'], request.headers['token'])
        return func(*args, **kwargs)

    return wrapper
