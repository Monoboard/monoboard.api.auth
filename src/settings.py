"""This module provides config variables for app."""

import os

# App stuff
APP_NAME = "monoboard.api.auth"
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

# JWT Stuff
ACCESS_JWT_EXP_DAYS = int(os.getenv("ACCESS_JWT_EXP_DAYS", "7"))
REFRESH_JWT_EXP_DAYS = int(os.getenv("REFRESH_JWT_EXP_DAYS", "30"))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# API keys
INTERNAL_CONFIGS = {
    "monoboard.api.user": {
        "api_key": os.getenv("AUTH_USER_API_KEY"),
        "api_host": os.getenv("MONOBOARD_API_USER_HOST"),
        "api_port": os.getenv("MONOBOARD_API_USER_PORT"),
    }
}
