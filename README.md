# @luna_bot (Develop branch)
The Discord bot for Dusked Ocean Discord Server ([link](https://discord.gg/8rNYvSnR7c))

## Requirements
* Debian/Ubuntu (or container)
* Docker
* Docker-compose
* Poetry (Optional)

## Prepare
Clone repository
```bash
$ git clone https://github.com/Twylixy/luna_bot.git
```
(Optional) Install Poetry. Required for future dependencies updates.
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

## On dependencies updates
### Develope requirements.txt
```bash
$ poetry export --dev -f requirements.txt -o requirements.dev.txt
```
### Production requirements.txt
```bash
$ poetry export -f requirements.txt -o requirements.prod.txt
```

