from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__, url_prefix='/api/v1/products')

# TC: Using versioned API endpoints
PRODUCTS = [
    {"id": 1, "name": "Widget", "price": 10.99},
    {"id": 2, "name": "Gadget", "price": 23.99},
]

@products_bp.route('/', methods=['GET'])
def list_products():
    return jsonify(PRODUCTS)
