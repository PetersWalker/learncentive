from flask import Blueprint

problem_generation = Blueprint('problem_generation', __name__)

from . import views
