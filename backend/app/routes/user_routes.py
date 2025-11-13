from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import register_user, login_user

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.post("/register")
def register():
    try: 
        data = request.get_json()
        user = register_user(data)
        return jsonify({"user": user}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_bp.post("/login")
def login():
    try: 
        data = request.get_json()
        token = login_user(data)
        return jsonify(token), 200
    except Exception as e: 
        return jsonify({"error": str(e)}), 401
    
@user_bp.post("/profile")
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = user_service.get_profile(user_id)
    if not user: 
        return jsonify({"error": "User not Found"}), 404
    return jsonify(user.to_dict()), 200
