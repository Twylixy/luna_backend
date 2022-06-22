# Env configuration
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types available values is `0` and `1`
**Note 2:** for `array[<type>]` set variables like: VAR=some some2 ...

## Docker Settings
Those variables are required for Docker Compose.\
**All of those variables required to be set.**
---

## Django Settings
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