"""This module includes api endpoints for auth."""


from fastapi import APIRouter, status

from repositories.user import UserRepository
from schemas.base import ResponseSchema
from schemas.auth import LoginRequestSchema, RefreshRequestSchema, TokensResponseSchema
from utils.response import make_response
from utils.token import generate_token, decode_token
from exceptions import APIError, TokenError
from settings import JWT_SECRET_KEY, ACCESS_JWT_EXP_DAYS, REFRESH_JWT_EXP_DAYS
from constants import (
    ID_KEY,
    REFRESH_ACCESS_TOKEN_EXP_KEY,
    REFRESH_ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_EXP_KEY,
    MONOBANK_TOKEN_KEY,
)

router = APIRouter()


@router.post(
    "/login",
    response_model=TokensResponseSchema,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": ResponseSchema, "description": "User not found"},
        422: {"model": ResponseSchema, "description": "Validation error"},
        500: {"model": ResponseSchema, "description": "Internal Error"},
    },
)
async def login(login_input: LoginRequestSchema):
    """Login a user if the supplied credentials are correct."""
    try:
        user = await UserRepository.get_user(MONOBANK_TOKEN_KEY, login_input.monobank_token)
    except APIError as exc:
        return make_response(
            success=False,
            http_status=exc.status_code,
            subcode=exc.subcode,
            message=exc.message,
            data=exc.data,
        )

    token, token_exp = generate_token(
        secret_key=JWT_SECRET_KEY,
        private_claims={ID_KEY: str(user.id)},
        exp_days=ACCESS_JWT_EXP_DAYS,
    )
    refresh_token, refresh_token_exp = generate_token(
        secret_key=JWT_SECRET_KEY,
        private_claims={ID_KEY: str(user.id)},
        exp_days=REFRESH_JWT_EXP_DAYS,
    )

    return TokensResponseSchema(
        success=True,
        message="User was successfully authorized",
        data={
            ACCESS_TOKEN_KEY: token,
            ACCESS_TOKEN_EXP_KEY: token_exp,
            REFRESH_ACCESS_TOKEN_KEY: refresh_token,
            REFRESH_ACCESS_TOKEN_EXP_KEY: refresh_token_exp,
        },
    )


@router.post(
    "/refresh",
    response_model=TokensResponseSchema,
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": ResponseSchema, "description": "Bad request"},
        422: {"model": ResponseSchema, "description": "Validation error"},
        500: {"model": ResponseSchema, "description": "Internal Error"},
    },
)
def refresh(refresh_input: RefreshRequestSchema):
    """Return refreshed access token for a user."""
    try:
        payload = decode_token(refresh_input.refresh_access_token, JWT_SECRET_KEY)
    except TokenError as exc:
        return make_response(
            success=False,
            http_status=status.HTTP_400_BAD_REQUEST,
            subcode=exc.subcode,
            message=exc.message,
        )

    user_id = payload[ID_KEY]
    token, token_exp = generate_token(
        secret_key=JWT_SECRET_KEY,
        private_claims={ID_KEY: str(user_id)},
        exp_days=ACCESS_JWT_EXP_DAYS,
    )
    refresh_token, refresh_token_exp = generate_token(
        secret_key=JWT_SECRET_KEY,
        private_claims={ID_KEY: str(user_id)},
        exp_days=REFRESH_JWT_EXP_DAYS,
    )

    return TokensResponseSchema(
        success=True,
        message="Token was successfully refreshed",
        data={
            ACCESS_TOKEN_KEY: token,
            ACCESS_TOKEN_EXP_KEY: token_exp,
            REFRESH_ACCESS_TOKEN_KEY: refresh_token,
            REFRESH_ACCESS_TOKEN_EXP_KEY: refresh_token_exp,
        },
    )
