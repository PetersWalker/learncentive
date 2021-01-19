from learncentive.app import create_app
from learncentive.config import TestConfig


def test_config_is_set():
    app = create_app(TestConfig())
    assert app.config['WTF_CSRF_ENABLED'] == False
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://peterwalker:7011@localhost/learncentive_test_db'
