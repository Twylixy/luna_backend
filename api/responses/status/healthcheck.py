from api.responses.base import BaseResponse


class HealthcheckResponse(BaseResponse):
    """Response for healthcheck request."""

    message: str
