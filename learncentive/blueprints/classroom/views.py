from flask import render_template, url_for, Blueprint
from flask_jwt_extended import jwt_required


blueprint = Blueprint(
    'classroom',
    __name__,
    template_folder="templates",
    static_folder="static",
)


@blueprint.route('')
@jwt_required
def classroom_app():
    bundle = url_for('classroom.static', filename='js/react_dist/index_bundle.js')
    return render_template('classroom.html', react_bundle=bundle)
