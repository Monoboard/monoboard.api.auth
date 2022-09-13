"""This module includes api endpoints for auth."""


from fastapi import APIRouter, status

from repositories.user import UserRepository
from schemas.base import ResponseSchema
from schemas.auth import LoginRequestSchema, LoginResponseSchema
from utils.response import make_response
from utils.token import generate_token
from exceptions import APIError
from settings import JWT_SECRET_KEY, ACCESS_JWT_EXP_DAYS, REFRESH_JWT_EXP_DAYS


router = APIRouter()


@router.post(
    "/login",
    response_model=LoginResponseSchema,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": ResponseSchema, "description": "User not found"},
        422: {"model": ResponseSchema, "description": "Validation error"},
        500: {"model": ResponseSchema, "description": "Internal Error"},
    },
)
def login(user_input: LoginRequestSchema):
    """Login a user if the supplied credentials are correct."""
    try:
        user = UserRepository.get_user_by_monobank_token(user_input.monobank_token)
    except APIError as exc:
        return make_response(
            success=False,
            http_status=exc.status_code,
            subcode=exc.subcode,
            message=exc.message,
        )

    token, token_exp = generate_token(
        secret_key=JWT_SECRET_KEY, private_claims={"user_id": str(user.id)}, exp_days=ACCESS_JWT_EXP_DAYS
    )
    refresh_token, refresh_token_exp = generate_token(
        secret_key=JWT_SECRET_KEY, private_claims={"user_id": str(user.id)}, exp_days=REFRESH_JWT_EXP_DAYS
    )

    response_data = {
        "access_token": token,
        "access_token_exp": token_exp,
        "refresh_access_token": refresh_token,
        "refresh_access_token_exp": refresh_token_exp,
    }
    return LoginResponseSchema(
        success=True,
        message="User was successfully authorized",
        data=response_data,
    )
