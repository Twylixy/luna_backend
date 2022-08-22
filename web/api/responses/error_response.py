from __future__ import annotations

from pydantic import BaseModel
from typing import Literal


class ErrorResponse(BaseModel):
    """Represents an error response."""

    status: Literal['failure']
    message: str
