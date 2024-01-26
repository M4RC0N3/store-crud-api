from flask_sqlalchemy import SQLAlchemy
from apiflask import Schema, fields
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name  = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer(), nullable=False, default=0)
    quantity = db.Column(db.Integer(), nullable=False, default=0)
    #purchases_relation = db.relationship("Purchases", backref='product')