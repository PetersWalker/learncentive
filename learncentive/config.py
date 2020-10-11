#FLASK_APP & FLASK_ENV settings are in .flaskenv

class Config():
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT= 300
    DEBUG = False
    SECRET_KEY = 'temp'
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URL'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://peterwalker:7011@localhost/learncentive_test_db'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://peterwalker:7011@localhost/learncentive_test_db'

