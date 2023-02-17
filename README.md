# @luna_bot (Backend)
The Discord bot for [Dusked Ocean Discord Server](https://discord.gg/8rNYvSnR7c)

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

Configure **.env.example** and save as **.env.dev** or **.env.production**.
**Note:** Detailed information about **.env** configurations provided in **ENVFILES.md**

---
</br>

## Deploy
### Develope
```bash
$ docker-compose -f docker-compose.dev.yml -p "luna" up --build -d
```

### Production
In production backend will set up it's own nginx web server. You can specify which one it should use: http (only) or http (https). For second you need to provide ssl cert and key into `./ssl` folder with following name: `cert.crt` - for certificate and `private.key` for key. Also you can edit nginx's config in those files: `./docker/nginx/nginx.http.conf` (for http only) and `./docker/nginx/nginx.https.conf` (for both protocols).

Then you can run in production:
```bash
# you can pull build images from hub.docker.com (http only)
$ docker-compose -f docker-compose.http.prod.yml -p "luna" pull
# you can pull built images from hub.docker.com (http & https)
$ docker-compose -f docker-compose.https.prod.yml -p "luna" pull

# or you can build them by yourself (http)
$ docker-compose -f docker-compose.http.prod.yml -p "luna" build
# or you can build them by yourself (http & https)
$ docker-compose -f docker-compose.http.prod.yml -p "luna" build

# and, finally, run (http)
$ docker-compose -f docker-compose.http.prod.yml -p "luna" up -d
# and, finally, run (http & https)
$ docker-compose -f docker-compose.https.prod.yml -p "luna" up -d
```

## Run behind nginx (production).
You can run backend behind your own nginx, just edit ports in docker-compose file.
```
nginx:
  ... 
  ports:
    - 127.0.0.1:7080:80
    - 127.0.0.1:7443:443
```
It will force container to listen connections from host machine only.

## Develop on Windows
Before run the project make sure, that you've added environment variables. \
To add environment variables use that instructions:
* Execute `poetry install` (if you didn't do that before)
* Open `PROJECT_HOME\.venv\Scripts\activate.ps1`
* Add all required variables from `.env(.prod|.dev)` file. Example `$env:VAR_NAME=VALUE` 

## Debug (only for develop)
For debug use dev version of project, then you've to setup vscode debugger for python with this configuration.
Place it in `~/.vscode/launch.json`
Port may be changed, but don't forget to change it in `docker-compose.dev.yml` in `api` service.
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