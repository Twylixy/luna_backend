from api.entities.database import DatabaseUser
from api.responses.base import BaseResponse


class GetDatabaseUserResponse(BaseResponse):
    """Represents a response for getting user from database."""

    user: DatabaseUser


class CreateDatabaseUserResponse(BaseResponse):
    """Represents a response for creating user in database."""

    user: DatabaseUser


class UpdateDatabaseUserResponse(BaseResponse):
    """Represents a response for updating user in database."""

    user: DatabaseUser


class DeleteDatabaseUserResponse(BaseResponse):
    """Represents a response for deleting user from database."""
