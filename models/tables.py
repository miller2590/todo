from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, unique=True)
