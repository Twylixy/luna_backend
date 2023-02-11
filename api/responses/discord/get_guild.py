from api.responses.base import BaseResponse
from api.entities.discord import DiscordGuild


class GetGuildResponse(BaseResponse):
    """Represents get guild response."""

    guild: DiscordGuild
