# @luna_bot (Backend)
The Discord bot for [Dusked Ocean Discord Server](https://discord.gg/8rNYvSnR7c)

## Requirements
* Debian/Ubuntu
* Docker
* Docker-compose
* Poetry (Optional)

## Prepare
Clone repository
```bash
$ git clone https://github.com/Twylixy/luna_backend.git
```
(Optional) Install Poetry.
```bash
$ python3 -m pip install poetry
```
Configure **.env.example** and save as **.env.dev** or **.env.production**.
**Note:** Detailed information about **.env** configurations provided in **ENVFILES.md**

---
</br>

## Deploy
**Note:** argument *-p* isn't required
### Develope
```bash
$ docker-compose -f docker-compose.dev.yml -p "luna" up --build -d
```

### Production
Before up the project in production, make sure that you've edit `./docker/nginx/nginx.conf` by editing `server_name` and providing ssl cert and key to `./ssl` folder with required names.
```bash
$ docker-compose -f docker-compose.prod.yml -p "luna" up --build -d
```

## Develop on Windows
Before run the project make sure, that you've added environment variables. \
To add environment variables use that instructions:
* Execute `poetry install` (if you didn't do that before)
* Open `PROJECT_HOME\.venv\Scripts\activate.ps1`
* Add all required variables from `.env(.prod|.dev)` file. Example `$env:VAR_NAME=VALUE` 
