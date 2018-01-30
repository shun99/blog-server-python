# 标准的蓝图格式
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates', static_folder='../../static')

from . import errors, views
