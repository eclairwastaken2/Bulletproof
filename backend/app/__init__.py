from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.auth import auth
    from app.routes.journal import journal
    from app.routes.users import users

    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(journal, url_prefix="/api")
    app.register_blueprint(users, url_prefix="/api")

    @app.route("/api/health")
    def health():
        return {"status":"ok"}

    return app