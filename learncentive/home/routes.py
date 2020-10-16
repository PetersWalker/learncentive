from flask import Blueprint, render_template
from learncentive.home.static.content import catalog_content
from learncentive.users.forms.register import RegistrationForm

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='home/static'
    )


@home.route('/', methods=['GET', 'POST'])
def home_page():
    form = RegistrationForm()
    return render_template('home.html', form=form)


@home.route('/catalog')
def catalog():
    return render_template('catalog.html', catalog_content=catalog_content)


@home.route('/about')
def about():
    return render_template('about.html')
