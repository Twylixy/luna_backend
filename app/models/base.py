from os import environ

import peewee

from app.helpers import UnsupportedDatabaseError


class BaseModel(peewee.Model):
    """Represents base model"""

    class Meta:
        """Represents meta information"""

        database_type = environ.get('DATABASE_TYPE', 'sqlite').lower()

        if database_type == 'sqlite':
            database = peewee.SqliteDatabase(
                database=environ.get('DATABASE_NAME', 'database'),
            )
        elif database_type == 'postgresql':
            database = peewee.PostgresqlDatabase(
                host=environ.get('DATABASE_HOST', 'localhost'),
                port=environ.get('DATABASE_PORT'),
                user=environ.get('DATABASE_USER', 'root'),
                password=environ.get('DATABASE_PASSWORD', 'password'),
                database=environ.get('DATABASE_NAME', 'database'),
            )
        elif database_type == 'mysql':
            database = peewee.MySQLDatabase(
                host=environ.get('DATABASE_HOST', 'localhost'),
                port=environ.get('DATABASE_PORT'),
                user=environ.get('DATABASE_USER', 'root'),
                password=environ.get('DATABASE_PASSWORD', 'password'),
                database=environ.get('DATABASE_NAME', 'database'),
                charset=environ.get('DATABASE_CHARSET', 'utf8mb4'),
            )
        else:
            raise UnsupportedDatabaseError(
                'The database "{0}" is not supported'.format(database_type),
            )
