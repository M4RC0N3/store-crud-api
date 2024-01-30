from flask_sqlalchemy import SQLAlchemy

from app import db

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cash = db.Column(db.Integer, nullable=False)
