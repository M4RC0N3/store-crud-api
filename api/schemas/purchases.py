from apiflask import Schema, fields
from schemas.product import ProductSchema
#from schemas.user import UserSchema

class PurchasesSchema(Schema):
    id = fields.Integer()
    #user_id = fields.Integer()
    product_id = fields.Integer()
    # Inclua os campos específicos da entidade Purchases
    # Pode ser útil incluir esquemas para os modelos relacionados
    #user = fields.Nested(UserSchema, attribute='user', dump_only=True)
    product_relation = fields.Nested(ProductSchema(only=('id', 'name', 'price')))
