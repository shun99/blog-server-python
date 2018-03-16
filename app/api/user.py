from flask import abort, jsonify, request
from app.models.user import User, Auth
from .base import BaseResource
from app.wraps.token import token_required
from app.wraps.error import robust


class UserRes(BaseResource):
    @robust
    def get(self):
        return User.get(request.json['tel'], request.json['pwd'])


class AuthLoginRes(BaseResource):
    @robust
    def post(self):
        return Auth.get_one(request.json['tel'], request.json['pwd'])


class AuthRegisterRes(BaseResource):
    @robust
    def post(self):
        data = Auth(tel=request.json['tel'], pwd=request.json['pwd'])
        return data.inset_one()
