from __future__ import annotations

from api.responses.base_response import BaseResponse


class DiscordAuthResponse(BaseResponse):
    """Represents discord auth response."""

    token: str
