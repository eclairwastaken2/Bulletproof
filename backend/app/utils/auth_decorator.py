from functools import wraps
from flask import request, jsonify
import os, jwt
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGO = "HS256"

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error":"missing token"}), 401
        token = auth_header.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
            request.user_id = payload.get("user_id")
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"token expired"}), 401
        except Exception:
            return jsonify({"error":"invalid token"}), 401
        return f(*args, **kwargs)
    return wrapper