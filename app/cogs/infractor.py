from os import environ

import discord
from discord.commands.context import ApplicationContext
from discord.ext import commands
from discord.ui import Button, View

from app.callbacks import (
    bad_messages_menu_callback,
    link_filter_menu_callback,
    spam_detector_menu_callback,
)
from app.helpers import EMBED_DEFAULT_COLOR, TextedInfractorSettings
from app.models import InfractorSettingsModel


class InfractorCog(commands.Cog):
    """Represents an `infractor` cog-module"""

    def __init__(self, luna_instance: commands.Bot) -> None:
        """
        Initialize a new 'infractor' instance

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
        Setup command for infractor

        Params:
            ctx: commands.Context
        """
        infractor_settings, created = InfractorSettingsModel.get_or_create(
            guild_id=ctx.guild.id,
        )

        texted_infractor_settings = TextedInfractorSettings.get_texted_settings(
            infractor_settings,
        )

        infractor_embed = (
            discord.Embed(
                title=f'{texted_infractor_settings.infractor_is_enabled} Infractor | Dashboard',
                description='They cannot confronts to empress',
                color=EMBED_DEFAULT_COLOR,
            )
            .add_field(
                name='💬 Bad Messages',
                value=texted_infractor_settings.bad_words_is_enabled,
                inline=True,
            )
            .add_field(
                name='🌐 Link Filter',
                value=texted_infractor_settings.link_filter_is_enabled,
                inline=True,
            )
            .add_field(
                name='🌊 Spam Detector',
                value=texted_infractor_settings.spam_detector_is_enabled,
                inline=True,
            )
            .set_footer(text='The best way to control content')
        )

        bad_messages_button = Button(
            label='Bad Messages',
            style=discord.ButtonStyle.gray,
            emoji='💬',
        )
        link_filter_button = Button(
            label='Link Filter',
            style=discord.ButtonStyle.gray,
            emoji='🌐',
        )
        spam_detector_button = Button(
            label='Spam Detector',
            style=discord.ButtonStyle.gray,
            emoji='🌊',
        )

        bad_messages_button.callback = bad_messages_menu_callback
        link_filter_button.callback = link_filter_menu_callback
        spam_detector_button.callback = spam_detector_menu_callback

        view = View(
            bad_messages_button,
            link_filter_button,
            spam_detector_button,
        )

        await ctx.respond(embed=infractor_embed, view=view)
