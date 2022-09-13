"""This module includes schemas for base usage."""

from typing import Union

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    """Base model of base usage."""

    success: bool
    message: Union[str, None]
    data: Union[dict, None]
    subcode: Union[str, None]
