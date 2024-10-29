from flask import Blueprint
from .controllers import create_user, get_user, update_user, delete_user

users_bp = Blueprint('users', __name__)

users_bp.route('/register', methods=['POST'])(create_user)
users_bp.route('/<int:user_id>', methods=['GET'])(get_user)
users_bp.route('/<int:user_id>', methods=['PUT'])(update_user)
users_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user)
