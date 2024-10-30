from flask import Blueprint
from .controllers import create_order, get_user_orders, get_order, update_order_status, delete_order

orders_bp = Blueprint('orders', __name__)

orders_bp.route('/create-order', methods=['POST'])(create_order)  # Create Order
orders_bp.route('/cart', methods=['GET'])(get_user_orders)  # Get All Orders
orders_bp.route('/<int:order_id>', methods=['GET'])(get_order)  # Get Order by ID
orders_bp.route('/<int:order_id>', methods=['PUT'])(update_order_status)  # Update Order Status
orders_bp.route('/<int:order_id>', methods=['DELETE'])(delete_order)  # Delete Order