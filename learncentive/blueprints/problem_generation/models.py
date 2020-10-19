from learncentive.extensions import db

class ArithemticProblem(db.Model):
    difficulty = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    format =  db.Column(db.String, unique=False, nullable=False)
    values_needed = db.Column(db.Integer, unique=False, nullable=False)
