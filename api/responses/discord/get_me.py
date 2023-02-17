from api.entities.discord import DiscordUser
from api.responses.base import BaseResponse


class GetMeResponse(BaseResponse):
    """Return Discord user."""

    user: DiscordUser
