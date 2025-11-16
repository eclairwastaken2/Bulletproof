from flask import Blueprint, jsonify, session

user_bp = Blueprint("user", __name__, url_prefix="/api")

@user_bp.get("/profile")
def profile():
    user = session.get("user")
    if not user:
        return jsonify({"error": "Not authenticated"}), 401
    return jsonify(user), 200