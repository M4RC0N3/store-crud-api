from apiflask import Schema, fields

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()