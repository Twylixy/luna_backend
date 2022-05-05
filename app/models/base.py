from os import environ

import peewee

from app.helpers import UnsupportedDatabaseError


class BaseModel(peewee.Model):
    """Represents base model"""

    class Meta:
        """Represents meta information"""

        database_type = environ.get('BOT_DATABASE_TYPE', 'sqlite').lower()

        if database_type == 'postgresql':
            database = peewee.PostgresqlDatabase(
                host=environ.get('BOT_DATABASE_HOST', 'localhost'),
                port=environ.get('BOT_DATABASE_PORT'),
                user=environ.get('BOT_DATABASE_USER', 'root'),
                password=environ.get('BOT_DATABASE_PASSWORD', 'password'),
                database=environ.get('BOT_DATABASE_NAME', 'database'),
            )
        elif database_type == 'mysql':
            database = peewee.MySQLDatabase(
                host=environ.get('BOT_DATABASE_HOST', 'localhost'),
                port=environ.get('BOT_DATABASE_PORT'),
                user=environ.get('BOT_DATABASE_USER', 'root'),
                password=environ.get('BOT_DATABASE_PASSWORD', 'password'),
                database=environ.get('BOT_DATABASE_NAME', 'database'),
                charset=environ.get('BOT_DATABASE_CHARSET', 'utf8mb4'),
            )
        else:
            raise UnsupportedDatabaseError(
                'The database "{0}" is not supported'.format(database_type),
            )
