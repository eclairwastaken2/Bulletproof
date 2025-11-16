from functools import wraps
from flask import request, jsonify, session
import jwt
import requests
import os

COGNITO_POOL_ID = os.getenv("COGNITO_POOL_ID")
COGNITO_REGION = os.getenv("COGNITO_POOL_REGION")
COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")

JWKS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_POOL_ID}/.well-known/jwks.json"
JWKS = requests.get(JWKS_URL).json()

def verify_cognito_jwt(token):
    unverified = jwt.get_unverified_header(token)
    key = next(k for k in JWKS['keys'] if k['kid'] == unverified['kid'])

    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

    return jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        audience=COGNITO_CLIENT_ID
    )

def cognito_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = session.get("user")
        if not user:
            return jsonify({"error": "unauthorized"}), 401

        request.user = user
        return fn(*args, **kwargs)
    return wrapper