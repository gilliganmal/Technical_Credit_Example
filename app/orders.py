from flask import Blueprint, jsonify

orders_bp = Blueprint('orders', __name__, url_prefix='/api/v1/orders')

@orders_bp.route('/', methods=['GET'])
def list_orders():
    return jsonify([])  # Placeholder
