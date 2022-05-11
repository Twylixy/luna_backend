import peewee

from .base import BaseModel


class GuildModel(BaseModel):
    """Represents a guild model"""

    guild_id = peewee.BigIntegerField(null=False, unique=True)

    class Meta:
        db_table = 'guilds'