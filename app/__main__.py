import logging
from os import environ

from .entrypoints import luna_instance

logging.basicConfig(
    level=environ.get('DEBUG_LEVEL', 'INFO'),
    format=environ.get(
        'DEBUG_FORMAT',
        '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    ),
    datefmt=environ.get('DEBUG_DATEFMT', '%H:%M:%S'),
)

luna_instance.run(environ.get("BOT_TOKEN"))
