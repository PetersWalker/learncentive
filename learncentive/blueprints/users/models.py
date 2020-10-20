from sqlalchemy.dialects.postgresql import JSON, UUID
import uuid
from learncentive.extensions import db

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    grades = db.Column(JSON)

class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grades = db.Column(JSON)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
