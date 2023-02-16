from pydantic import BaseModel

from api.entities.database import DatabaseDiscordGuild


class CreateDatabaseGuildRequest(BaseModel):
    """Represents create guild request."""

    guild_id: int


class UpdateDatabaseGuildRequest(BaseModel):
    """Represents update guild request."""

    guild: DatabaseDiscordGuild


class DeleteDatabaseGuildRequest(BaseModel):
    """Represents delete guild request."""

    guild_id: int
