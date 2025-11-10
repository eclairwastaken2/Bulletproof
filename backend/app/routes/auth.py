from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import get_db
import os, jwt, datetime

auth = Blueprint("auth", __name__)

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGO = "HS256"

@auth.route("/register", methods=["POST"])
def register():
    db = get_db()
    body = request.json or {}
    username = body.get("username")
    email = body.get("email")
    password = body.get("password")
    if not username or not password:
        return jsonify({"error":"username and password required"}), 400
    if db.users.find_one({"$or":[{"username":username},{"email":email}] }):
        return jsonify({"error":"user already exists"}), 409
    pw_hash = generate_password_hash(password) 
    user = {
        "username": username,
        "email": email,
        "password": pw_hash,
        "created_at": datetime.datetime.utcnow()
    }
    res = db.users.insert_one(user)
    user_id = str(res.inserted_id)
    token = jwt.encode({"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)}, JWT_SECRET, algorithm=JWT_ALGO)
    return jsonify({"token": token, "username": username}), 201

@auth.route("/login", methods=["POST"])
def login():
    db = get_db()
    body = request.json or {}
    username_or_email = body.get("username") or body.get("email")
    password = body.get("password")
    if not username_or_email or not password:
        return jsonify({"error":"username/email and password required"}), 400
    user = db.users.find_one({"$or":[{"username":username_or_email},{"email":username_or_email}]})
    if not user:
        return jsonify({"error":"invalid credentials"}), 401
    if not check_password_hash(user["password"], password):
        return jsonify({"error":"invalid credentials"}), 401
    user_id = str(user["_id"])
    token = jwt.encode({"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)}, JWT_SECRET, algorithm=JWT_ALGO)
    return jsonify({"token": token, "username": user["username"]})