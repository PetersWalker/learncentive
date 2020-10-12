from learncentive.app import create_app
from learncentive.config import DevelopmentConfig


def test_config_is_set():
    app = create_app(DevelopmentConfig())
    assert app.config['CACHE_TYPE'] == 'simple'
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://peterwalker:7011@localhost/learncentive_test_db'
