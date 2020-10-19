from flask import Blueprint, render_template, url_for
from flask_jwt_extended import jwt_required


classroom = Blueprint(
    'classroom',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/classroom/static'
)


@jwt_required
@classroom.route('/classroom')
def classroom_app():
    bundle = url_for('classroom.static', filename='js/react_dist/index_bundle.js')
    return render_template('classroom.html', react_bundle=bundle)
