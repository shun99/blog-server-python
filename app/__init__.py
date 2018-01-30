from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    # 注册路由
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .article import article as article_blueprint
    app.register_blueprint(article_blueprint, url_prefix='/api/article')

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/user')
    return app
