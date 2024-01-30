from apiflask import APIBlueprint
from flask import request, Response
import json
import logging

from app import db
from models import User, Purchases
from schemas import UserSchema, UsersSchema

user_routes = APIBlueprint("user", __name__)

@user_routes.get("/user-list")
@user_routes.output(UsersSchema)
def user_list():
    users = User.query.all()
    response_data = {"Users": UsersSchema(many=True).dump(users)}

    return Response(json.dumps(response_data), status=200, content_type="application/json")

@user_routes.get("/user-view/<user_id>")
@user_routes.output(UserSchema)
def user_view(user_id):
    user = User.query.get(user_id)
    if user:
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return result