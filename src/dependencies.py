"""This module includes dependencies."""

from fastapi import Header, status, HTTPException

from settings import INTERNAL_CONFIGS


def verify_api_key(
    x_auth: str = Header(description="API key"),
    x_from_name: str = Header(description="Name of services from where request is came"),
):
    """Check if user is logged in."""
    api_config = INTERNAL_CONFIGS.get(x_from_name)
    if not api_config:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="X-From-Name header is invalid"
        )

    if api_config["api_key"] != x_auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="X-Auth header is invalid"
        )
