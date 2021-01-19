from learncentive.tests.fixtures import db_context


def test_connetion_to_db(db_context):
    assert db_context.session()
