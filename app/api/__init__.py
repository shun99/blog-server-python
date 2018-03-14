# 标准的蓝图格式
from flask import Blueprint

b_main = Blueprint('b_main', __name__, template_folder='..templates', static_folder='../../static')
b_article = Blueprint('b_article', __name__)
b_auth = Blueprint('b_auth', __name__)


@b_main.route('/')
def home():
    return b_main.send_static_file('index.html')


from . import errors
from . import article
from . import auth
