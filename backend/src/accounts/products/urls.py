from flask import Blueprint
from .controllers import create_product, get_all_products, get_product, update_product, delete_product

products_bp = Blueprint('products', __name__)

# Add routes for product CRUD operations
products_bp.route('/create-product', methods=['POST'])(create_product)      # Create
products_bp.route('/all', methods=['GET'])(get_all_products)                # Read All
products_bp.route('/<int:product_id>', methods=['GET'])(get_product)        # Read One
products_bp.route('/<int:product_id>', methods=['PUT'])(update_product)     # Update
products_bp.route('/<int:product_id>', methods=['DELETE'])(delete_product)  # Delete
