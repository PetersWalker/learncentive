from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_admin import Admin

db = SQLAlchemy()
cors = CORS()
cache = Cache()
jwt = JWTManager()
admin = Admin()
