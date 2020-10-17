from flask import Blueprint, render_template
from learncentive.home.static.content import catalog_content
from learncentive.users.forms.login_signup import SignupForm

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='home/static'
    )


@home.route('/', methods=['GET', 'POST'])
def home_page():
    form = SignupForm()
    return render_template('home.html', form=form)


@home.route('/catalog')
def catalog():
    return render_template('catalog.html', catalog_content=catalog_content)

