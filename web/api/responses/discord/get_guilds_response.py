from __future__ import annotations

from typing import List

from api.helpers.discord import DiscordServer
from api.responses.base_response import BaseResponse
from drf_yasg.openapi import Response, Schema


class GetGuildsResponse(BaseResponse):
    """Represents discord auth response."""

    guilds: List[DiscordServer]

    @classmethod
    def get_response_schema(cls: GetGuildsResponse) -> Response:
        """
        Return schema of response.

        Returns:
            Response
        """
        return Response(
            description='Success response',
            schema=Schema(**cls.schema()),
        )
