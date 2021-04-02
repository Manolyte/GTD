
DBURI = "postgresql://postgres:0@localhost/GTD"

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DBURI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "123"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DBURI

class DevelopmentConfig(Config):
    DEBUG = True
