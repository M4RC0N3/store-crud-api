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

@purchases_routes.post("/purchases-new")
@purchases_routes.input(PurchasesSchema)
@purchases_routes.output(PurchasesSchema)
def purchase_new(json_data):
    body = request.get_json()
    
    new_purchases = Purchases(user_id=body["user_id"], product_id=body["product_id"])

    db.session.add(new_purchases)

    try:
        db.session.commit()
        return Response(json.dumps(PurchasesSchema().dump(new_purchases)), status=201, content_type="application/json")
    except Exception as e:
        db.session.rollback()
        return Response(json.dumps({"erros": str(e)}), status=400, content_type="application/json")
    finally:
        db.session.close()