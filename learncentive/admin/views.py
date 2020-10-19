from flask_admin.contrib.sqla import ModelView

from learncentive.extensions import db
from learncentive.users.models import User


def configure_admin_views(admin):
    admin.add_view(ModelView(User, db.session))
