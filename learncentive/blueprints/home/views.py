from flask import render_template, Blueprint

from learncentive.blueprints.home.static.content import catalog_content
from learncentive.blueprints.users.forms.login_signup import SignupForm

blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='home/static'
    )


@blueprint.route('/', methods=['GET', 'POST'])
def home_page():
    form = SignupForm()
    return render_template('home.html', form=form)


@blueprint.route('/catalog')
def catalog():
    return render_template('catalog.html', catalog_content=catalog_content)

