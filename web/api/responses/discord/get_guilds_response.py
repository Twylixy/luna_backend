from __future__ import annotations

from typing import List

from api.entities.discord import DiscordServer
from api.responses.base_response import BaseResponse


class GetGuildsResponse(BaseResponse):
    """Represents discord auth response."""

    guilds: List[DiscordServer]
