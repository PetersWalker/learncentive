import pytest

from learncentive.app import create_app
from learncentive.config import TestConfig
from learncentive.extensions import db

@pytest.fixture
def client():
    app = create_app(TestConfig)

    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield test_client


@pytest.fixture
def db_context():
    app = create_app(TestConfig)

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db