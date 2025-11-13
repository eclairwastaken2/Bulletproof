from app.models.user import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def register_user(data): 
    if User.objects(email=data["email"]).first():
        raise ValueError("Email already registered")
    
    user = User(email=data["email"], name=data.get("name"))
    user.set_password(data["password"])
    user.save()

    return user.to_dict()

def login_user(data): 
    user = User.objects(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        raise ValueError("Invalid email or password")
    
    token = create_access_token(identity=str(user.id))
    return {"access_token": token}

def get_profile(user_id): 
    user = User.objects(id=user_id).first()
    return user