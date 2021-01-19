from flask_admin.contrib.sqla import ModelView

from learncentive.extensions import db
from learncentive.blueprints.classroom.models import User, ProblemDefinition


def configure_admin_views(admin):
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(ProblemDefinition, db.session))
