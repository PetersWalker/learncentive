from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import jwt_required

from learncentive.extensions import db
from learncentive.blueprints.users.models import User
from learncentive.blueprints.problem_generation.models import ArithemticProblem


def configure_admin_views(admin):
    admin.add_view(AuthorizedModelView(User, db.session))
    admin.add_view(AuthorizedModelView(ArithemticProblem, db.session))

class AuthorizedModelView(ModelView):

    def is_accessible(self):

        return False
