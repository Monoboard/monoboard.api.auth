"""This module include functionality to work with user microservice."""

from http import HTTPStatus

from schemas.user import UserSchema
from repositories.base import BaseRepository
from settings import INTERNAL_CONFIGS
from exceptions import APIError


class UserRepository(BaseRepository):
    """Class that includes http requests to user microservice."""

    api_name = "monoboard.api.user"
    api_config = INTERNAL_CONFIGS[api_name]

    api_url = "http://{host}:{port}".format(
        host=api_config["api_host"], port=api_config["api_port"]
    )
    api_version = "v1"
    api_key = api_config["api_key"]

    api_user_path = "user/"

    @classmethod
    async def get_user(cls, field: str, value: str):
        """Request user by monobank_token."""
        request_url = cls.format_url(cls.api_user_path)
        request_headers = cls.format_headers()
        response, response_status = await cls.get(
            request_url, request_headers, params={"field": field, "value": value}
        )

        if response_status != HTTPStatus.OK:
            raise APIError(
                status_code=response_status,
                message=response.message,
                subcode=response.subcode,
                data=response.data,
            )

        return UserSchema(**response.data)
