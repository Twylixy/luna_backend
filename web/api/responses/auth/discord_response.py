from __future__ import annotations

from api.responses.base_response import BaseResponse
from drf_yasg.openapi import Response, Schema


class DiscordAuthResponse(BaseResponse):
    """Represents discord auth response."""

    token: str

    @classmethod
    def get_response_schema(cls: DiscordAuthResponse) -> Response:
        """
        Return schema of response.

        Returns:
            Response
        """
        return Response(
            description='Success response',
            schema=Schema(**cls.schema()),
            examples={
                'application/json': {
                    'code': 'test',
                    'redirect_uri': 'https://example.com/',
                },
            },
        )
