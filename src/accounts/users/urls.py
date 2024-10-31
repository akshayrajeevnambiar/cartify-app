from flask import Blueprint
from .controllers import register_user, get_user, update_user, delete_user, login_user
from flask_jwt_extended import jwt_required

users_bp = Blueprint('users', __name__)

users_bp.route('/register', methods=['POST'])(register_user) # register
users_bp.route('/<int:user_id>', methods=['GET'])(jwt_required()(get_user)) # get user
users_bp.route('/<int:user_id>', methods=['PUT'])(jwt_required()(update_user))  # update
users_bp.route('/<int:user_id>', methods=['DELETE'])(jwt_required()(delete_user)) # delete
users_bp.route('/login', methods=['POST'])(login_user)
