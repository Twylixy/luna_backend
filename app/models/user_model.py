from datetime import datetime

import peewee

from .base_model import BaseModel


class UserModel(BaseModel):
    """Represents a user model"""

    discord_id = peewee.BigIntegerField(null=False, unique=True)

    class Meta:
        db_table = 'users'
