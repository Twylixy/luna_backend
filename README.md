# @luna_bot
The Discord bot for Dusked Ocean Discord Server ([link](https://discord.gg/8rNYvSnR7c))

## Requirements
* Debian/Ubuntu
* Docker
* Docker-compose
* Poetry (Optional)

## Prepare
Clone repository
```bash
$ git clone https://github.com/Twylixy/luna_bot.git
```
(Optional) Install Poetry.
```bash
$ python3 -m pip install poetry
```
Configure **.env.dev.example** (or **.env.prod.example**) and remove **.example** tail.
Detailed information about **.env** configurations is [here](https://github.com/Twylixy/luna_bot/blob/develop/ENVFILES.md)

## Deploy
**Note:** argument *-p* isn't required
### Develope
```bash
$ docker-compose -f docker-compose.dev.yml -p "luna" up --build -d
```
### Production
```bash
$ docker-compose -f docker-compose.prod.yml -p "luna" up --build -d
```

## Develop on Windows
Before run the project make sure, that you've added environment variables to the project environment. \
To add environment variables use that instructions:
* Execute `poetry install` (if you didn't do that before)
* Open `PROJECT_HOME\.venv\Scripts\activate.ps1`
* Add all required variables from `.env(.prod|.dev)` file. Example `$env:VAR_NAME=VALUE` 
