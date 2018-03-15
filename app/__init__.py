from flask import Flask
from flask_pymongo import PyMongo
from config import config

mongo = PyMongo()


def create_app(config_name):
    # import pdb # 断点
    # pdb.set_trace()
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mongo.init_app(app)

    # 注册路由
    from .api import b_main, b_article, b_auth, b_label
    app.register_blueprint(b_main)
    app.register_blueprint(b_article, url_prefix='/api/article')
    app.register_blueprint(b_auth, url_prefix='/api/user')
    app.register_blueprint(b_label, url_prefix='/api/label')
    return app
