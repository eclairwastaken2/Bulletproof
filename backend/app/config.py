import os
from datetime import timedelta

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET", "dev-secret")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/bulletproof")
    MONGO_DBNAME = os.getenv("DB_NAME", "bulletproof")

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False