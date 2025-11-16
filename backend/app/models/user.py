from flask import current_app
from app.extensions import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
import datetime

def get_db():
    return mongo.db

def create_user(email, password, username=""):
    db = get_db()
    hashed = generate_password_hash(password)
    user = {
        "email": email,
        "password": hashed,
        "username": username,
        "created_at": datetime.datetime.utcnow()
    }
    db.users.insert_one(user)
    user["_id"] = str(user["_id"])
    return user

def find_user_by_email(email):
    db = get_db()
    user = db.users.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])
    return user

def find_user_by_id(user_id):
    db = get_db()
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
    return user

def check_user_password(user, raw_password):
    return check_password_hash(user["password"], raw_password)