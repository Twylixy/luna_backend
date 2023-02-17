from api.responses.base import BaseResponse


class DiscordAuthResponse(BaseResponse):
    """Represents success discord authentication response."""

    token: str
