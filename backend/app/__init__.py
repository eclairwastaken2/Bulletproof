from flask import Flask
from flask_cors import CORS
from .extensions import mongo
from .auth_routes import auth_bp

def create_app(config_object="app.config.DevConfig"):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_object)

    mongo.init_app(app)
    

    @app.route("/api/health")
    def health():
        return {"status":"ok"}

    return app