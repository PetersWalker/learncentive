from learncentive.extensions import db
from sqlalchemy.dialects.postgresql import UUID, JSON

import json
import uuid


class User(db.Model):
    """ The User Model has a one to many relationship with the grades table"""
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    grades = db.relationship('Grades', backref='user', lazy=False)


class Grades(db.Model):
    """ A table listing the grades of many users who are taking many courses"""
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    grades = db.Column(JSON, default=json.dumps([0]))


class Course(db.Model):
    """ The Courses Model has a one to many relationship with the grades table"""
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    grade_level = db.Column(db.Integer, unique=False, nullable=False)
    subject = db.Column(db.String, unique=False, nullable=False)
    problems = db.relationship('ProblemDefinition', backref='course')
    grades = db.relationship('Grades', backref='course')


class ProblemDefinition(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    difficulty = db.Column(db.Integer, unique=True, nullable=False)
    format = db.Column(db.String, unique=False, nullable=False)
    values_needed = db.Column(db.Integer, unique=False, nullable=False)
