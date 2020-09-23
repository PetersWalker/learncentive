from learncentive.app import db
from learncentive.user.models import User
#previous frmo psycop2 only, no SQLAlchemy
#connection = psycopg2.connect(dbname='learncentive_test_db', user='postgres', password='7011')

def test_retrieval_of_user_info():
    db.create_all()
    assert db
