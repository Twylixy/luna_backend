from pydantic import BaseModel

from api.entities.database import DatabaseGuild


class CreateDatabaseGuildRequest(BaseModel):
    """Represents create guild request."""

    guild_id: int
