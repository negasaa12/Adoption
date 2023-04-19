from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    species = db.Column(db.String(50), nullable=False)

    photo_url = db.Column(db.Text, nullable=True)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, default=True)
