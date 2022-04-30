import logging
from os import environ

from discord import Message
from discord.ext.commands import Bot

luna_instance = Bot(
    command_prefix=environ.get('BOT_COMMAND_PREFIX', '-'),
    case_insensitive=environ.get('BOT_CASE_INSENSITIVE', False),
    owner_id=environ.get('BOT_OWNER_ID', None),
    strip_after_prefix=environ.get('BOT_STRIP_AFTER_PREFIX', True),
)


@luna_instance.event
async def on_ready() -> None:
    """Callback when bot is ready"""
    logging.warning('The bot is ready [{0.user}]'.format(luna_instance))


@luna_instance.event
async def on_message(message: Message) -> None:
    """Handler for new messages"""
    ctx = await luna_instance.get_context(message)
