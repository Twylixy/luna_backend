# Env configuration
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types available values is `0` and `1`
**Note 2:** for `array[<type>]` set variables like: VAR=some some2 ...

## Docker Settings
Variables for Docker Compose.\

### Database
Variables for Docker's database container \
**POSTGRES_PASSWORD** required
```
POSTGRES_USER - Database user (string)
POSTGRES_PASSWORD - User's password (string)
POSTGRES_DB - Database name (string)
```

### Nginx
Variables for Docker's Nginx container
```
SERVER_NAME - server_name derective (string) 
SERVER_LISTEN_HTTP_PORT - listening http port (string)
SERVER_LISTEN_HTTPS_PORT - listening http**s** port (string)
HTTPS_PROXY_PASS_PORT - specifies proxy pass port to https (string with ':', ex HTTPS_PROXY_PASS_PORT=:7443)
API_HOST=api:8000 - api host for upstream derective (string)
```
**Note**: `HTTPS_PROXY_PASS_PORT` is the variable that is required if you don't use Proxy services, like Cloudflare, otherwise you must leave this value blank or `proxy_pass` will not work at all.

---
<br>

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