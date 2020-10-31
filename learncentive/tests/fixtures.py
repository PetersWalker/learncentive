import pytest

from learncentive.app import create_app
from learncentive.config import TestConfig
from learncentive.extensions import db
from learncentive.seed import problem_content
from learncentive.blueprints.users.models import User
from learncentive.blueprints.problem_generation.models import ArithemticProblem


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()
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


def seed_test_db():
    for problem in problem_content:
        db.session.add(ArithemticProblem(
            difficulty=problem['difficulty'],
            format=problem['format'],
            values_needed=problem['values_needed']
        ))
    db.session.add(User(
        name='test_user',
        email='test_user@learncentive.com',
        password='test',
    ))
    db.session.commit()

def login(c):
    data = {'email':'test_user@learncentive.com', 'password':'test'}
    c.post('users/token/auth', data=data)
