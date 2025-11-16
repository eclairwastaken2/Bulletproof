from flask import Flask
from flask_cors import CORS
from app.extensions import mongo, jwt
from app.services.auth_service import init_oauth
from app.routes import register_blueprints
from app.config import DevConfig
import os


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevConfig)
    app.secret_key = os.getenv("SECRET_KEY") or "dev-secret"
    print("SECRET KEY:", os.getenv("SECRET_KEY"))

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)
    init_oauth(app)
    mongo.init_app(app)
    jwt.init_app(app)

    register_blueprints(app)
    return app