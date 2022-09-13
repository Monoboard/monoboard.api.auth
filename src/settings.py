"""This module provides config variables for app."""

import os

# App stuff
APP_NAME = "monoboard.api.auth"
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

# API keys
INTERNAL_API_KEYS = {
    "monoboard.api.user": os.getenv("AUTH_USER_API_KEY")
}
