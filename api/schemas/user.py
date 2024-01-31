from apiflask import Schema, fields
from schemas.purchases import PurchasesSchema
from schemas.wallet import WalletSchema

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    wallet_relation = fields.Nested(WalletSchema(only=('id', 'cash')))
    purchases_relation = fields.List(fields.Nested(PurchasesSchema))

class UsersSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    wallet_relation = fields.Nested(WalletSchema(only=('id', 'cash')))