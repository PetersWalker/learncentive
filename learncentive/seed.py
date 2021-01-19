import click
from flask.cli import with_appcontext
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.schema import DropConstraint, DropTable, MetaData, Table

from learncentive.extensions import db
from learncentive.blueprints.classroom.models import User, Grades, Course, ProblemDefinition


@click.command('seed')
@with_appcontext
def seed_database():
    if input('this will drop the development database are you sure? (type yes or no):  ') == 'yes':
        db.drop_cascading()
        db.create_all()
        """
        admin = {
    'name': 'admin',
    'email': 'admin@learncentive.com',
    'password': 'admin',
    'confirm': 'admin'
        }
        db.session.add(User(admin))
        db.session.commit()
        """
    else:
        print('aborted')


def seed_test_db():
    user = User(
        name='test_user',
        email='test_user@learncentive.com',
        password='test',
    )
    arithmetic = Course(
        grade_level=0,
        subject='Arithmetic'
    )
    grades = Grades(
        user=user,
        course=arithmetic,
        grades=[.96, .75]
    )
    arithmetic_problem_definitions = [
        {'difficulty': 0, 'format': '{}+{}', 'values_needed': 2},
        {'difficulty': 1, 'format': '{}-{}', 'values_needed': 2},
        {'difficulty': 2, 'format': '{}*{}', 'values_needed': 2},
        {'difficulty': 3, 'format': '{}/{}', 'values_needed': 2},
        {'difficulty': 4, 'format': '{}+{}+{}', 'values_needed': 3}
    ]

    for problem in arithmetic_problem_definitions:
        db.session.add(
            ProblemDefinition(
            difficulty=problem['difficulty'],
            format=problem['format'],
            values_needed=problem['values_needed'],
            course=arithmetic
            )
        )
    db.session.add(user)
    db.session.add(arithmetic)
    db.session.add(grades)
    db.session.commit()

def drop_cascading():
    """
    **nice bit of code to deal with dropping a table with foreign keys from here: https://github.com/pallets/flask-sqlalchemy/issues/722

    (On a live db) drops all foreign key constraints before dropping all tables.
    Workaround for SQLAlchemy not doing DROP ## CASCADE for drop_all()
    (https://github.com/pallets/flask-sqlalchemy/issues/722)
    """

    con = db.engine.connect()
    trans = con.begin()
    inspector = Inspector.from_engine(db.engine)

    # We need to re-create a minimal metadata with only the required things to
    # successfully emit drop constraints and tables commands for postgres (based
    # on the actual schema of the running instance)
    meta = MetaData()
    tables = []
    all_fkeys = []

    for table_name in inspector.get_table_names():
        fkeys = []

        for fkey in inspector.get_foreign_keys(table_name):
            if not fkey["name"]:
                continue

            fkeys.append(db.ForeignKeyConstraint((), (), name=fkey["name"]))

        tables.append(Table(table_name, meta, *fkeys))
        all_fkeys.extend(fkeys)

    for fkey in all_fkeys:
        con.execute(DropConstraint(fkey))

    for table in tables:
        con.execute(DropTable(table))

    trans.commit()
