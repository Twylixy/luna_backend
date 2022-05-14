from os import environ

from discord.commands.context import ApplicationContext
from discord.ext import commands

from app.callbacks import (
    bad_messages_menu_callback,
    link_filter_menu_callback,
    spam_detector_menu_callback,
)
from app.views import get_infractor_view


class InfractorCog(commands.Cog):
    """Represents an `infractor` cog-module"""

    def __init__(self, luna_instance: commands.Bot) -> None:
        """
        Initialize a new `infractor` instance

        Params:
            luna_instance: discord.ext.commands.Bot
        """
        self.luna_instance = luna_instance

    @commands.slash_command(
        name='infractor',
        description='The Infractor module Dashboard',
        guild_ids=environ.get('BOT_DEBUG_GUILDS_IDS', []).split(),
    )
    async def infractor(self, ctx: ApplicationContext) -> None:
        """
        Dashboard of the `infractor` module

        Params:
            ctx: discord.commands.context.ApplicationContext
        """
        view, infractor_embed = get_infractor_view(
            ctx,
            bad_messages_menu_callback,
            link_filter_menu_callback,
            spam_detector_menu_callback,
        )
        await ctx.respond(embed=infractor_embed, view=view)
