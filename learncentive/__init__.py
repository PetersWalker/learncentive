from learncentive.app import create_app
from learncentive.config import DevelopmentConfig


config = DevelopmentConfig()
app = create_app(config)
