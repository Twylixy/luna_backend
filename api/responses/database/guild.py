from api.entities.database import DatabaseGuild
from api.responses.base import BaseResponse


class GetDatabaseGuildResponse(BaseResponse):
    """Represents get guild response."""

    guild: DatabaseGuild


class CreateDatabaseGuildResponse(BaseResponse):
    """Represents create guild response."""

    guild: DatabaseGuild


class UpdateDatabaseGuildResponse(BaseResponse):
    """Represents update guild response."""

    guild: DatabaseGuild


class DeleteDatabaseGuildResponse(BaseResponse):
    """Represents delete guild response."""
