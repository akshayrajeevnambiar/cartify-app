from flask import request, jsonify
from .models import Product
from src import db

def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data.get('stock', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201


def get_all_products():

    # Retrieve pagination parameters from request arguments
    page = request.args.get('page', type=int)

    # setting the amount of data to be showed per page
    per_page = request.args.get('per_page', 10, type=int)

    # Query with pagination
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)

    # structuring the response
    response = {
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
        "products": [product.to_dict() for product in products.items]
    }

    return jsonify(response)

def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify(product.to_dict())

def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
