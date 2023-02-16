from api.entities.database import DatabaseDiscordGuild
from api.responses.base import BaseResponse


class GetDatabaseGuildResponse(BaseResponse):
    """Represents get guild response."""

    guild: DatabaseDiscordGuild


class CreateDatabaseGuildResponse(BaseResponse):
    """Represents create guild response."""

    guild: DatabaseDiscordGuild


class UpdateDatabaseGuildResponse(BaseResponse):
    """Represents update guild response."""

    guild: DatabaseDiscordGuild


class DeleteDatabaseGuildResponse(BaseResponse):
    """Represents delete guild response."""
