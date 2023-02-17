from typing import Literal

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """Represents base response."""

    status: Literal['success']
