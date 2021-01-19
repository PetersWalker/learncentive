import pytest

from learncentive.app import create_app
from learncentive.config import TestConfig
from learncentive.extensions import db
from learncentive.seed import seed_test_db


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            seed_test_db()
        yield test_client


@pytest.fixture
def authorized_client():
    app = create_app(TestConfig)
    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            seed_test_db()
            login(test_client)
        yield test_client


@pytest.fixture
def db_context():
    app = create_app(TestConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db




def login(c):
    data = {'email':'test_user@learncentive.com', 'password':'test'}
    c.post('users/token/auth', data=data)
