from pydantic import BaseModel


class DatabaseDiscordGuild(BaseModel):
    """Represents discord guild."""

    id: int
    guild_id: int
    settings_id: int
