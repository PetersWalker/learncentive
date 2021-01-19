from learncentive.extensions import db
from sqlalchemy.dialects.postgresql import UUID


class ArithemticProblem(db.Model):
    difficulty = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    format = db.Column(db.String, unique=False, nullable=False)
    values_needed = db.Column(db.Integer, unique=False, nullable=False)


class Course(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    grade_level = db.Column(db.Integer, unique=False, nullable=False)
    subject = db.Column(db.String, unique=False, nullable=False)
    age_group = db.Column(db.Integer, unique=False, nullable=True)
    problems = db.relationship('Problems', backref='course')


class Problems(db.Model):
    id = db.Column(db.ForeignKey('course.id'), primary_key=True, nullable=False)
    difficulty = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    format = db.Column(db.String, unique=False, nullable=False)
    values_needed = db.Column(db.Integer, unique=False, nullable=False)
