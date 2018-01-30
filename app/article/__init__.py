# 文章相关
from flask import Blueprint

# ../  表示是返回上一级目录
article = Blueprint('article', __name__, static_folder='../../static')

from . import views
