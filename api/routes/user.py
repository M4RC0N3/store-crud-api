from apiflask import APIBlueprint, abort
from flask import request, Response
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select
import json
import logging

from app import db
from models import User, Purchases
from schemas import UserSchema, UsersSchema, OnlyUserDataSchema

user_routes = APIBlueprint("user", __name__)

@user_routes.get("/user-list")
@user_routes.output(UsersSchema)
def user_list():
    users = User.query.all()
    response_data = {"Users": UsersSchema(many=True).dump(users)}

    return Response(json.dumps(response_data), status=200, content_type="application/json")

@user_routes.get("/user-view/<user_id>")
@user_routes.output(OnlyUserDataSchema)
def user_view(user_id):
    try:
        user = db.session.query(User).filter_by(id=user_id).one()
        response_data = {"User": OnlyUserDataSchema().dump(user)}
        return Response(json.dumps(response_data), status=200, content_type="application/json")

    except NoResultFound:
        return abort (404, "user not found")