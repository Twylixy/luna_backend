from pydantic import BaseModel


class GetGuildRequest(BaseModel):
    """Represents get guild request."""

    guild_id: int
