from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    purchases_relation = db.relationship("Purchases", backref="user", lazy='dynamic')
    