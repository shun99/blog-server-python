from flask import abort, jsonify, request
from app.models import User
from .base import BaseResource


class UserRes(BaseResource):
    def get(self):
        return User.get(request.json['tel'], request.json['pwd'])


class AuthRes(BaseResource):
    def get(self):
        return User.get(request.json['tel'], request.json['pwd'])

    def post(self):
        data = User(tel=request.json['tel'], pwd=request.json['pwd'])
        return data.insert_one()
