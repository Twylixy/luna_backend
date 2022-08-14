from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """Represents a base response."""

    status: Literal['success', 'failure']
