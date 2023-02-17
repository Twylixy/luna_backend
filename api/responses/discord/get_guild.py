from api.entities.discord import DiscordGuild
from api.responses.base import BaseResponse


class GetGuildResponse(BaseResponse):
    """Represents get guild response."""

    guild: DiscordGuild
