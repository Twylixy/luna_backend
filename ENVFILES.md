# Env configuration (Develop branch)
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types available values is `0` and `1`

## Debug
Configurations for **python logging**\
You can leave them empty.
```
DEBUG_LEVEL - Debug level (string or int)
DEBUG_FORMAT - Debug log format (string)
DEBUG_DATEFMT - Debug date format (string)
```

## Bot
Configurations for **discord bot**\
The following variables aren't required:
BOT_COMMAND_PREFIX, BOT_CASE_INSENSITIVE, BOT_OWNER_ID, BOT_STRIP_AFTER_PREFIX
```
BOT_TOKEN - Discord bot token
BOT_COMMAND_PREFIX - Bot prefix
BOT_CASE_INSENSITIVE - Bot's commands insensivity (bool)
BOT_OWNER_ID - Bot's owner id (int)
BOT_STRIP_AFTER_PREFIX - Bot's strip after prefix (! command -> !command) (booL)
```

## Database
Database configurations for bot.
```
DATABASE_TYPE - Database type (mysql or postgres or sqlite)
DATABASE_HOST - Database host
DATABASE_PORT - Database port 
DATABASE_USER - Database user
DATABASE_PASSWORD - Database user's password
DATABASE_NAME - Database name (for sqlite - filename, can be empty)
DATABASE_CHARSET - Database charset (for mysql, can be empty)
```

## Docker Database
Those variables are required for Docker Compose.\
If you set up with postgres use **POSTGRES** section of configuration, either if you have mysql use **MYSQL** configuration instead. **All of those variables required to be set.**