from flask import request, jsonify
from .models import Order
from ..products.models import Product
from src import db

def create_order():
    data = request.get_json()

    product = Product.query.get(data['product_id'])
    if not product or data['quantity'] > product.stock:
        return jsonify({"error": "Product unavailable or insufficient stock"}), 400
    
    new_order = Order(
        user_id=data['user_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        status='pending'
    )

    product.stock -= data['quantity']
    db.session.add(new_order)
    db.session.commit()

    return jsonify(new_order.to_dict())

def get_all_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())

def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    order.status = data.get('status', order.status)
    db.session.commit()
    return jsonify(order.to_dict())

def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully"})