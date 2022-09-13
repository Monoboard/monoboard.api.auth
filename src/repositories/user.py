"""This module include functionality to work with user microservice."""


from schemas.user import UserSchema
from settings import INTERNAL_API_KEYS


class UserRepository:
    """Class that includes http requests to user microservice."""

    service_name = "monoboard.api.user"
    api_key = INTERNAL_API_KEYS[service_name]

    @classmethod
    def get_user_by_monobank_token(cls, monobank_token: str):
        """Request user by monobank_token."""
        from datetime import datetime

        return UserSchema(
            id="4473648b-ff6d-4199-ad09-d265c07bf022",
            first_name="test",
            last_name="test2",
            created_date=datetime.now().isoformat(),
        )
