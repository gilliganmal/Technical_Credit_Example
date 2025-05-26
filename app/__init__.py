from flask import Flask
from .products import products_bp
from .orders import orders_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    return app
