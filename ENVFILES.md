Env configuration
---
The **.env** configuration files for the project are separated into 2 files (develop and production). Following explanainsion will help you to configure project.

**Note:** for `bool` types valid values is `0` and `1` \
**Note 2:** for `array[<type>]` set variables like: VAR=some some2 ... \
**Note 3:** `Required` means that variable required to run backend.

# Docker Settings
Variables for Docker Compose.

## Database
Variables for database setup

`POSTGRES_USER` \
**Type**: *string* \
**Required**: *True* \
Docker's PostgreSQL container database user.

`POSTGRES_PASSWORD` \
**Type**: *string* \
**Required**: *True* \
Docker's PostgreSQL container database password.

`POSTGRES_DB` \
**Type**: *string* \
**required**: *True* \
Docker's PostgreSQL container database name. 

`POSTGRES_HOST` \
**Type**: *string* \
**Required**: *True* \
Database host

`POSTGRES_PORT` \
**Type**: *integer* \
**Required**: *True* \
Database port


## Nginx (Production Only)
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
**Required**: *True (if https)* \
Port for HTTPS **listen** derective in **nginx.conf**

`HTTPS_PROXY_PASS_PORT` \
**Type**: *string* \
**Required**: *True (if https)* \
**Exapmle**: *HTTPS_PROXY_PASS_PORT=:7443* \
Port for redirect from HTTP to HTTPS, if you don't have to define port, for example you're using proxy server (Cloudflare or simillar), then you can leave it empty, otherwise, specify port with **:** 
Why ":"? Because if you don't have domain you can use just ip and it will work!

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
**Required**: *True* \
**Exapmle**: *CORS_ALLOWED_ORIGINS=https://localhost:7443 https://localhost:3000 http://localhost:7080 http://localhost:3000* \
Allowed domains, that can read and request to api from browser \
**Note**: CORS settings required only if you've different origins. For example, you've run frontend at example.com and backend on api.example.com, you are need to set CORS_ALLOWED_ORIGINS=*.example.com, otherwise leave it the same

`CORS_ALLOWED_METHODS` \
**Type**: *array[string]* \
**Required**: *True* \
**Exapmle**: *CORS_ALLOWED_METHODS=GET, POST, OPTIONS, PUT, DELETE* \
Methods, that allowed for CORS requests

---
<br>

# FastAPI Settings
The following variables sets up Django
`LOGGING_LEVEL` \
**Type**: *int* \
**Required**: *False* \
**Exapmle**: *LOGGING_LEVEL=10* \
Debug mode for FastAPI

`DATABASE_API_KEY` \
**Type**: *string* \
**Required**: *True* \
**Exapmle**: *DATABASE_API_KEY=super-secret-key* \
API Key to provide bot access to database api section.

## Discord API
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

`SWAGGER_URL` \
**Type**: *string* \
**Required**: *False* \
Url for contacts in swagger docs

`SWAGGER_EMAIL` \
**Type**: *string* \
**Required**: *False* \
Email for contacts in swagger docs
