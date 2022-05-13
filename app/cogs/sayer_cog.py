import discord
import peewee
from discord.ext import commands

from app.helpers import MessageAnalyzer
from app.models import SavedMessageModel


class SayerCog(commands.Cog):
    """Represent a `sayer` cog-module"""

    def __init__(self, luna_instance: commands.Bot) -> None:
        """
        Initialize a new `sayer` instance

        Params:
            luna_instance: discord.ext.commands.Bot
        """
        self.luna_instance = luna_instance

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """
        Handle a messages

        Params:
            message: discord.Message
        """
        if self.luna_instance.user.mentioned_in(message):
            random_message = (
                SavedMessageModel.select()
                .where(SavedMessageModel.hidden == False)
                .order_by(peewee.fn.Random())
                .limit(1)
            ).get()

            return await message.reply(random_message.text)

        analyzer = MessageAnalyzer(message)

        if analyzer.is_valid:
            SavedMessageModel.create(
                discord_id=message.author.id,
                text=message.content,
            )
