from __future__ import annotations

from typing import List

from api.entities.discord import DiscordGuild
from api.responses.base import BaseResponse


class GetGuildsResponse(BaseResponse):
    """Represents discord auth response."""

    guilds: List[DiscordGuild]
