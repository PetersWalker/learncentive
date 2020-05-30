'''This module contains the instance of the Flask App, Cache, API endpoints
and vanilla routes'''

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from learncentive.resource.problem_set import ProblemSet
from learncentive.src.cache import cache

#FLASK APP
app = Flask('app')
CORS(app)

#initialize cache object with app

cache.init_app(app, config={'CACHE_TYPE':'simple'})


#API
api = Api(app)
api.add_resource(ProblemSet,
                 '/api/problem_set/<int:amount_of_probs>/<string:type_of_prob>'
                 )

#VANILLA ROUTES
@app.route('/')
def home():
    return "learncentive"

#CONFIGURATIONS, FLASK_APP & FLASK_ENV settings are in .flaskenv
app.config.update(
    CACHE_TYPE='simple',
    CACHE_DEFAULT_TIMEOUT=300
    )
