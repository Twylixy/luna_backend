# @luna_bot (Backend)
The Discord bot for [Dusked Ocean Discord Server](https://discord.gg/8rNYvSnR7c)

## Requirements
* Docker
* Docker-Compose 
* Poetry 1.2.0 (Optional)

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
Before up the project in production, make sure that you've edit `./docker/nginx/nginx.conf` and provide ssl cert (`cert.crt`) and key (`private.key`) to `./ssl` folder.
```bash
$ docker-compose -f docker-compose.prod.yml -p "luna" pull
$ docker-compose -f docker-compose.prod.yml -p "luna" up -d
```

## Develop on Windows
Before run the project make sure, that you've added environment variables. \
To add environment variables use that instructions:
* Execute `poetry install` (if you didn't do that before)
* Open `PROJECT_HOME\.venv\Scripts\activate.ps1`
* Add all required variables from `.env(.prod|.dev)` file. Example `$env:VAR_NAME=VALUE` 

## Debug
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