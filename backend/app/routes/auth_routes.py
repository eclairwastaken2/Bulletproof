from flask import Blueprint, redirect, session, url_for
from app.services.auth_service import oauth
from app.services.user_service import get_user_by_cognito_id, create_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.get("/login")
def login():
    redirect_uri = url_for("auth.authorize", _external=True)
    return oauth.cognito.authorize_redirect(redirect_uri)

@auth_bp.get("/authorize")
def authorize():
    print("COOKIES:", session)
    token = oauth.cognito.authorize_access_token()
    userinfo = token["userinfo"]

    session["user"] = userinfo
    cognito_id = userinfo["sub"]

    user = get_user_by_cognito_id(cognito_id)
    if not user:
        username = userinfo.get("preferred_username") or userinfo.get("email").split("@")[0]
        user = create_user(cognito_id, username, userinfo.get("email"))
    return redirect(f"http://localhost:5173/{user['username']}")

@auth_bp.get("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")