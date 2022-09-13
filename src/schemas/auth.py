"""This module includes schemas for auth."""

import datetime

from pydantic import BaseModel, Field

from schemas.base import ResponseSchema


class TokensSchema(BaseModel):
    """Base model for tokens schema."""

    access_token: str
    access_token_exp: datetime.datetime
    refresh_access_token: str
    refresh_access_token_exp: datetime.datetime


class LoginRequestSchema(BaseModel):
    """Base model for login input."""

    monobank_token: str = Field(..., min_length=10)

    class Config:
        """Additional configuration for user login model."""

        anystr_strip_whitespace = True


class RefreshRequestSchema(BaseModel):
    """Base model for refresh input."""

    refresh_access_token: str = Field(..., min_length=10)


class TokenRequestSchema(BaseModel):
    """Base model for refresh input."""

    access_token: str = Field(..., min_length=10)


class TokensResponseSchema(ResponseSchema):
    """Base model for tokens response."""

    data: TokensSchema
