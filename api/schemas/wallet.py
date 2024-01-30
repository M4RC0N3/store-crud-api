from apiflask import Schema, fields

class WalletSchema(Schema):
    id = fields.Integer()
    cash = fields.Integer()
    user_id = fields.Integer()