from sqlalchemy.dialects.postgresql import  JSON
from learncentive.app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    grades = db.relationship('Grades', backref='user', lazy=True)

class Grades(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     subject = db.Column(db.String(80), unique=False, nullable=False)
     grade_json = db.Column(db.String(80), unique=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
