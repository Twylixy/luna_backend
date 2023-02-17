from pydantic import BaseModel

from api.entities.database import DatabaseUser


class CreateDatabaseUserRequest(BaseModel):
    """Represents create user request."""

    discord_id: int
    email: str


class UpdateDatabaseUserRequest(BaseModel):
    """Represents update user request."""

    email: str
