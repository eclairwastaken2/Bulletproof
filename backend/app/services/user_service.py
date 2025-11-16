from app.extensions import mongo
from bson import ObjectId
import datetime

def get_user_by_cognito_id(cognito_id):
    return mongo.db.users.find_one({"cognito_id": cognito_id})

def create_user(cognito_id, username, email):
    user = {
        "cognito_id": cognito_id, 
        "username": username, 
        "email": email, 
        "created_at": datetime.datetime.utcnow(), 
        "profile": {}
    }

    mongo.db.users.insert_one(user)
    return user