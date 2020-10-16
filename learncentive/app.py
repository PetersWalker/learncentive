from flask import Flask
from learncentive.extensions import db, cors, cache

# Import Blueprints
from learncentive.users.routes import users
from learncentive.problem_generation.routes import problem_generation
from learncentive.home.routes import home
from learncentive.classroom.routes import classroom


# FLASK APP Factory
def create_app(config_obj):
    app = Flask('__name__')
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    cors.init_app(app)
    cache.init_app(app)


def register_blueprints(app):
    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(problem_generation, url_prefix='/problem_generation')
    app.register_blueprint(home, url_prefix='')
    app.register_blueprint(classroom)
