from apiflask import APIBlueprint
from flask import request, Response
import json
import logging

from app import db
from models import User, Purchases
from schemas import UserSchema

user_routes = APIBlueprint("user", __name__)

@user_routes.get("/user-list")
@user_routes.output(UserSchema)
def user_list():
    users = User.query.all()
    response_data = {"Users": UserSchema(many=True).dump(users)}

    return Response(json.dumps(response_data), status=200, content_type="application/json")
