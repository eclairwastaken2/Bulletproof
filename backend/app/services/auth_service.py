from flask import Flask, redirect, url_for, session
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
import os

oauth = OAuth()

def init_oauth(app):
    oauth.init_app(app)

    oauth.register(
        name='cognito',
        server_metadata_url=(
            f"https://cognito-idp.{os.getenv('COGNITO_POOL_REGION')}.amazonaws.com/"
            f"{os.getenv('COGNITO_POOL_ID')}/.well-known/openid-configuration"
        ),
        client_id=os.getenv("COGNITO_CLIENT_ID"),
        client_secret=os.getenv("COGNITO_CLIENT_SECRET"),
        client_kwargs={"scope": "openid email"},
    )

    return oauth
