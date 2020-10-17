from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('', methods=['get', 'post'])
def admin_homepage():
    return render_template('admin/dashboard.html')