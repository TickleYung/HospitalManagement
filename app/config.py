import os


class Config:
    # 这边进行自定义
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    PORT = 8080

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql+pymysql://root:gxy151o11,A@localhost/hsp'  # 后面自己填写连接数据库


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}