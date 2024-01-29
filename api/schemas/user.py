from apiflask import Schema, fields
from schemas.purchases import PurchasesSchema

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    purchases_relation = fields.List(fields.Nested(PurchasesSchema))
