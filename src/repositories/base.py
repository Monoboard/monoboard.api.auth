"""This module includes base functionality to work with microservice."""


from abc import ABC
from urllib.parse import urlencode

import aiohttp

from schemas.base import ResponseSchema
from constants import X_AUTH_HEADER_KEY, X_FROM_NAME_HEADER_KEY
from settings import APP_NAME


class BaseRepository(ABC):
    """Class that includes http requests microservice."""

    api_name = None
    api_config = None

    api_url = None
    api_version = None
    api_key = None

    @classmethod
    def format_headers(cls):
        """Format headers for communications between microservices."""
        return {X_AUTH_HEADER_KEY: cls.api_key, X_FROM_NAME_HEADER_KEY: APP_NAME}

    @classmethod
    def format_url(cls, path):
        """Format request url for communications between microservices."""
        return f"{cls.api_url}/api/{cls.api_version}/{path}"

    @staticmethod
    async def get(url, headers=None, params=""):
        """Return response from async get http request in json format."""
        url = f"{url}?{urlencode(params)}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response_json = await response.json()
                return ResponseSchema(**response_json), response.status

    @staticmethod
    async def post(url, headers=None, body=None):
        """Return response from async post http request in json format."""
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=body) as response:
                response_json = await response.json()
                return ResponseSchema(**response_json), response.status
