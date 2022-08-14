from api.requests.base_request import BaseRequest


class DiscordAuthRequest(BaseRequest):
    """Represents discord auth request."""

    code: str
    redirect_uri: str
