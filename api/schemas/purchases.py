from apiflask import Schema, fields
from schemas.product import ProductSchema
#from schemas.user import UserSchema

class PurchasesSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    product_id = fields.Integer()
    product_relation = fields.Nested(ProductSchema(only=('id', 'name', 'price')))
