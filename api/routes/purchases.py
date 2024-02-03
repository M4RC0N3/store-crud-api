from apiflask import APIBlueprint, abort
from flask import request, Response
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
import json
import logging

from app import db
from models import Purchases, User, Wallet, Product
from schemas import PurchasesSchema, ProductSchema, UsersSchema, WalletSchema

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
    cash = 0
    product_price = 0

    wallet_query = select(Wallet).filter_by(user_id=body["user_id"])
    try:
        wallet = db.session.execute(wallet_query).scalar_one()
        cash = wallet.cash
    except NoResultFound:
        return abort(404, "Wallet compatible user not found")

    product_query = select(Product).filter_by(id=body["product_id"])
    try:
        product = db.session.execute(product_query).scalar_one()
        product_price = product.price

    except NoResultFound:
        return abort(404, "Product not found")

    if can_buy(cash, product_price):
        wallet_discount = cash - product_price

        try:
            wallet.cash = wallet_discount
            db.session.commit()
        except Exception as e:
            db.rollback()
            return abort(400, str(e))
        finally:
            db.session.close()
    else:
        return abort(404, "The customer does not have enough balance to purchase the product")

def can_buy(wallet_cash, product_price):
    if wallet_cash >= product_price:
        return True
    else:
       return False