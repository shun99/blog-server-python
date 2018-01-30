# 用户相关
from flask import Blueprint

# ../  表示是返回上一级目录
user = Blueprint('user', __name__)

from . import auth
