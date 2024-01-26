from apiflask import APIBlueprint
from flask import request, Response
import json
import logging

from app import db
from models import Purchases
from schemas import PurchasesSchema, ProductSchema

purchases_routes = APIBlueprint("purchases", __name__)

@purchases_routes.get("/purchases-list")
@purchases_routes.output(PurchasesSchema)
def get_purchase():
    purchases = Purchases.query.all()
    response_data = {"Purchases": PurchasesSchema(many=True).dump(purchases)}
    return Response(json.dumps(response_data), status=200, content_type="application/json")