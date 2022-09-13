"""This module includes custom errors."""


class BaseError(Exception):
    """Class that represents base error."""

    def __init__(self, message: str = None):
        """Initialize base custom error."""
        super().__init__()
        self.message = message

    def __str__(self):
        """Return message for str method."""
        return f"{self.__class__.__name__}: {self.message}"

    def __repr__(self):
        """Return message for repr method."""
        return f"{self.__class__.__name__}: {self.message}"


class TokenError(BaseError):
    """Class that represents errors caused on interaction with auth token."""


class RetryError(BaseError):
    """Class that represents errors caused for retry."""
