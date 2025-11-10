from flask import Blueprint, jsonify
from app.extensions import get_db

users = Blueprint("users", __name__)

@users.route("/users/<username>", methods=["GET"])
def get_user(username):
    db = get_db()
    u = db.users.find_one({"username": username}, {"password": 0})
    if not u:
        return jsonify({"error": "not found"}), 404
    return jsonify({"username": u["username"], "id": str(u["_id"])})