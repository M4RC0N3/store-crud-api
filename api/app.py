from apiflask import APIFlask
from flask_migrate import Migrate
from flask_cors import CORS
import jwt
import os
import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import models

from routes import product_routes, purchases_routes

def create_app(debug=True):
    app = APIFlask(__name__)

    logging.basicConfig(level=logging.INFO)

    migrate = Migrate()

    testing = "Testando o limite de caracteres por linha definido no BLACK e testando se o pre-commit ira funcioncar corretamente."
    driver = os.environ["DB_DRIVER"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"{driver}://{user}:{password}@{host}:{port}/{db_name}"

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        db.create_all()

    app.register_blueprint(product_routes)
    app.register_blueprint(purchases_routes)
    
    return app


if __name__ == "__main__":
    app = create_app(debug=True)
