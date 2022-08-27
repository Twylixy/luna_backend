from typing import Literal

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Represents an error response."""

    status: Literal['failure']
    message: str
