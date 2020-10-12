from learncentive.users.models import User
from learncentive.tests.test_client import client
from learncentive.extensions import db

# previous from psycop2 only, no SQLAlchemy




# def test_add_and_retrieve_of_user_grades(client):
#     db.drop_all()
#     db.create_all()
#     grades = [.95, .92]
#     new_user = User(name='admin',
#                     email='admin@example.com',
#                     password='password',
#                     grades=grades
#                     )
#     db.session.add(new_user)
#     db.session.commit()
#     user = User.query.filter_by(name='admin').first()
#     assert user.grades == [.95, .92]
#

"""assert Table('user', MetaData(bind=None), Column('id', Integer(), table=<user>, primary_key=True, nullable=False), Column('name', String(length=80), table=<user>, nullable=False), Column('email', String(length=120), table=<user>, nullable=False), Column('password', String(length=120), table=<user>, nullable=False), Column('grades', JSON(astext_type=Text()), table=<user>), schema=None)"""


# connection = psycopg2.connect(dbname='learncentive_test_db', user='postgres', password='7011')
