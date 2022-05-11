# Env configuration (Develop branch)
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types available values is `0` and `1`
**Note 2:** for `array[<type>]` set variables like: VAR=some some2 ...

## # Bot Settings
### Debug
Configurations for **python logging**\
You can leave them empty.
```
BOT_DEBUG_LEVEL - Debug level (string or int)
BOT_DEBUG_FORMAT - Debug log format (string)
BOT_DEBUG_DATEFMT - Debug date format (string)
BOT_DEBUG_GUILDS_IDS - Guild ids for slash_commands (array[int])
```
### Bot
Configurations for **bot**\
There is only one required variable: BOT_TOKEN
```
BOT_TOKEN - Discord bot token (string)
BOT_COMMAND_PREFIX - Bot prefix (string)
BOT_CASE_INSENSITIVE - Bot's commands insensivity (bool)
BOT_OWNER_ID - Bot's owner id (int)
BOT_STRIP_AFTER_PREFIX - Bot's strip after prefix (! command -> !command) (bool)
```
### Database
Database configurations for bot.
```
DATABASE_HOST - Database host (string)
DATABASE_PORT - Database port (string)
DATABASE_USER - Database user (string)
DATABASE_PASSWORD - Database user's password (string)
DATABASE_NAME - Database name (string)
```
### Bot Modules
Configurations for bot's modules
```
MA_WORDS_COUNT - Words count for message analyzer (int)
MA_TEXT_LENGTH - Text length for message analyzer (int)
MA_USERS_BLACKLIST - Users blacklist for message analyzer (array[int])
```

## # Docker Settings
Those variables are required for Docker Compose.\
**All of those variables required to be set.**

## # Django Settings
The following variables sets up Django
```
DJANGO_SECRET_KEY - Secret key for django (string)
DJANGO_DEBUG - Debug mode (bool)
DJANGO_ALLOWED_HOSTS - Allowed hosts for django (array[string])
```
### Database
Variables for Django database connection
```
DJANGO_DATABASE_ENGINE - Database engine (string)
DJANGO_DATABASE_NAME - Database name (string)
DJANGO_DATABASE_USER - Database user (string)
DJANGO_DATABASE_PASSWORD - Database password (string)
DJANGO_DATABASE_HOST - Database host (string)
DJANGO_DATABASE_PORT - Database port (int)
```