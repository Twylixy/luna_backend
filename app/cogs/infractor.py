import discord
from discord.ext import commands
from discord.ui import Button, View

from app.callbacks import (
    bad_messages_menu_callback,
    link_filter_menu_callback,
    spam_detector_menu_callback,
)


class InfractorCog(commands.Cog):
    """Represents an `infractor` cog-module"""

    def __init__(self, luna_instance: commands.Bot) -> None:
        """
        Initialize a new 'infractor' instance

        Params:
            luna_instance: discord.ext.commands.Bot
        """
        self.luna_instance = luna_instance

    @commands.command()
    async def infractor(self, ctx: commands.Context) -> None:
        """
        Setup command for infractor

        Params:
            ctx: commands.Context
        """

        infractor_embed = (
            discord.Embed(
                title='🟢 Infractor | Dashboard',
                description='They cannot confronts to empress',
                color=discord.Color.from_rgb(54, 62, 122),
            )
            .add_field(
                name='💬 Bad Messages',
                value='☑️ Enabled',
                inline=True,
            )
            .add_field(
                name='🌐 Link Filter',
                value='❌ Disabled',
                inline=True,
            )
            .add_field(
                name='🌊 Spam Detector',
                value='☑️ Enabled',
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

        await ctx.send(embed=infractor_embed, view=view)
