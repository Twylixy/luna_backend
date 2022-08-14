from __future__ import annotations

from api.responses.base_response import BaseResponse
from drf_yasg.openapi import Response, Schema


class ErrorResponse(BaseResponse):
    """Represents an error response."""

    message: str

    @classmethod
    def get_response_schema(cls: ErrorResponse) -> Response:
        """
        Return schema of response.

        Returns:
            Response
        """
        return Response(
            description='Error response',
            schema=Schema(**cls.schema()),
            examples={
                'application/json': {
                    'code': 'somecode',
                    'redirect_uri': 'https://example.com/',
                },
            },
        )
