from flask import request, jsonify
from src import db
from .models import User

# Creating a new User
def create_user():
    data = request.get_json()

    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "Email already exists"}), 409

    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

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