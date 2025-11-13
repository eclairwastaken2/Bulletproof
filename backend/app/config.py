import os
from datetime import timedelta

class Config:
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    MONGODB_SETTINGS = {
        "MONGO_URI": os.getenv("MONGO_URI", "mongodb://mongo:27017"),
        "DB_NAME": os.getenv("DB_NAME"),
    }

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False