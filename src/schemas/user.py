"""This module includes schemas for user."""

import uuid
import datetime
from typing import Union

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """Base model of user entity."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    first_name: Union[str, None]
    last_name: Union[str, None]
    created_date: datetime.datetime


class UserIDSchema(BaseModel):
    """Base model of user id schema."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
