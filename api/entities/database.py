from pydantic import BaseModel


class DatabaseGuild(BaseModel):
    """Represents discord guild."""

    id: int
    guild_id: int
    settings_id: int


class DatabaseUser(BaseModel):
    """Represents discord user."""

    id: int
    discord_id: int
    email: str
