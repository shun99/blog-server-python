# 系统经常要用到很多全局配置变量以及多套环境（开发，测试，生产）配置变量，因此单独的使用配置文
# 件来进行配置可以做到方便管理。本示例项目主要包含加密使用的SECRET_KEY，发送邮件的相关配置，
# 数据库配置等


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:##Blog123A@127.0.0.1/blog'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:##Blog123A@127.0.0.1/blog'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:##Blog123A@127.0.0.1/blog'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
