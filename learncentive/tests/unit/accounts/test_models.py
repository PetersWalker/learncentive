from learncentive.app import db
from learncentive.accounts.models import User
import json
#previous frmo psycop2 only, no SQLAlchemy
#connection = psycopg2.connect(dbname='learncentive_test_db', user='postgres', password='7011')

def test_retrieval_of_user_grades():
    db.drop_all()
    db.create_all()
    grades = [.95, .92]
    new_user = User(name = 'admin',
                    email = 'admin@example.com',
                    password = 'password',
                    grades = grades
                    )
    db.session.add(new_user)
    db.session.commit()
    user = User.query.filter_by(name = 'admin').first()
    assert user.grades == [.95, .92]

"""assert Table('user', MetaData(bind=None), Column('id', Integer(), table=<user>, primary_key=True, nullable=False), Column('name', String(length=80), table=<user>, nullable=False), Column('email', String(length=120), table=<user>, nullable=False), Column('password', String(length=120), table=<user>, nullable=False), Column('grades', JSON(astext_type=Text()), table=<user>), schema=None)"""
