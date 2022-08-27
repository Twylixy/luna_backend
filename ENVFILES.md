Env configuration
---
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types valid values is `0` and `1` \
**Note 2:** for `array[<type>]` set variables like: VAR=some some2 ... \

# Docker Settings
Variables for Docker Compose.

## Database
Variables for Docker's database container

`POSTGRES_USER` \
**Type**: *string* \
**Required**: *False* \
Docker's PostgreSQL container database user.

`POSTGRES_PASSWORD` \
**Type**: *string* \
**Required**: *True* \
Docker's PostgreSQL container database password.

`POSTGRES_DB` \
**Type**: *string* \
**required**: *False* \
Docker's PostgreSQL container database name. 

## Nginx
Variables for Docker's Nginx container

`SERVER_NAME` \
**Type**: *string* \
**Required**: *True* \
Value for **server_name** derective in **nginx.conf**

`SERVER_LISTEN_HTTP_PORT` \
**Type**: *integer* \
**Required**: *True* \
Port for HTTP **listen** derective in **nginx.conf**

`SERVER_LISTEN_HTTPS_PORT` \
**Type**: *integer* \
**Required**: *True* \
Port for HTTPS **listen** derective in **nginx.conf**

`HTTPS_PROXY_PASS_PORT` \
**Type**: *string* \
**Required**: *False* \
**Exapmle**: *HTTPS_PROXY_PASS_PORT=:7443* \
Port for redirect from HTTP to HTTPS, if you don't have to define port, for example you're using proxy server (Cloudflare or simillar), then you can leave it empty, otherwise, specify port with **:** 

`API_HOST` \
**Type**: *string* \
**Required**: *True* \
**Exapmle**: *API_HOST=api:8000* \
Host of api. In example defined api container (by its name) and port, that Uvicorn is listening

`FRONTEND_HOST` \
**Type**: *string* \
**Required**: *True* \
**Exapmle**: *FRONTEND_HOST=frontend:3000* \
Host of frontend. In example defined frontend container (by its name) and port, that Nuxt is listening

`CORS_ALLOWED_ORIGINS` \
**Type**: *array[string]* \
**Required**: *False* \
**Exapmle**: *CORS_ALLOWED_ORIGINS=https://localhost:7443 https://localhost:3000 http://localhost:7080 http://localhost:3000* \
Allowed domains, that can read and request to api from browser \
**Note**: CORS settings required only if you've different origins. For example, you've run frontend at example.com and backend on api.example.com, you are need to set CORS_ALLOWED_ORIGINS=*.example.com, otherwise leave it the same

`CORS_ALLOWED_METHODS` \
**Type**: *array[string]* \
**Required**: *False* \
**Exapmle**: *CORS_ALLOWED_METHODS=GET, POST, OPTIONS, PUT, DELETE* \
Methods, that allowed for CORS requests

---
<br>

# FastAPI Settings
The following variables sets up Django

## Database
Variables for Django database connection

`POSTGRES_HOST` \
**Type**: *string* \
**Required**: *True* \
Database host

`POSTGRES_PORT` \
**Type**: *integer* \
**Required**: *False* \
Database port

## API
Variables for project's API

`DISCORD_ENDPOINT` \
**Type**: *string* \
**Required**: *False* \
Discord API endpoint

`CLIENT_ID` \
**Type**: *integer* \
**Required**: *True* \
Discord API client ID

`CLIENT_SECRET` \
**Type**: *string* \
**Required**: *True* \
Discord API client secret

`TOKEN_LENGTH` \
**Type**: *int* \
**Required**: *False* \
Token length
