from os import environ

import peewee

from app.helpers import UnsupportedDatabaseError


class BaseModel(peewee.Model):
    """Represents base model"""

    class Meta:
        """Represents meta information"""

        database = peewee.PostgresqlDatabase(
            host=environ.get('BOT_DATABASE_HOST', 'localhost'),
            port=environ.get('BOT_DATABASE_PORT', 5432),
            user=environ.get('BOT_DATABASE_USER', 'postgres'),
            password=environ.get('BOT_DATABASE_PASSWORD', 'postgres'),
            database=environ.get('BOT_DATABASE_NAME', 'postgres'),
        )
