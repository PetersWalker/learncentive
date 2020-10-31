from functools import wraps
from flask import redirect, url_for
from flask_jwt_extended import verify_fresh_jwt_in_request, verify_jwt_in_request


def jwt_required_else_redirect(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except:
            return redirect(url_for('users.refresh'))

    return wrapper

"""TODO: LOOKUP

For some reason using verify_fresh_jwt_in_request in this decorator results in 
response.headers.add("Access-Control-Allow-Origin", "http://localhost:8080/") being set to '*' vice 
the specified 'http://localhost:8080' what is going on here?
"""