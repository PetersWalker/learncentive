'''This module contains the instance of the Flask App, Cache, API endpoints
and vanilla routes'''

from flask import Flask, render_template, url_for
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from learncentive.api.problem_set_generator import ProblemSetALaCarte, ProblemSetGenerator
from learncentive.problem_generation.cache import cache
from learncentive.config import DevelopmentConfig
from learncentive.frontend.catalog.content import catalog_content

#FLASK APP
app = Flask(
    'app',
    template_folder='./frontend/templates',
    static_folder='./frontend/static'
    )

#TODO: cross origin resource charing was necessary for react compatability,
#evaluate if necessary in staging
CORS(app)

#CONFIGURATIONS
app.config.from_object(DevelopmentConfig)

#Initialize database
db = SQLAlchemy(app)

#Initialize cache object with app
cache.init_app(app)

#API
api = Api(app)
api.add_resource(
    ProblemSetALaCarte,
    '/api/problem_set_generator/<int:amount_of_probs>/<int:type_of_prob>'
    )
api.add_resource(
    ProblemSetGenerator,
    '/api/problem_set_generator/<string:problem_set>'
    )

#VANILLA ROUTES
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', catalog_content=catalog_content)

@app.route('/about')
def about():
    return render_template('about.html')

#REACT frontend
@app.route('/classroom')
def classroom_app():
    return render_template('classroom.html')

#CONFIGURATIONS, FLASK_APP & FLASK_ENV settings are in .flaskenv
app.config.update(
    CACHE_TYPE='simple',
    CACHE_DEFAULT_TIMEOUT=300
    )
