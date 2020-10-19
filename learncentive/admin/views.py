from flask_admin.contrib.sqla import ModelView

from learncentive.extensions import db
from learncentive.blueprints.users.models import User
from learncentive.blueprints.problem_generation.models import ArithemticProblem


def configure_admin_views(admin):
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(ArithemticProblem, db.session))
