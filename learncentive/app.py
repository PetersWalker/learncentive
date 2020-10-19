from flask import Flask

from learncentive.extensions import db, cors, cache, jwt
from flask_admin import Admin

# Import Blueprints
from learncentive.users.routes import users
from learncentive.problem_generation.routes import problem_generation
from learncentive.home.routes import home
from learncentive.classroom.routes import classroom
from learncentive.admin.views import configure_admin_views

from learncentive.seed import seed_database


# FLASK APP Factory
def create_app(config_obj):
    app = Flask('learncentive', template_folder='templates')
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    # configure admin views. registering flask admin with init_app causes blueprint name collisions.
    # see https://github.com/flask-admin/flask-admin/issues/910
    admin = Admin(app)
    configure_admin_views(admin)

    return app


def register_extensions(app):
    db.init_app(app)
    cors.init_app(app)
    cache.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(problem_generation, url_prefix='/problem_generation')
    app.register_blueprint(home, url_prefix='')
    app.register_blueprint(classroom)


def register_commands(app):
    app.cli.add_command(seed_database)
