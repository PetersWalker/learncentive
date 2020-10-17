from flask_admin.contrib.sqla import ModelView

from learncentive.extensions import admin, db
from learncentive.users.models import User

def configure_admin_view():
    admin.add_view(ModelView(User, db.session))
