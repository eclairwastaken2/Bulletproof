from .user_routes import auth_bp
from .journal_routes import journal_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(journal_bp)