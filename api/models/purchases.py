from flask_sqlalchemy import SQLAlchemy
from app import db

class Purchases(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False,  unique=True)
    product_relation = db.relationship('Product', backref= "purchases", uselist=False)
