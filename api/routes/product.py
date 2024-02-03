from apiflask import APIBlueprint
from flask import request, Response
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
import json
import logging

from models import Product
from schemas import ProductSchema
from app import db
product_routes = APIBlueprint("products", __name__)

@product_routes.get("/product-list")
@product_routes.output(ProductSchema)
def get_products():
   products = Product.query.all()

   response_data = {"products": ProductSchema(many=True).dump(products)}

   logging.info(products)
   return Response(json.dumps(response_data), status=200, content_type="application/json")

@product_routes.post("/product-new")
@product_routes.input(ProductSchema)
@product_routes.output(ProductSchema)
def create_product(json_data):
   body = request.get_json()

   new_product = Product(name=body["name"], price=body["price"], quantity=body["quantity"])

   db.session.add(new_product)

   try:
      db.session.commit()
      return Response(json.dumps(ProductSchema().dump(new_product)), status=201, content_type="application/json")
   except Exception as e:
      db.session.rollback()
      return Response(json.dumps({"erros": str(e)}), status=400, content_type="application/json")
   finally:
      db.session.close()

@product_routes.put("/product-change")
@product_routes.input(ProductSchema)
@product_routes.output(ProductSchema)
def update_product(json_data):
   product_query = select(Product).filter_by(id=json_data.get("id"))
   product = db.session.execute(product_query).scalar_one()
   try:

      if "name" in json_data:
         product.name = json_data["name"]
      if "price" in json_data:
         product.price = json_data["price"]
      if "quantity" in json_data:
         product.quantity = json_data["quantity"]

      db.session.commit()

      response_data = {
         "message": "Product edits successfully",
         "product": ProductSchema().dump(product)
      }
      return Response(json.dumps(response_data), status=200, content_type="application/json")

   except NoResultFound:
      db.session.rollback()
      return abort(404, "Product not found")

   finally:
      db.session.close()

@product_routes.delete("/product-delete")
@product_routes.input(ProductSchema)
@product_routes.output(ProductSchema)
def delete_product(json_data):
   product_query = select(Product).filter_by(id=json_data.get("id"))
   product = db.session.execute(product_query).scalar_one()
   try:
      db.session.delete(product)
      db.session.commit()

      return Response(json.dumps({"message": "Product deleted successfully"}), status=200, content_type="application/json")

   except Exception as e:
      db.session.rollback()
      return Response(json.dumps({"error": str(e)}), status=400, content_type="application/json")

   finally:
      db.session.close()