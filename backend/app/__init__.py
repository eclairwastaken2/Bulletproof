from flask import Flask
from flask_cors import CORS
from app.extensions import mongo, jwt
from app.services.auth_service import init_oauth
from app.routes import register_blueprints
from app.config import DevConfig
import os

def create_app():
    app = Flask(__name__)
    app.secret_key =os.getenv("SECRET_KEY")
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
    app.config['SESSION_COOKIE_SAMESITE'] = "Lax"  
    app.config['SESSION_COOKIE_SECURE'] = False 
    init_oauth(app) 
    app.config.from_object(DevConfig)

    mongo.init_app(app)
    jwt.init_app(app)

    register_blueprints(app)
    return app