from flask import Flask
from flask_pymongo import PyMongo
from config import config
from flask_cors import CORS

mongo = PyMongo()


def create_app(config_name, blueprints=None):
    # import pdb # 断点
    # pdb.set_trace()
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*", "expose_headers": "X-Total"}})
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mongo.init_app(app)

    # 注册路由
    if blueprints is None:
        from .api import BLUEPRINTS
        blueprints_resister(app, BLUEPRINTS)
    return app


def blueprints_resister(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)
