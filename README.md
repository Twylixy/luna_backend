# @luna_bot (Backend)
The Discord bot for [AltMoon Discord Server](https://discord.gg/8rNYvSnR7c)

## Requirements
* Docker
* Docker-Compose 
* Poetry 1.2.0+ (Optional)

## Prepare
Clone repository
```bash
$ git clone https://github.com/Twylixy/luna_backend.git
```
(Optional) Install Poetry.
Read about installing [here](https://python-poetry.org/docs/#installation)
Recommended for future development, but not needed for deploy.

Configure **.env.example** and save as **.env.dev** or **.env.production** depending on deploy scope. \
**Note:** Detailed information about **.env** configurations provided in **ENVFILES.md** file.

## Deploy
### Develop
```bash
# you don't need to use "-p", but it migth me helpful
$ docker-compose -f docker-compose.dev.yml -p "luna" up --build -d
```

### Production
In production backend will set up it's own **NGINX** web server. You can set-up which one it should use: `HTTP` (only) or both `HTTP` and `HTTPS`. For second you need to provide SSL cert and key into `./ssl` folder with following name: `cert.crt` - for certificate and `private.key` for key. 

**IMPORTANT**: By default backend is configured to work with `HTTP` protocol only. If you need to use `HTTP` and `HTTPS` or only `HTTPS` you have to slightly edit **nginx.conf**.

### Run behind NGINX (HTTP) (Recommended).
So, for `HTTP` it's quite simple:
```bash
# use pre-build images from Docker Hub
$ docker compose -f docker-compose.prod.yml -p "luna" up -d

# or build them by yourself
$ docker compose -f docker-compose.prod.yml -p "luna" up --build -d
```
**IMPORTANT:** in `docker-compose.prod.yml` you can see port setup for **NGINX** like that: `- 127.0.0.1:7080:80`. The `127.0.0.0.1` will force container to listen connections only from localhost, so you can't access it from outside.

### Run without NGINX or HTTP or HTTPS or both
Otherwise, you can use `HTTPS`, then you have to edit `docker-compose.prod.yml` file. Just uncomment the line with port `7443`, or if you want to use only `HTTPS` you have to comment line with port `7080`. **DO NOT FORGET TO PLACE SSL FILES TO ./ssl folder**
```yaml
nginx:
  ...
  ports:
    - 127.0.0.1:7080:80 # in case to use HTTPS change it to 7080:80 (or any other port you wan't on left side) or just comment
    # - 7443:443 # Uncomment this line if you want to use HTTPS
```
Then, you have to edit `nginx.conf` file. Uncomment the whole configuration block for `HTTPS` and comment configuration on top.
```nginx
#
# Uncomment this code and comment the code above if you need to enable HTTPS
#

# server {
#     listen ${SERVER_LISTEN_HTTP_PORT} default_server;
#     server_name ${SERVER_NAME};
#     ...
```
Also if you use only HTTPS, just uncomment the `server` directive with `listen 443 ssl;` and comment the `server` directive with `listen 80;` directive. \
**NOTE:** to make service accessible from outside, then remove `127.0.0.1` rule for ports for **NGINX**. \
**IMPORTANT:** do not use backend without **NGINX** for public.


## Develop on Windows
Before run the project make sure, that you've added environment variables. \
To add environment variables use that instructions:
* Execute `poetry install` (if you didn't do that before)
* Open `PROJECT_HOME\.venv\Scripts\activate.ps1`
* Add all required variables from `.env(.prod|.dev)` file. Example `$env:VAR_NAME=VALUE` 

## Debug (only for develop)
For debug use develop version of project, then you've to setup vscode debugger for python with this configuration.
Place it in `~/.vscode/launch.json`
Port may be changed, but don't forget to change it in `docker-compose.dev.yml` in `api` service. Or assign your own.
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI (remote)",
      "type": "python",
      "request": "attach",
      "port": 5678,
      "host": "localhost",
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "/usr/src/luna_api"
        }
      ]
    }
  ]
}
```