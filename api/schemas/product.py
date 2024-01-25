from apiflask import Schema, fields
from models import Product

class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    quantity = fields.Integer()
