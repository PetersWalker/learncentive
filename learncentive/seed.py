import click
from flask.cli import with_appcontext

from learncentive.extensions import db
from learncentive.blueprints.problem_generation.models import ArithemticProblem


@click.command('seed')
@with_appcontext
def seed_database():
    if input('this will drop the database are you sure? (type yes or no):  ') == 'yes':
        db.drop_all()
        db.create_all()
        for problem in problem_content:

            db.session.add(ArithemticProblem(
                difficulty =problem['difficulty'],
                format=problem['format'],
                values_needed=problem['values_needed']
            ))

        db.session.commit()
    else:
        print('aborted')


problem_content = [
    {'difficulty': 0, 'format': '{}+{}', 'values_needed': 2},
    {'difficulty': 1, 'format': '{}-{}', 'values_needed': 2},
    {'difficulty': 2, 'format': '{}*{}', 'values_needed': 2},
    {'difficulty': 3, 'format': '{}/{}', 'values_needed': 2},
    {'difficulty': 4, 'format': '{}+{}+{}', 'values_needed': 3}
]