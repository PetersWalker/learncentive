import pytest

from learncentive.app import create_app
from learncentive.config import TestConfig

@pytest.fixture
def client():
    app = create_app(TestConfig)

    with app.test_client() as test_client:
        yield test_client
