# 标准的蓝图格式
from flask import Blueprint
from flask_restful import Api

from app.api.article import ArticleRes
from app.api.user import UserRes, AuthRes
from app.api.label import LabelRes

api_bp_v1 = Blueprint('api_bp_v1', __name__)
api_v1 = Api(api_bp_v1, prefix='/api/v1')

api_v1.add_resource(ArticleRes, '/article')
api_v1.add_resource(UserRes, '/user')
api_v1.add_resource(AuthRes, '/auth')
api_v1.add_resource(LabelRes, '/label')

# 首页配置
bp_main = Blueprint('api_ba_1', __name__, template_folder='..templates', static_folder='../../static')
from . import main

BLUEPRINTS = [
    api_bp_v1,
    bp_main
]

__all__ = ['BLUEPRINTS']
