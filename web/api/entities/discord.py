from pydantic import BaseModel


class OAuth2Credentials(BaseModel):
    """Represents oauth2 credentials."""

    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str


class DiscordUser(BaseModel):
    """Represents discord user."""

    id: int
    username: str
    email: str


class DiscordServer(BaseModel):
    """Represents Discord server."""

    id: int
    name: str
    icon: str
    permissions: int
