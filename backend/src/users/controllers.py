from flask import request, jsonify
from src import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity

# Creating a new User
def register_user():
    data = request.get_json()

    # Check whether an existing user
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "Email already exists"}), 409

    # Creating a new user
    hashed_password = generate_password_hash(data['password'])
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Generate JWT token upon successful registration
    access_token = create_access_token(identity=new_user.id)
    return jsonify({"message": "User registered successfully", "access_token": access_token}), 201

# Reading the user details
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# Updating the user details
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    user.email = data['email'] if 'email' in data else user.email
    user.name = data['name'] if 'username' in data else user.username
    user.password = data['password'] if 'password' in data else user.password

    db.session.commit()
    return jsonify(user.to_dict())

# Delete the User
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "user deleted successfully"})

# Route to check user login credentials
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    # Create JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

def adim_route() :
    current_user = User.query.get(get_jwt_identity())
    if current_user.role != 'admin':
        return jsonify({"error": "Access forbidden"}), 403
    # Do admin stuff here