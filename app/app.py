from flask import Flask
from flask_caching import Cache
from flask_restful import  Resource, Api

from random import randint, choice

from learncentive.resource import problem
#FLASK_APP
app = Flask('learncentive')

#CONFIGURATIONS, FLASK_APP & FLASK_ENV are in .flaskenv
app.config.update(
    CACHE_TYPE='simple',
    CACHE_DEFAULT_TIMEOUT=300
    )

#CACHE
cache = Cache(app)

#pre-generated random numbers for seeding problems
@cache.cached(key_prefix='random_bank')
def create_cached_random_bank():
    random_bank = {
        'operator':[choice(['x','+']) for x in range(1000)],
        'integer':[randint(2, 10) for x in range(1000)]
        }
    return random_bank

cached_random_bank = create_cached_random_bank()
#CACHE_DEFAULT_TIMEOUT
#CACHE_THRESHOLD
#CACHE_ARGS
#CACHE_OPTIONS

#API
api = API(app)

class ()

#VANILLA ROUTES
@app.route('/')
def index():
    return "learncentive"
