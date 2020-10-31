# FLASK_APP & FLASK_ENV settings are in .flaskenv


class Config:
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300
    DEBUG = False
    SECRET_KEY = 'temp'
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URL'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # temporary!!!!!
    JWT_SECRET_KEY = 'temp'
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_REFRESH_COOKIE_PATH = '/users/token/refresh'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://peterwalker:7011@localhost/learncentive_dev_db'


class TestConfig(Config):
    WTF_CSRF_ENABLED = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://peterwalker:7011@localhost/learncentive_test_db'
