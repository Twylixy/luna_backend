from pydantic import BaseModel


class DiscordAuthRequest(BaseModel):
    """Represents discord auth request."""

    code: str
    redirect_uri: str
