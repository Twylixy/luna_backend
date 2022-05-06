import logging
from os import environ

import discord
from discord.ext import commands

from app.models import UserModel

intents = discord.Intents(messages=True, message_content=True)

luna_instance = commands.Bot(
    command_prefix=environ.get('BOT_COMMAND_PREFIX', '-'),
    case_insensitive=environ.get('BOT_CASE_INSENSITIVE', False),
    owner_id=environ.get('BOT_OWNER_ID', None),
    strip_after_prefix=environ.get('BOT_STRIP_AFTER_PREFIX', True),
    intents=intents,
)


@luna_instance.event
async def on_ready() -> None:
    """Callback when bot is ready"""
    logging.info('The bot is ready [{0.user}]'.format(luna_instance))


@luna_instance.event
async def on_message(message: discord.Message) -> None:
    """Handler for new messages"""
    UserModel.get_or_create(
        discord_id=message.author.id,
    )

    await luna_instance.process_commands(message)
